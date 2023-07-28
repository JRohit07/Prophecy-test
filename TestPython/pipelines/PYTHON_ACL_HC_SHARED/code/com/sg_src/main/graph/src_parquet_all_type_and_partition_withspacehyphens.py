from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from com.sg_src.main.config.ConfigStore import *
from com.sg_src.main.udfs.UDFs import *

def src_parquet_all_type_and_partition_withspacehyphens(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/Prophecy/qa_data/parquet/all_type_and_partition_withspacehyphens")
