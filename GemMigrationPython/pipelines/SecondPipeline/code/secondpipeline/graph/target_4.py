from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def target_4(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("jdbc")\
        .option("url", f"{Config.JDBC}{Config.JDBC_DATABASE}")\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", "test_user")\
        .option("password", "admin")\
        .option("driver", "com.mysql.jdbc.Driver")\
        .mode("overwrite")\
        .save()
