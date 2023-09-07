from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def RowDistributor_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame, DataFrame):
    df1 = in0.filter((col("c_tinyint") > lit(-10)))
    df2 = in0.filter((col("c_int") > lit(-10)))
    df3 = in0.filter((col("c_tinyint") > lit(10)))

    return df1, df2, df3
