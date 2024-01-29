from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def source_5(spark: SparkSession) -> DataFrame:
    import os

    return spark.read\
        .format("jdbc")\
        .option("url", "jdbc:mysql://3.101.152.38:3306/test_database")\
        .option("user", "test_user")\
        .option("password", "admin")\
        .option("dbtable", "test_table_automation")\
        .option("pushDownPredicate", True)\
        .option("driver", "com.mysql.jdbc.Driver")\
        .load()
