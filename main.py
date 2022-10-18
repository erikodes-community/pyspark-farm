from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("data/farm.csv", inferSchema=True, header=True)

print(df)