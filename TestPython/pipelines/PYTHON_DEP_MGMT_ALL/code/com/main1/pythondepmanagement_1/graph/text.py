from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def text(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("text")\
        .schema(StructType([StructField("value", StringType(), True)]))\
        .text("dbfs:/Prophecy/qa_data/delimiter/tab/DatasetWithSpaceHyphens", wholetext = False, lineSep = None)
