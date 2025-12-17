💓 Heart Health Alert System
Using AWS EMR, SageMaker, Lambda, SNS, Athena, and S3

🧭 Project Overview

This project implements a complete cloud-based intelligent health monitoring and alert system using AWS.
It simulates patient vitals, processes them at scale, trains a predictive model, and sends real-time alerts for high-risk patients.

The system integrates several AWS services to build an end-to-end ML pipeline:

Amazon S3 – Data storage and ingestion

AWS EMR (Spark) – Big data processing

Amazon SageMaker – Model training & endpoint deployment

AWS Lambda – Automated prediction

Amazon SNS – Email alerting

Amazon Athena – Analytics on predictions & vitals

This architecture reflects a real-world remote-health monitoring system used in modern hospitals.

📊 Final Deliverables
🔹 End-to-End AWS ML Pipeline

A fully functional architecture performing:

Data ingestion

Spark preprocessing

XGBoost model training

Real-time model inference

Automated alerts

SQL analytics and reporting

🔹 SNS Alert Example

Screenshot: (S6 goes here — high-risk patient alert email)

🔹 Athena Analytics Output

Screenshot: (S7 — SQL query results)

🧩 Project Phases
Phase I – Data Generation & Ingestion

Generated 7-day simulated patient vitals

Uploaded all raw data to Amazon S3

Historical dataset + simulated vitals stored in /raw folders

📄 Files Included:

phase1/generate_simulated.py
phase1/upload_to_s3.sh

Phase II – Data Processing on EMR (Spark)

Aggregated daily vitals into weekly averages

Cleaned and transformed historical dataset

Performed left join on Patient ID

Wrote final ML-ready dataset back to S3

📄 Files Included:

phase2/spark/main.py

Phase III – SageMaker Training & Deployment

Preprocessed the dataset (split BP, one-hot encoding, drop identifiers)

Trained an XGBoost binary classifier

Deployed a real-time inference endpoint

Created feature_list.txt for Lambda preprocessing

📄 Files Included:

phase3/preprocess.py
phase3/sagemaker_train.py
phase3/notebook/Yourname_HeartAttack_Prediction.ipynb

Phase IV – Automated Prediction & SNS Alerts

Lambda retrieves processed CSV from S3

Preprocesses each row using feature_list.txt

Sends rows to SageMaker endpoint for real-time scoring

Stores prediction results in S3 under /predictions

Sends SNS email alert for any patient with risk > 0.45

📄 Files Included:

phase4/lambda_function.py

Phase V – SQL Analytics using Athena

Created two external tables:

Processed vitals data

Prediction results

Executed advanced SQL queries for:

High-risk detection

Age group risk analysis

Sleep-hour correlation

Activity vs heart rate

📄 Files Included:

phase5/athena_ddls.sql

⚙️ Tools & Technologies Used

AWS S3 – Data storage

AWS EMR (Spark) – Large-scale preprocessing

Amazon SageMaker – Machine learning pipeline

AWS Lambda – Automated inference

Amazon SNS – Email alert notifications

Amazon Athena – Analytics engine

Python (boto3, pandas, PySpark)

🧠 Dataset Description
Simulated Dataset (Phase 1)

20 unique patient IDs

7 days of vitals per patient

Columns:

Heart Rate

BP Systolic / Diastolic

Sleep Hours

Physical Activity

Timestamp

Historical Dataset

Includes:

Age, Sex, Cholesterol, Diabetes

Stress Level, BMI, Exercise Hours

Heart Attack Risk label

👥 Intended Users

Cardiologists

Healthcare providers

Researchers & analysts

Medical administrators

Insurance risk analysts

💡 Insights Provided

Identification of high-risk patients

Trends by age group and demographics

Sleep, activity, and heart rate correlation with predicted risk

Model-driven alerts for early intervention

📂 Repository Structure
phase1/
   ├─ generate_simulated.py
   └─ upload_to_s3.sh

phase2/
   └─ spark/main.py

phase3/
   ├─ preprocess.py
   ├─ sagemaker_train.py
   └─ notebook/Yourname_HeartAttack_Prediction.ipynb

phase4/
   └─ lambda_function.py

phase5/
   └─ athena_ddls.sql

docs/
   ├─ project_report.docx
   └─ screenshots/

README.md
LICENSE
.gitignore

🔗 Project Repository

Add your link here once uploaded:
👉 https://github.com/YOURUSERNAME/heart-health-alert

🎞️ Project Video

Include in your project_report.docx (Google Drive / Zoom / YouTube link)

🎓 Submitted By

YOUR NAME
IFT 512 – Advanced Big Data Analytics / AI
Arizona State University | Fall 2025
