from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def catalog(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"qa_database.test_catalog_source")
