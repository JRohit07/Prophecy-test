from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline.config.ConfigStore import *
from pipeline.udfs.UDFs import *

def test_uc_seed_1(spark: SparkSession) -> DataFrame:
    return spark.read.table("`main`.`qa_database`.`test_uc_seed_1`")
