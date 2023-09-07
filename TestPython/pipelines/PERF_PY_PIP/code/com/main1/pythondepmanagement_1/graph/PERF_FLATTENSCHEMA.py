from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def PERF_FLATTENSCHEMA(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.columns
    selectCols = [col("cmls_3ds_authntn_mthd") if "cmls_3ds_authntn_mthd" in flt_col else col("cmls_3ds_authntn_mthd")]

    return in0.select(*selectCols)
