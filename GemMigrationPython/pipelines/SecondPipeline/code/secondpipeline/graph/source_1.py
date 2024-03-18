from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def source_1(spark: SparkSession) -> DataFrame:
    from pyspark.dbutils import DBUtils

    return spark.read\
        .format("jdbc")\
        .option("url", Config.JDBC_URL)\
        .option("user", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("dbtable", Config.JDBC_TABLE_SOURCE)\
        .option("pushDownPredicate", True)\
        .option("driver", "com.mysql.jdbc.Driver")\
        .load()
