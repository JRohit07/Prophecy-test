from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.sg_src.main.udfs.UDFs import *

def Reformat_7(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_struct.`col-1`").alias("nested.field.col1"), 
        expr(
            "named_struct('a', named_struct('test1', named_struct('test- another', 2)), 'b', named_struct('test1', named_struct('test- another', 2)))"
          )\
          .alias("nested.field.col2")
    )
