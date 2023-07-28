from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def SchemaTransform_1_1_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("c_double_c_float", concat(col("c_double"), col("`c_float-__  `")))\
        .drop("c  - int")\
        .withColumnRenamed("c_decimal  -  ", "c_decimal_new")
