from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.withColumn("c_array", explode_outer("c_array")).columns
    selectCols = [col("c_array") if "c_array" in flt_col else col("c_array"),                   col("c_struct") if "c_struct" in flt_col else col("c_struct")]

    return in0.withColumn("c_array", explode_outer("c_array")).select(*selectCols)
