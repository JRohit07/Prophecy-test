from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def SchemaTransform_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("concat short int", concat(col("`c   short  --`"), col("`c-int-column type`")))\
        .drop("c- - -double")\
        .withColumnRenamed("c-decimal", "c-decimal renamed")
