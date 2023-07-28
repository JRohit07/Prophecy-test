from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from perf_unitest_generate.config.ConfigStore import *
from perf_unitest_generate.udfs.UDFs import *

def RowDistributor_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    df1 = in0.filter(col("email").like("%a%"))
    df2 = in0.filter(col("first_name").like("%a%"))

    return df1, df2
