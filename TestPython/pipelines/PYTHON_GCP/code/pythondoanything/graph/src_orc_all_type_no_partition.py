from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def src_orc_all_type_no_partition(spark: SparkSession) -> DataFrame:
    return spark.read.format("orc").load("dbfs:/Prophecy/qa_data/orc/all_type_no_partition")
