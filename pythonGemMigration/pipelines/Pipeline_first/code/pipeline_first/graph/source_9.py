from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_9(spark: SparkSession) -> DataFrame:
    import os

    return spark.read\
        .format("jdbc")\
        .option("url", Config.JDBC + "/" + Config.JDBC_DATABASE)\
        .option("user", os.environ("JDBC_USERNAME"))\
        .option("password", os.environ("JDBC_PASSWORD"))\
        .option("query", f"select * from {Config.JDBC_TABLE}")\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
