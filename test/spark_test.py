import time
from typing import List, Any
import os
import sys

from pyspark.sql import SparkSession

# os.environ['PYSPARK_PYTHON'] = sys.executable
# os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# os.environ['PYSPARK_PYTHON'] = "/Users/aaronge/PycharmProjects/pythonProject/venv/bin/python"

spark = SparkSession.builder. \
    appName("pyspark-learning"). \
    master("spark://127.0.0.1:7077"). \
    config("spark.executor.memory", "512m"). \
    config("spark.executor.cores", 1). \
    getOrCreate()

sc = spark.sparkContext

big_list = range(100000)
rdd = sc.parallelize(big_list, 100)  # will create 100 tasks in parallel...
rdd_map = rdd.map(lambda x: x * 2)
odds = rdd_map.filter(lambda x: x % 2 != 0)
result = odds.repartition(10).collect()  # 10 tasks created to repartition the data

print(result)


# This while loop is to just make this program blocking.
while True:
    time.sleep(1)

# export PYSPARK_PYTHON=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# export PYSPARK_DRIVER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3