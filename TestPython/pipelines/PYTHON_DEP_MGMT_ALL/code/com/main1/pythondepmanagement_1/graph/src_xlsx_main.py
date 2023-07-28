from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def src_xlsx_main(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("excel")\
        .option("header", True)\
        .option("dataAddress", "'Sheet1'!B1:G20")\
        .load("dbfs:/Prophecy/qa_data/xlsx/office_supply_sales/office_supply_sales.xlsx")
