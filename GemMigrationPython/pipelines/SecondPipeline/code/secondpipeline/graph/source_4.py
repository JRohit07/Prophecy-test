from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def source_4(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("jdbc")\
        .option("url", f"{Config.JDBC}{Config.JDBC_DATABASE}")\
        .option("user", "{}".format(f"{Config.TEST}_{Config.USER}"))\
        .option("password", "{}".format(f"{Config.ADM}{Config.IN}"))\
        .option("query", f"select * from {Config.JDBC_TABLE}")\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
