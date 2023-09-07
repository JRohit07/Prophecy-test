from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def Reformat_8(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_tinyint"), 
        col("c_smallint"), 
        col("c_int"), 
        col("c_bigint"), 
        col("c_float"), 
        col("c_double"), 
        col("c_string"), 
        col("c_boolean"), 
        col("c_array"), 
        col("c_struct"), 
        to_date(unix_timestamp(lit("08/26/2016"), "MM/dd/yyyy").cast(TimestampType())).alias("c_date"), 
        unix_timestamp(lit("08/26/2016"), "MM/dd/yyyy").cast(TimestampType()).alias("c_timestamp"), 
        col("c_float").cast(DecimalType(10, 0)).alias("c_decimal"), 
        col("c_tinyint").cast(ShortType()).alias("c_short")
    )
