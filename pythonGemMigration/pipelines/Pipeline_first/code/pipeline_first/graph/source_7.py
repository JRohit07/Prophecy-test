from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_7(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("jdbc")\
        .option("url", f"jdbc:mysql://3.101.152.38:3306/{Config.JDBC_DATABASE}")\
        .option("user", "{}".format(f"{Config.TEST}_{Config.USER}"))\
        .option("password", "{}".format(f"{Config.ADM}{Config.IN}"))\
        .option("dbtable", f"{Config.TEST}_table_automation")\
        .option("pushDownPredicate", True)\
        .option("driver", Config.DRIVER_NAME)\
        .load()
