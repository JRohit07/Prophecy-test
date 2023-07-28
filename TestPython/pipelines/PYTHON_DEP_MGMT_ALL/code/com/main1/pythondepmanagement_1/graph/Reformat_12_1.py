from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_12_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_short"), 
        col("c_int"), 
        col("c_long"), 
        col("c_decimal"), 
        col("c_float"), 
        col("c_boolean"), 
        col("c_double"), 
        col("c_string"), 
        col("c_date"), 
        col("c_timestamp"), 
        col("c_array_int"), 
        col("c_array_string"), 
        col("c_array_long"), 
        col("c_array_boolean"), 
        col("c_array_date"), 
        col("c_array_timestamp"), 
        col("c_array_float"), 
        col("c_array_decimal"), 
        col("c_struct"), 
        monotonically_increasing_id().alias("c_increasing")
    )
