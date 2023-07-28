from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def RowDistributor_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame, DataFrame, DataFrame):
    df1 = in0.filter(
        (
          ((col("`c_struct -- _  `.`c_double - of a struct _`") > lit(20)) | (col("`c_date-for today`") == lit("2005-04-16")))
          & col("`c_array-string  _ string`")[1].like("%7%")
        )
    )
    df2 = in0.filter(
        (col("`c -  boolean _  `").isin(lit(None), lit(True)) & col("`c_array-string  _ string`")[1].like("%8%"))
    )
    df3 = in0.filter(((col("`c_array -- decimal`")[0] > lit(10)) & col("`c_array-string  _ string`")[1].like("%6%")))
    df4 = in0.filter(
        (
          (col("p_string").like("%a%") | col("p_string").rlike("%A%"))
          | ((col("`c_decimal  -  `") == lit(12321)) & col("`c_array-string  _ string`")[0].like("%3%"))
        )
    )

    return df1, df2, df3, df4
