from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "c- short",
          row_number()\
            .over(Window\
            .partitionBy(col("`c- short`"), col("`c  - int`"), col("`- c long`"))\
            .orderBy(col("`c_float-__  `").asc(), col("`c -  boolean _  `").asc()))
        )\
        .withColumn("c-string", row_number()\
        .over(Window\
        .partitionBy(col("`c- short`"), col("`c  - int`"), col("`- c long`"))\
        .orderBy(col("`c_float-__  `").asc(), col("`c -  boolean _  `").asc())))
