from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum as _sum, round as _round, col, concat_ws
from pyspark.sql.types import IntegerType

# Replace YOURNAME before running in AWS (showcase only)
HIST_PATH = "s3://healthcare-project-data-YOURNAME/raw/historical/heart_attack_prediction_dataset.csv"
SIM_PATH  = "s3://healthcare-project-data-YOURNAME/raw/simulated/simulated_vitals.csv"
OUT_PATH  = "s3://healthcare-project-data-YOURNAME/processed/final_health_dataset_csv/"

spark = SparkSession.builder.appName("AggregateVitalsJoinFinal").getOrCreate()

# Load datasets
hist = spark.read.option("header", True).csv(HIST_PATH, inferSchema=True)
sim  = spark.read.option("header", True).csv(SIM_PATH, inferSchema=True)

# Aggregate 7-day vitals per patient
agg = sim.groupBy("Patient ID").agg(
    _round(avg(col("Heart Rate")), 0).alias("Heart Rate"),
    _round(avg(col("BP_Systolic")), 0).alias("AvgBP_Systolic"),
    _round(avg(col("BP_Diastolic")), 0).alias("AvgBP_Diastolic"),
    _round(avg(col("Sleep Hours Per Day")), 2).alias("Sleep Hours Per Day"),
    _sum(col("Physical Activity Per day")).alias("Physical Activity Days Per Week")
)

# Rebuild Blood Pressure string
agg = agg.withColumn(
    "Blood Pressure",
    concat_ws("/", col("AvgBP_Systolic").cast(IntegerType()), col("AvgBP_Diastolic").cast(IntegerType()))
).drop("AvgBP_Systolic", "AvgBP_Diastolic")

# Drop old vitals + risk column from historical data
drop_cols = ["Heart Rate", "Blood Pressure", "Sleep Hours Per Day",
             "Physical Activity Days Per Week", "Heart Attack Risk"]

hist_clean = hist.drop(*[c for c in drop_cols if c in hist.columns])

# Left join — keeps all simulated IDs
final = agg.join(hist_clean, on="Patient ID", how="left")

# Save to S3
final.coalesce(1).write.mode("overwrite").option("header", True).csv(OUT_PATH)

print("Final dataset written to:", OUT_PATH)
print("Columns:", final.columns)

spark.stop()
