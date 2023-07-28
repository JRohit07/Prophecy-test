from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_7(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("customer_id").cast(ShortType()).alias("c_short1"), 
        col("customer_id").cast(IntegerType()).alias("c_int1"), 
        col("customer_id").cast(ShortType()).alias("c_short2"), 
        col("customer_id").cast(IntegerType()).alias("c_int2")
    )
