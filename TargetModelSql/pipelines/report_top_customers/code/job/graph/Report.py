from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Report(spark: SparkSession, in0: DataFrame):
    if Config.fabricName == "dev":
        in0.write\
            .option("header", True)\
            .option("sep", ",")\
            .option("ignoreLeadingWhiteSpace", True)\
            .option("ignoreTrailingWhiteSpace", True)\
            .mode("overwrite")\
            .option("separator", ",")\
            .option("header", True)\
            .csv("dbfs:/Prophecy/a95b0b9c2b76937c5ab701265a2a9cbf/report-top-customers.csv")
    else:
        raise Exception("No valid dataset present to read fabric")
