from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from livy_python.udfs.UDFs import *

def Filter_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(~ col("year").like("%45345%"))
