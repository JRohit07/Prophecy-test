from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emr_synapse.config.ConfigStore import *
from emr_synapse.udfs.UDFs import *

def mydataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", StringType(), True), StructField("customer_id", StringType(), True), StructField("order_status", StringType(), True), StructField("order_category", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("wasbs://data@prophecydevpublic.blob.core.windows.net/OrdersDatasetInput.csv")
