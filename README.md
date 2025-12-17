project:
  title: "Heart Health Alert System"
  subtitle: "Intelligent Heart Attack Prediction Pipeline Using AWS EMR, SageMaker, Lambda, SNS, Athena, and S3"
  author: "YOUR NAME"
  institution: "Arizona State University"
  course: "IFT 512 – Advanced Big Data Analytics / AI"
  instructor: "Durgesh Sharma"

description: |
  This project builds an end-to-end automated healthcare analytics system on AWS.
  It simulates real patient vitals, preprocesses data using EMR Spark, trains and deploys an
  XGBoost model with SageMaker, performs real-time inference with Lambda, sends
  high-risk alerts with SNS, and runs analytical queries using Athena.

repository_structure:
  phase1:
    files:
      - phase1/generate_simulated.py
      - phase1/upload_to_s3.sh
    purpose: "Create simulated 7-day vitals and upload datasets to S3."

  phase2:
    files:
      - phase2/spark/main.py
    purpose: "Run Spark job on EMR to aggregate vitals, join historical data, and output final dataset."

  phase3:
    files:
      - phase3/preprocess.py
      - phase3/sagemaker_train.py
      - phase3/notebook/Yourname_HeartAttack_Prediction.ipynb
    purpose: "Preprocess, train, evaluate, and deploy XGBoost model using SageMaker."

  phase4:
    files:
      - phase4/lambda_function.py
    purpose: "Lambda pulls processed data from S3, invokes deployed model, generates predictions, and sends SNS alerts."

  phase5:
    files:
      - phase5/athena_ddls.sql
    purpose: "Create Athena external tables and run analytical SQL queries on predictions and vitals."

  documentation:
    - docs/project_report.docx
    - docs/screenshots/

execution_order:
  step1:
    name: "Generate Simulated Data"
    file: "phase1/generate_simulated.py"
    run_command: "python3 generate_simulated.py"
    run_where: "Local machine or AWS Cloud9"
    produces:
      - "simulated_vitals.csv"
    description: |
      Generates synthetic vitals for 20 patients over 7 days.
      Mimics data from wearable healthcare devices.

  step2:
    name: "Upload Data to S3"
    file: "phase1/upload_to_s3.sh"
    run_command: "./upload_to_s3.sh"
    run_where: "Local terminal / Cloud9"
    uploads_to:
      - "s3://<bucket>/raw/simulated/"
      - "s3://<bucket>/raw/historical/"
    description: |
      Uploads simulated vitals and historical dataset into respective S3 folders,
      preparing the data for EMR processing.

  step3:
    name: "Run Spark Job on EMR"
    file: "phase2/spark/main.py"
    run_command: "spark-submit main.py"
    run_where: "EMR Master Node or EMR Step"
    reads:
      - "raw/simulated/"
      - "raw/historical/"
    produces:
      - "processed/final_health_dataset_csv/"
    description: |
      Spark aggregates 7-day vitals into weekly averages, cleans historical data,
      and performs a left join to keep only the 20 simulated patients.
      Outputs machine-learning-ready dataset into processed/ folder in S3.

  step4:
    name: "Preprocess, Train & Deploy ML Model"
    files:
      - "phase3/notebook/Yourname_HeartAttack_Prediction.ipynb"
      - "phase3/preprocess.py"
    run_where: "Amazon SageMaker Notebook"
    produces:
      - "XGBoost trained model"
      - "SageMaker real-time inference endpoint"
      - "preprocess/feature_list.txt"
    description: |
      Loads processed dataset from S3, preprocesses features,
      trains an XGBoost model, deploys an inference endpoint, and generates feature_list.txt
      to ensure Lambda uses identical feature order.

  step5:
    name: "Lambda Real-Time Prediction & SNS Alerts"
    file: "phase4/lambda_function.py"
    run_where: "AWS Lambda Console"
    triggers: "Manual test or automated scheduled invocation"
    reads:
      - "processed/final_health_dataset_csv/"
      - "preprocess/feature_list.txt"
    writes:
      - "predictions/heart_attack_predictions_<timestamp>.csv"
    alerts:
      - "SNS email to subscribed doctors"
    description: |
      Lambda preprocesses new data rows, invokes the SageMaker endpoint,
      writes predictions to S3, and triggers email alerts for high-risk patients (score > 0.45).

  step6:
    name: "Analytics in Athena"
    file: "phase5/athena_ddls.sql"
    run_where: "Athena Query Editor"
    description: |
      Creates two external tables (processed vitals + predictions) and runs queries
      to analyze risk patterns, age groups, sleep correlation, and more.

outputs:
  s3_folders:
    - "raw/historical/"
    - "raw/simulated/"
    - "processed/final_health_dataset_csv/"
    - "preprocess/feature_list.txt"
    - "predictions/*.csv"
  alerts:
    - "SNS email notifications for HIGH-RISK patients"
  analytics:
    - "Athena dashboards and query results"

screenshots_required:
  S1: "Upload simulated data to S3"
  S2: "EMR cluster creation"
  S3: "Processed data folder in S3"
  S4: "SageMaker model training & endpoint"
  S5: "SNS topic"
  S6: "SNS alert email"
  S7: "Athena query results"

video:
  description: "5–6 minute project walkthrough including architecture, workflow, AWS execution, model training, alerts, and analytics."
  included_in: "docs/project_report.docx"

license: "MIT License"
acknowledgements:
  - "Arizona State University"
  - "IFT 512 – Advanced Big Data Analytics"
  - "Instructor: Durgesh Sharma"
