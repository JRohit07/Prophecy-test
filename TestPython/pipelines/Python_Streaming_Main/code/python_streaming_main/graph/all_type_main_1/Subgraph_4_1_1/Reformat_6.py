from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from python_streaming_main.udfs.UDFs import *

def Reformat_6(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c_int.test.value1`").alias("value1"), 
        col("`c_int.test.value1.complex-array1.diabetes`").alias("diabetes"), 
        col("`c_int.test.value1.complex-struct1.diabetes.medication`.medicationsClasses").alias("medicationsClasses")
    )
