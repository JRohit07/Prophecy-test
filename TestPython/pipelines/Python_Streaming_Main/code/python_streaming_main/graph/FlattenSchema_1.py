from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.withColumn("c_array", explode_outer("c_array")).columns
    selectCols = [col("c_array") if "c_array" in flt_col else col("c_array"),                   col("c_struct") if "c_struct" in flt_col else col("c_struct"),                   col("p_int") if "p_int" in flt_col else col("p_int"),                   col("p_float") if "p_float" in flt_col else col("p_float"),                   col("p_string") if "p_string" in flt_col else col("p_string")]

    return in0.withColumn("c_array", explode_outer("c_array")).select(*selectCols)
