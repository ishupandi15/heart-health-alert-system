"""
phase3/sagemaker_train.py
Showcase script containing the key logic used in SageMaker Notebook
for training & deploying the XGBoost heart attack prediction model.

NOTE:
You will NOT run this file in GitHub.
The actual execution happens inside SageMaker Notebook.
"""

import boto3
import pandas as pd
import io
from sagemaker import get_execution_role
from sklearn.model_selection import train_test_split

# Replace with your bucket
bucket = "healthcare-project-data-YOURNAME"
region = "us-east-1"
role = get_execution_role()

# Load processed file from S3 (placeholder logic for notebook)
def load_processed_from_s3(key):
    s3 = boto3.client("s3", region_name=region)
    obj = s3.get_object(Bucket=bucket, Key=key)
    return pd.read_csv(io.BytesIO(obj["Body"].read()))

# Preprocessing (imported from preprocess.py)
from preprocess import preprocess_health_data

# Example training workflow (as shown in notebook)
def train_xgboost_model(df):
    df_proc = preprocess_health_data(df)
    
    y = df_proc["Heart Attack Risk"].astype(int)
    X = df_proc.drop(columns=["Heart Attack Risk"])

    # train/test split
    train_df, test_df = train_test_split(
        pd.concat([y, X], axis=1), 
        test_size=0.2, 
        random_state=42, 
        stratify=y
    )

    # Save feature list
    features = list(X.columns)
    with open("feature_list.txt", "w") as f:
        f.write("\n".join(features))

    print("Data ready for SageMaker training job.")
    print("Train shape:", train_df.shape, "Test shape:", test_df.shape)

    # Actual SageMaker training occurs in the notebook, not here.
    return train_df, test_df, features
