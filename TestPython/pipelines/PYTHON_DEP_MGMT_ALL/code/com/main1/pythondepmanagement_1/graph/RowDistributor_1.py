from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def RowDistributor_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame, DataFrame, DataFrame):
    df1 = in0.filter(expr(Config.c_row_distributor))
    df2 = in0.filter(
        (col("`c -  boolean _  `").isin(lit(None), lit(True)) & col("`c_array-string  _ string`")[1].like("%8%"))
    )
    df3 = in0.filter(((col("`c_array -- decimal`")[0] > lit(10)) & col("`c_array-string  _ string`")[1].like("%6%")))
    df4 = in0.filter(expr(Config.c_rowdistributor_complex_expr))

    return df1, df2, df3, df4
