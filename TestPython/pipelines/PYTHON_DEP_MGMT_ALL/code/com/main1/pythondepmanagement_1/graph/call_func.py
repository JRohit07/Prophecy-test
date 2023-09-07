from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def call_func(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        expr("qa_mask_zip_code(c_string)").alias("c1"), 
        expr("named_struct('a', 'test', 'b', 2, 'c', 3)").alias("c2"), 
        expr(Config.EXPR_COMPLEX_DATES).alias("c4")
    )
