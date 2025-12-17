"""
phase3/preprocess.py
Helper functions to preprocess the merged dataset before training in SageMaker.
Showcase-only: include in repo for grading and for copy-paste into your notebook.
"""
import pandas as pd

def preprocess_health_data(df: pd.DataFrame) -> pd.DataFrame:
    # Split Blood Pressure into numeric components if present
    if "Blood Pressure" in df.columns:
        bp = df["Blood Pressure"].astype(str).str.split("/", n=1, expand=True)
        df["BP_Systolic"] = pd.to_numeric(bp[0], errors="coerce")
        df["BP_Diastolic"] = pd.to_numeric(bp[1], errors="coerce")
        df.drop(columns=["Blood Pressure"], inplace=True)

    # Drop identifiers that shouldn't be features
    df = df.drop(columns=["Patient ID","Country","Continent","Hemisphere"], errors="ignore")

    # Example: convert categorical columns to dummies and fill missing values
    df = pd.get_dummies(df, drop_first=True).fillna(0)

    return df
