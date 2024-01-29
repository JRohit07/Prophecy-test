from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_3(spark: SparkSession) -> DataFrame:
    import os

    return spark.read\
        .format("jdbc")\
        .option("url", Config.JDBC + "/" + Config.JDBC_DATABASE)\
        .option("user", dbutils.secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", dbutils.secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("dbtable", f"{Config.TEST}_table_automation")\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
