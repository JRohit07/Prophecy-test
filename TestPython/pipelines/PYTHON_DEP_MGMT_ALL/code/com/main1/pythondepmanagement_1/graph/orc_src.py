from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def orc_src(spark: SparkSession) -> DataFrame:
    return spark.read.format("orc").load("dbfs:/Prophecy/qa_data/orc/all_type_no_partition")
