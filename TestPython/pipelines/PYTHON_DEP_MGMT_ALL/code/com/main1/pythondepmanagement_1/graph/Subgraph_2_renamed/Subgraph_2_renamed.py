from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_2_renamed(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_16 = Reformat_16(spark, in0)
    df_Reformat_16 = collectMetrics(
        spark, 
        df_Reformat_16, 
        "Subgraph_2_renamed", 
        "F3H4fdHQS9wWJxODjid6a$$SjwQVFp--tLcTegShv8R6", 
        "gdEKQrTCR9Zue8hgCpFl-$$1_l5LTgJ-27ZQjpS1a_JQ"
    )

    return df_Reformat_16
