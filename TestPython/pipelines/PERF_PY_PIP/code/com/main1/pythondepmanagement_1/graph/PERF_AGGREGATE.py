from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def PERF_AGGREGATE(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("cmls_acct_ctry_cd_drvd"), col("cmls_acct_fundg_srce_cd_drvd"))

    return df1.agg(
        first(col("cmls_3ds_authntn_mthd")).alias("cmls_3ds_authntn_mthd"), 
        first(col("cmls_acct_cobrnd_bus_id_drvd")).alias("cmls_acct_cobrnd_bus_id_drvd")
    )
