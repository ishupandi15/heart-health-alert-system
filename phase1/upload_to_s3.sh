#!/usr/bin/env bash
# Simple helper to create the S3 bucket (if needed) and upload simulated_vitals.csv
# IMPORTANT: Replace YOURNAME with your unique identifier (no spaces) and REGION if needed.

BUCKET="healthcare-project-data-YOURNAME"
REGION="us-east-1"
SIM_FILE="simulated_vitals.csv"

if [ "$BUCKET" = "healthcare-project-data-YOURNAME" ]; then
  echo "Please edit this script and replace YOURNAME with your name (bucket must be unique)."
  exit 1
fi

echo "Creating bucket (if it doesn't exist): ${BUCKET} in ${REGION}"
aws s3api create-bucket --bucket ${BUCKET} --region ${REGION} --create-bucket-configuration LocationConstraint=${REGION} 2>/dev/null || true

echo "Uploading ${SIM_FILE} to s3://${BUCKET}/raw/simulated/${SIM_FILE}"
aws s3 cp "${SIM_FILE}" "s3://${BUCKET}/raw/simulated/${SIM_FILE}"
echo "Upload complete."
