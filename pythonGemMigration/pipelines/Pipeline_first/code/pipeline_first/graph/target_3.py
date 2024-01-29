from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def target_3(spark: SparkSession, in0: DataFrame):
    import os
    in0.write\
        .format("jdbc")\
        .option("url", Config.JDBC + "/" + Config.JDBC_DATABASE)\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", dbutils.secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", dbutils.secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("driver", "com.mysql.jdbc.Driver")\
        .mode("overwrite")\
        .save()
