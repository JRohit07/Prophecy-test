from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def target_9(spark: SparkSession, in0: DataFrame):
    import os
    in0.write\
        .format("jdbc")\
        .option("url", "jdbc:mysql://3.101.152.38:3306/" + Config.JDBC_DATABASE)\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", os.environ("JDBC_USERNAME"))\
        .option("password", os.environ("JDBC_PASSWORD"))\
        .option("driver", Config.DRIVER_NAME)\
        .mode("overwrite")\
        .save()
