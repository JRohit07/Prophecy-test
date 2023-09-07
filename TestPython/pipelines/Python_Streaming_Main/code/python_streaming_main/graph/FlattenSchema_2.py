from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def FlattenSchema_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.columns
    selectCols = [col("amount") if "amount" in flt_col else col("value.amount").alias("amount"),                   col("customer_id") if "customer_id" in flt_col else col("value.customer_id").alias("customer_id"),                   col("order_category") if "order_category" in flt_col else col("value.order_category").alias("order_category"),                   col("order_date") if "order_date" in flt_col else col("value.order_date").alias("order_date"),                   col("order_id") if "order_id" in flt_col else col("value.order_id").alias("order_id"),                   col("order_status") if "order_status" in flt_col else col("value.order_status").alias("order_status"),                   col("timestamp") if "timestamp" in flt_col else col("timestamp")]

    return in0.select(*selectCols)
