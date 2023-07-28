from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(
        col("cmls_acct_cobrnd_bus_id_drvd"), 
        col("cmls_acct_ctry_cd_drvd"), 
        col("cmls_acct_fundg_srce_cd_drvd"), 
        col("cmls_acct_fundg_srce_cd_enr"), 
        col("cmls_acct_fundg_srce_cd_ri"), 
        col("cmls_acct_fundg_srce_mvisa_cd")
    )

    return df1.agg(first(col("cmls_3ds_authntn_mthd")).alias("cmls_3ds_authntn_mthd"))
