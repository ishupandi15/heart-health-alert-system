"""
phase4/lambda_function.py
Showcase Lambda function for invoking SageMaker endpoint
and sending alerts via SNS when heart attack risk is high.

NOTE:
This code is NOT executed in GitHub.
It is added to the repository for project completeness (Phase 4).
You run it only inside AWS Lambda.
"""

import boto3
import csv
import io
import pandas as pd
import json
from datetime import datetime

runtime = boto3.client("sagemaker-runtime")
s3 = boto3.client("s3")
sns = boto3.client("sns")

# Replace these two BEFORE running in AWS Lambda
ENDPOINT_NAME = "xgb-heart-attack-endpoint-REPLACE"
BUCKET_NAME = "healthcare-project-data-YOURNAME"

PROCESSED_PREFIX = "processed/final_health_dataset_csv/"
FEATURE_LIST_KEY = "preprocess/feature_list.txt"
ALERT_TOPIC_ARN = "arn:aws:sns:us-east-1:YOURACCOUNT:YOURNAME-health-alerts"

def load_feature_list():
    """Load expected features learned during SageMaker training."""
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=FEATURE_LIST_KEY)
    features = obj["Body"].read().decode("utf-8").splitlines()
    return [f.strip() for f in features if f.strip()]

def preprocess_row_for_model(row, expected_features):
    """Convert one row into model-ready numeric features."""
    df = pd.DataFrame([row])

    # Split BP
    if "Blood Pressure" in df.columns:
        bp = df["Blood Pressure"].astype(str).str.split("/", expand=True)
        df["BP_Systolic"] = pd.to_numeric(bp[0], errors="coerce")
        df["BP_Diastolic"] = pd.to_numeric(bp[1], errors="coerce")
        df.drop(columns=["Blood Pressure"], inplace=True)

    # Drop non-feature columns
    df = df.drop(columns=[
        "Patient ID", "Country", "Continent", "Hemisphere"
    ], errors="ignore")

    # Simple example encoding
    if "Sex" in df.columns:
        df["Sex_Male"] = (df["Sex"].astype(str).str.lower() == "male").astype(int)
    df = df.drop(columns=["Sex"], errors="ignore")

    df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

    # Add missing columns as 0
    for col in expected_features:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_features]
    return df

def lambda_handler(event, context):
    expected_features = load_feature_list()

    # Get latest processed CSV
    objs = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PROCESSED_PREFIX)
    csv_files = [o["Key"] for o in objs.get("Contents", []) if o["Key"].endswith(".csv")]

    if not csv_files:
        return {"statusCode": 404, "body": "No processed CSV found"}

    latest_csv = csv_files[0]
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=latest_csv)
    data = obj["Body"].read().decode("utf-8").splitlines()

    reader = csv.DictReader(data)
    rows = list(reader)

    results = []
    alerts = 0
    alert_details = []

    # Process first 50 rows
    for i, row in enumerate(rows[:50]):
        pid = row.get("Patient ID", f"Row{i+1}")
        df_row = preprocess_row_for_model(row, expected_features)
        payload = df_row.to_csv(header=False, index=False)

        # Call the SageMaker endpoint
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="text/csv",
            Body=payload
        )

        score = float(response["Body"].read().decode("utf-8"))
        results.append({"Patient ID": pid, "score": score})

        if score > 0.45:
            alerts += 1
            alert_details.append({"Patient ID": pid, "Score": score})

    # Save predictions to S3
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    key = f"predictions/heart_attack_predictions_{ts}.csv"

    buffer = io.StringIO()
    pd.DataFrame(results).to_csv(buffer, index=False)
    s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=buffer.getvalue().encode("utf-8"))

    # Send SNS alert if needed
    if alerts > 0:
        text = "\n".join([f"{x['Patient ID']}: {x['Score']}" for x in alert_details])
        sns.publish(
            TopicArn=ALERT_TOPIC_ARN,
            Subject="Heart Health Alert",
            Message=f"High-risk patients detected:\n{text}"
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "processed": len(rows),
            "alerts": alerts,
            "details": alert_details
        })
    }
