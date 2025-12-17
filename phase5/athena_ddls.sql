-- phase5/athena_ddls.sql
-- Creates database + tables for processed vitals and predictions
-- Replace YOURNAME with your bucket name where needed.

CREATE DATABASE IF NOT EXISTS healthcare_analysis_db;

CREATE EXTERNAL TABLE IF NOT EXISTS heart_attack_processed_data (
  `Patient ID` string,
  `Heart Rate` double,
  `Sleep Hours Per Day` double,
  `Physical Activity Days Per Week` int,
  `Blood Pressure` string,
  `Age` int,
  `Sex` string,
  `Cholesterol` double,
  `Diabetes` int,
  `Family History` int,
  `Smoking` int,
  `Obesity` int,
  `Alcohol Consumption` double,
  `Exercise Hours Per Week` double,
  `Diet` string,
  `Previous Heart Problems` int,
  `Medication Use` int,
  `Stress Level` int,
  `Sedentary Hours Per Day` double,
  `Income` bigint,
  `BMI` double,
  `Triglycerides` int,
  `Country` string,
  `Continent` string,
  `Hemisphere` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar"     = "\""
)
LOCATION 's3://healthcare-project-data-YOURNAME/processed/final_health_dataset_csv/'
TBLPROPERTIES ('skip.header.line.count'='1');

CREATE EXTERNAL TABLE IF NOT EXISTS heart_attack_predictions (
  `Patient ID` string,
  `Heart Attack Risk` double,
  `Risk_Status` string,
  `ScoredAt` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar"     = "\""
)
LOCATION 's3://healthcare-project-data-YOURNAME/predictions/'
TBLPROPERTIES ('skip.header.line.count'='1');
