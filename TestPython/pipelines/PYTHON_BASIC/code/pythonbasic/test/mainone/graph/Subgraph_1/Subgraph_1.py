from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_UL_Reformat_4_1 = UL_Reformat_4_1(spark, in0)
    df_UL_Join_1_1 = UL_Join_1_1(spark, df_UL_Reformat_4_1, df_UL_Reformat_4_1)
    df_UL_OrderBy_1_1 = UL_OrderBy_1_1(spark, df_UL_Join_1_1)

    return df_UL_OrderBy_1_1
