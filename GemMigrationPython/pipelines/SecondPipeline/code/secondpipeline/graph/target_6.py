from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def target_6(spark: SparkSession, in0: DataFrame):
    import os
    in0.write\
        .format("jdbc")\
        .option("url", f"{Config.JDBC}{Config.JDBC_DATABASE}")\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", os.environ["JDBC_USERNAME"])\
        .option("password", os.environ["JDBC_PASSWORD"])\
        .option("driver", Config.DRIVER_NAME)\
        .mode("overwrite")\
        .save()
