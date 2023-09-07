from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_4_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("customer_id"), 
        when(col("first_name").like("%a%"), lit("amar"))\
          .when(col("first_name").like("%b%"), lit("abhiimanyu"))\
          .otherwise(col("first_name"))\
          .alias("first_name"), 
        lit("last").alias("last_name"), 
        lit("invalid").alias("country_code"), 
        col("account_open_date"), 
        col("account_flags"), 
        col("email"), 
        col("phone")
    )
