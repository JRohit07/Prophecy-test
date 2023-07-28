from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def text(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("text")\
        .schema(StructType([StructField("value", StringType(), True)]))\
        .text("dbfs:/Prophecy/qa_data/delimiter/tab/DatasetWithSpaceHyphens", wholetext = False, lineSep = None)
