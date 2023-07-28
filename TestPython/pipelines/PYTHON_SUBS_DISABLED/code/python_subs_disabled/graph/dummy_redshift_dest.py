from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def dummy_redshift_dest(spark: SparkSession, in0: DataFrame):
    from pyspark.dbutils import DBUtils
    in0.write\
        .format("com.databricks.spark.redshift")\
        .option("url", "test")\
        .option("user", DBUtils(spark).secrets.get(scope = "test", key = f"test"))\
        .option("password", DBUtils(spark).secrets.get(scope = "test", key = f"test"))\
        .option("dbtable", "test")\
        .option("url", "test")\
        .save()
