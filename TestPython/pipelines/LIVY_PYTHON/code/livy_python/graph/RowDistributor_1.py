from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def RowDistributor_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    df1 = in0.filter(col("year").like(Config.c_expr))
    df2 = in0.filter(col("rme_size_grp").like("%b%"))

    return df1, df2
