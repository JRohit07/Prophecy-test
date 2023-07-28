from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def src_parquet_unity_catalog(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/Prophecy/qa_data/parquet/ThreePartitionsDataset.parquet")
