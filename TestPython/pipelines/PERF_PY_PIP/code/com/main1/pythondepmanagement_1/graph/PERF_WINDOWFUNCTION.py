from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def PERF_WINDOWFUNCTION(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "cmls_acct_fundg_srce_cd_drvd",
          row_number()\
            .over(Window\
            .partitionBy(col("cmls_3ds_authntn_mthd"))\
            .orderBy(col("cmls_acct_cobrnd_bus_id_drvd").asc(), col("cmls_acct_fundg_srce_cd").desc()))
        )\
        .withColumn("cmls_acct_fundg_srce_cd_drvd", row_number()\
        .over(Window\
        .partitionBy(col("cmls_3ds_authntn_mthd"))\
        .orderBy(col("cmls_acct_cobrnd_bus_id_drvd").asc(), col("cmls_acct_fundg_srce_cd").desc())))
