from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def PassThrough(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("c1").asc(), col("c2").asc(), col("c3").asc(), col("c4").asc(), col("c6").asc())
