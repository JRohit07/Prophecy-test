from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def target_7(spark: SparkSession, in0: DataFrame):
    import os
    in0.write\
        .format("jdbc")\
        .option("url", Config.JDBC + "/test_database")\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", Config.TEST + "_" + Config.USER)\
        .option("password", Config.ADM + Config.IN)\
        .option("driver", Config.DRIVER_NAME)\
        .mode("overwrite")\
        .save()
