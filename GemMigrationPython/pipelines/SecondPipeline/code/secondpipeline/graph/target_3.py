from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def target_3(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("jdbc")\
        .option("url", f"jdbc:mysql://3.101.152.38:3306/{Config.JDBC_DATABASE}")\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", f"{Config.JDBC_USER_STRING}")\
        .option("password", f"{Config.JDBC_PASSWORD_STRING}")\
        .option("driver", Config.DRIVER_NAME)\
        .mode("overwrite")\
        .save()
