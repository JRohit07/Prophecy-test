from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_4(spark: SparkSession) -> DataFrame:
    import os

    return spark.read\
        .format("jdbc")\
        .option("url", "jdbc:mysql://3.101.152.38:3306/" + Config.JDBC_DATABASE)\
        .option("user", dbutils.secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", dbutils.secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("query", f"select * from {Config.JDBC_TABLE}")\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
