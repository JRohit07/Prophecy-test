from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def py_sg_target_test_release(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").mode("overwrite").save("dbfs:/tmp/e2e/py_sg_target_test_release")
