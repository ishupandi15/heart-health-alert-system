import pandas as pd
import random
import time
import argparse

# List of example patient IDs (20)
patient_ids = [
    "BMW7812","CZE1114","BNI9906","JLN3497","GFO8847","ZOO7941",
    "WYV0966","XXM0972","XCQ5937","FTJ5456","HSD6283","YSP0073",
    "FPS0415","YYU9565","VTW9069","DCY3282","DXB2434","COP0566",
    "XBI0592","RQX1211"
]

def generate(out_file: str, days: int = 7):
    records = []
    base_ts = int(time.time())
    for pid in patient_ids:
        for i in range(days):
            record = {
                "Patient ID": pid,
                "Heart Rate": random.randint(60, 110),
                "BP_Systolic": random.randint(100, 170),
                "BP_Diastolic": random.randint(60, 120),
                "Sleep Hours Per Day": round(random.uniform(3.0, 9.0), 1),
                "Physical Activity Per day": random.randint(0, 1),
                "Timestamp": base_ts + i
            }
            records.append(record)
    df = pd.DataFrame(records)
    df.to_csv(out_file, index=False)
    print(f"Generated {out_file} with {len(df)} rows ({len(patient_ids)} patients x {days} days)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate simulated vitals CSV")
    parser.add_argument("--out", default="simulated_vitals.csv", help="Output CSV file name")
    parser.add_argument("--days", type=int, default=7, help="Days of vitals per patient")
    args = parser.parse_args()
    generate(args.out, args.days)
