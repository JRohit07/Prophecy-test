from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def source_5(spark: SparkSession) -> DataFrame:
    import os

    return spark.read\
        .format("jdbc")\
        .option("url", f"{Config.JDBC}{Config.JDBC_DATABASE}")\
        .option("user", os.environ["JDBC_USERNAME"])\
        .option("password", os.environ["JDBC_PASSWORD"])\
        .option("dbtable", "test_table_automation")\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
