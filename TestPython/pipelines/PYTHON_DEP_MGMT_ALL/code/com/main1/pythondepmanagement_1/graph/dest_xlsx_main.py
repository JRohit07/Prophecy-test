from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def dest_xlsx_main(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("excel")\
        .option("header", True)\
        .option("dataAddress", "A1")\
        .option("usePlainNumberFormat", False)\
        .mode("overwrite")\
        .save("dbfs:/tmp/e2e/python/testxlsx")
