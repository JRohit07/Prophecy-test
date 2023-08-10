from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from synapse_pipeline.config.ConfigStore import *
from synapse_pipeline.udfs.UDFs import *

def s3_dataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("sep", ",")\
        .csv("s3://prophecy-dataset-samples/OrdersDatasetInput.csv")
