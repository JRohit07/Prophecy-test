from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_13(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c  date`").alias("c  date"), 
        col("`c_timestamp_c   short  --`").alias("c_timestamp_c   short  --"), 
        col("`c_timestamp_c-int-column type`").alias("c_timestamp_c-int-column type"), 
        col("`c_timestamp_-- c-long`").alias("c_timestamp_-- c-long"), 
        col("`c_timestamp_c-decimal renamed`").alias("c_timestamp_c-decimal renamed"), 
        col("`c_timestamp_c  float`").alias("c_timestamp_c  float"), 
        col("`config_values_c   short  --`").alias("config_values_c   short  --"), 
        col("`config_values_c-int-column type`").alias("config_values_c-int-column type"), 
        col("`config_values_-- c-long`").alias("config_values_-- c-long"), 
        col("`config_values_c-decimal renamed`").alias("config_values_c-decimal renamed"), 
        col("`config_values_c  float`").alias("config_values_c  float")
    )
