# Heart Health Alert System  
### End-to-End Machine Learning Pipeline Using AWS EMR, SageMaker, Lambda, SNS, Athena, and S3

---

## 🧭 Project Overview

This project implements a complete cloud-based **heart attack risk prediction and alerting system** using Amazon Web Services.  
It simulates patient vitals, processes health data at scale, trains an XGBoost model, generates real-time predictions with AWS Lambda, triggers alerts through SNS, and delivers data insights with Athena.

The system reflects how modern hospitals and remote patient-monitoring systems use cloud-based machine learning for proactive cardiac risk assessment.

---

## 📊 Final Deliverables

### **1. End-to-End AWS ML Pipeline**
A fully operational pipeline integrating:  
- Amazon S3 (data lake)  
- AWS EMR (Spark preprocessing)  
- Amazon SageMaker (model training & deployment)  
- AWS Lambda (automated inference)  
- Amazon SNS (high-risk alerts)  
- Amazon Athena (analytics)

### **2. SNS High-Risk Alert Email**  
_Email notification triggered when prediction > 0.45_  
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/28b62312-8898-4795-a82c-4abd51979369" />


### **3. Athena Analytics Queries**  
_Insights on high-risk patterns, age segmentation, sleep correlation, and activity-to-heart-rate behavior._  
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/8b2fec8c-8c49-40e2-8add-7f2a83711a19" />
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/13f150d5-96d3-492c-8c89-8505b51c344b" />

---

## 🧩 Project Phases

---

## **Phase I – Data Generation & Ingestion**
- Generated 7-day simulated vitals for 20 patients  
- Uploaded both historical and simulated datasets into S3  
- Output: `simulated_vitals.csv`

**Files Included:**
```
phase1/generate_simulated.py
phase1/upload_to_s3.sh
```

---

## **Phase II – Data Processing Using EMR (Spark)**
- Aggregated daily vitals into weekly averages  
- Cleaned historical dataset  
- Joined datasets on Patient ID  
- Saved final dataset to `processed/` on S3  

**Files Included:**
```
phase2/spark/main.py
```

---

## **Phase III – Machine Learning Model (SageMaker)**
- Preprocessed dataset (split BP, encode categoricals, remove IDs)  
- Trained XGBoost binary classifier  
- Deployed real-time SageMaker endpoint  
- Generated `feature_list.txt`  

**Files Included:**
```
phase3/preprocess.py
phase3/sagemaker_train.py
phase3/notebook/Yourname_HeartAttack_Prediction.ipynb
```

---

## **Phase IV – Automated Prediction & SNS Alerts (Lambda)**
- Lambda loads the most recent processed CSV from S3  
- Preprocesses rows using `feature_list.txt`  
- Sends rows for real-time prediction using SageMaker endpoint  
- Saves results to `/predictions` in S3  
- Triggers SNS alerts for patients with risk > 0.45  

**Files Included:**
```
phase4/lambda_function.py
```

---

## **Phase V – Analytics via Amazon Athena**
- Created two Athena external tables:
  - `heart_attack_processed_data`
  - `heart_attack_predictions`
- Executed SQL analyses for:
  - High-risk patient ranking  
  - Risk by age groups  
  - Sleep duration correlation  
  - Activity vs heart rate  

**Files Included:**
```
phase5/athena_ddls.sql
```

---

## ⚙️ Tools & Technologies Used

- **Amazon S3** – Storage and ingestion  
- **AWS EMR + Spark** – Distributed data preprocessing  
- **Amazon SageMaker** – ML training, evaluation, and deployment  
- **AWS Lambda** – Automated inference  
- **Amazon SNS** – Email alerts  
- **Amazon Athena** – SQL-based analytics  
- **Python** – pandas, boto3, PySpark  

---

## 🧠 Dataset Information

### **Simulated Dataset (Phase 1)**
20 patients × 7 days  
- Heart Rate  
- BP Systolic / Diastolic  
- Sleep Hours  
- Physical Activity  
- Timestamp  

### **Historical Dataset**
Kaggle Heart Attack Prediction Dataset - https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset
Features include:
- Age, Sex, Cholesterol, Diabetes  
- BMI, Stress Level, Exercise Hours  
- Blood Pressure  
- Heart Attack Risk (label)

---

## 👥 Intended Users

- Cardiologists & Emergency Medical Teams  
- Healthcare Analysts  
- Insurance Risk Analysts  
- Clinical Researchers  
- Remote Monitoring Teams  

---

## 💡 Key Insights Generated

- High-risk patient detection  
- Correlation between sleep hours and predicted risk  
- Age-based risk patterns  
- Activity level vs heart rate & model prediction behavior  

---

## 📂 Repository Structure

```
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
```

---

## 🔗 Project Repository  
**[https://github.com/YOURUSERNAME/heart-health-alert](https://github.com/ishupandi15/heart-health-alert-system)**

---

## 🎞️ Project Video  
Link added in `project_report.docx`.

---
