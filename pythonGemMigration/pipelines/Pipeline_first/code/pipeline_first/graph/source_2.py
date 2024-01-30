from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_2(spark: SparkSession) -> DataFrame:
    from pyspark.dbutils import DBUtils

    return spark.read\
        .format("jdbc")\
        .option("url", f"{Config.JDBC}/{Config.JDBC_DATABASE}")\
        .option("user", DBUtils(spark).secrets.get(scope = Config.SCOPE, key = "username"))\
        .option("password", DBUtils(spark).secrets.get(scope = Config.SCOPE, key = "password"))\
        .option("dbtable", Config.JDBC_TABLE)\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
