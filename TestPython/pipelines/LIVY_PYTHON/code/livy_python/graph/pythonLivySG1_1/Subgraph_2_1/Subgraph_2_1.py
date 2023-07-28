from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_2_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_5_1 = Reformat_5_1(spark, in0)
    df_Reformat_5_1 = collectMetrics(
        spark, 
        df_Reformat_5_1, 
        "Subgraph_2_1", 
        "wn70pDd6j7exe249jeyeO$$2yEIe4MCkbQ8DyDzyaeY5", 
        "pMU0n6VsyYZJNHMcVKkVr$$FVO2PqVyacB3GruSu28En"
    )
    df_Subgraph_3_1 = Subgraph_3_1(spark, config.Subgraph_3_1, df_Reformat_5_1)

    return df_Subgraph_3_1
