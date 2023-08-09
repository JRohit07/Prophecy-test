from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from emr_synapse.config.ConfigStore import *
from emr_synapse.udfs.UDFs import *

def Limit_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(10)
