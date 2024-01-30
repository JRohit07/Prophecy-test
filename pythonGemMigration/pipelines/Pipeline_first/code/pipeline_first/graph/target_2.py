from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def target_2(spark: SparkSession, in0: DataFrame):
    from pyspark.dbutils import DBUtils
    in0.write\
        .format("jdbc")\
        .option("url", f"{Config.JDBC}/{Config.JDBC_DATABASE}")\
        .option("dbtable", Config.JDBC_DEST_TABLE)\
        .option("user", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("driver", Config.DRIVER_NAME)\
        .mode("overwrite")\
        .save()
