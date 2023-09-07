from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "cmls_acct_fundg_srce_cd_drvd",
          row_number()\
            .over(Window.partitionBy(col("cmls_acct_cobrnd_bus_id_drvd")).orderBy(col("cmls_acct_cobrnd_bus_id_drvd").desc()))
        )\
        .withColumn("cmls_acct_fundg_srce_cd_enr", row_number()\
        .over(Window.partitionBy(col("cmls_acct_cobrnd_bus_id_drvd")).orderBy(col("cmls_acct_cobrnd_bus_id_drvd").desc())))
