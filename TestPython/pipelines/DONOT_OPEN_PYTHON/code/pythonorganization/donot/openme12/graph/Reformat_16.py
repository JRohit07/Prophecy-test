from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Reformat_16(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("account_flags"), 
        col("account_open_date"), 
        col("country_code"), 
        col("customer_id"), 
        col("email"), 
        col("first_name"), 
        col("last_name"), 
        col("phone")
    )
