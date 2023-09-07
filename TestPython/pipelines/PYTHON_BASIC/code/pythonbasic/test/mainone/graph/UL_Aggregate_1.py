from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def UL_Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("country_code"))

    return df1.agg(
        first(lookup("TestLookup", col("customer_id"), col("email")).getField("first_name")).alias("c_lookup"), 
        first(col("first_name")).alias("first_name"), 
        first(col("last_name")).alias("last_name"), 
        first(col("phone")).alias("phone"), 
        first(col("account_open_date")).alias("account_open_date"), 
        first(col("account_flags")).alias("account_flags")
    )
