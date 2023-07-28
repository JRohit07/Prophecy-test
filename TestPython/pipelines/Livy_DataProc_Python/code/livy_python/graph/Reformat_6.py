from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def Reformat_6(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        array(col("year"), col("value"), col("unit")).alias("a1"), 
        array(col("industry_code_ANZSIC"), col("industry_name_ANZSIC")).alias("a2"), 
        array(lit(1), lit(2), col("year").cast(IntegerType())).alias("a3"), 
        struct(
            array(col("year"), col("value"), col("unit")).alias("col1"), 
            array(col("industry_code_ANZSIC"), col("industry_name_ANZSIC")).alias("col2"), 
            col("unit")
          )\
          .alias("s1"), 
        col("year")
    )
