from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_1_1 = Reformat_1_1(spark, in0)
    df_Join_1_2 = Join_1_2(spark, df_Reformat_1_1, df_Reformat_1_1)

    return df_Join_1_2
