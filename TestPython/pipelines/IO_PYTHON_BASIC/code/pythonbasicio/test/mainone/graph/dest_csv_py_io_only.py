from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasicio.test.mainone.config.ConfigStore import *
from pythonbasicio.test.mainone.udfs.UDFs import *

def dest_csv_py_io_only(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").mode("overwrite").save("dbfs:/tmp/dest_csv_py_disabled")
