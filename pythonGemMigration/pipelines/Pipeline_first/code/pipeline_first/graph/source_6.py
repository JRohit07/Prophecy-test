from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_6(spark: SparkSession) -> DataFrame:
    import os

    return spark.read\
        .format("jdbc")\
        .option("url", Config.JDBC_URL)\
        .option("user", Config.JDBC_USER_STRING)\
        .option("password", Config.JDBC_PASSWORD_STRING)\
        .option("query", Config.SQL_QUERY)\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
