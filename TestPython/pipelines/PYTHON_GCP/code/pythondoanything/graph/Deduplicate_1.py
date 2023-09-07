from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def Deduplicate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "row_number",
          row_number()\
            .over(Window\
            .partitionBy("c -  boolean _  ", "c-string")\
            .orderBy(concat(lit(Config.c_repartition_colname), col("`c  - int`")).asc(), lit(Config.c_expr_schematransform).desc()))
        )\
        .filter(col("row_number") == lit(1))\
        .drop("row_number")
