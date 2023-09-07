from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from python_one_gem_only.config.ConfigStore import *
from python_one_gem_only.udfs.UDFs import *

def src_parquet_all_type_no_partition(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/Prophecy/qa_data/parquet/all_type_no_partition")
