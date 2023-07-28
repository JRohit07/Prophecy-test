from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def OrderBy_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(
        col("`c   short  --`").asc(), 
        col("`c-int-column type`").asc(), 
        col("`-- c-long`").asc(), 
        col("`c-decimal`").asc(), 
        col("`c  float`").asc(), 
        col("`c--boolean`").asc(), 
        col("`c- - -double`").asc(), 
        col("`c___-- string`").asc(), 
        col("`c  date`").asc(), 
        col("c_timestamp").asc()
    )
