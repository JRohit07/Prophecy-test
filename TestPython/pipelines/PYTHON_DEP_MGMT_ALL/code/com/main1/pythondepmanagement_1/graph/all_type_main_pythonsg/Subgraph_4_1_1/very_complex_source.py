from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def very_complex_source(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/Prophecy/qa_data/parquet/verycomplexdata.parquet")
