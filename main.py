from pyspark.sql import SparkSession
from pyspark.sql import Window
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("data/farm.csv", inferSchema=True, header=True)

window = Window.partitionBy('tag').orderBy('hay_ration')

# print(df)

df = df.withColumn('rank', F.rank().over(window))

df.show()

"""
+-------+-----+----------+----+
|   name|  tag|hay_ration|rank|
+-------+-----+----------+----+
|  frank|horse|        30|   1|
|frankie|horse|        65|   2|
|    cow|  cow|        10|   1|
|   joe2|  cow|        10|   1|
|    joe|  cow|        11|   3|
|   pig1|  pig|        20|   1|
|   pig2|  pig|        40|   2|
|   pig3|  pig|        50|   3|
|   pig4|  pig|        60|   4|
|   pig6|  pig|        70|   5|
|   pig5|  pig|        80|   6|
+-------+-----+----------+----+

"""