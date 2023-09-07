from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def UL_Reformat_4(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        lookup("TestLookup", col("customer_id"), col("email")).getField("first_name").alias("c_lookup_first_name"), 
        lookup("TestLookup", col("customer_id"), col("email")).getField("last_name").alias("c_lookup_last_name"), 
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        col("email"), 
        col("country_code"), 
        col("account_open_date"), 
        col("account_flags"), 
        col("customer_id").contains(lit("1")).alias("c_contains"), 
        (
          (col("first_name").contains(col("last_name")) | col("first_name").endswith(col("last_name")))
          | col("first_name").startswith(col("last_name"))
        )\
          .alias(
          "c_contains_starts_ends"
        )
    )
