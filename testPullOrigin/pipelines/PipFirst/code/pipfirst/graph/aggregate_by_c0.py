from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipfirst.config.ConfigStore import *
from pipfirst.functions import *

def aggregate_by_c0(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("_c0"))

    return df1.agg(first(col("_c0")).alias("_c0"))
