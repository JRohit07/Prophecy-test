from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_7_1_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_OrderBy_4_1_1_1 = OrderBy_4_1_1_1(spark, in0)
    df_OrderBy_4_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_4_1_1_1, 
        "Subgraph_7_1_1_1", 
        "Ekwe16XMcAZiU-B2RlLwJ$$sQmz-K-hzS-4mNwGbHkkc", 
        "BOmBbL6v7bwM1BAAY4HbQ$$Z-VGOb_avcbMPBsqcdItI"
    )
    df_Subgraph_8_1_1_1 = Subgraph_8_1_1_1(spark, config.Subgraph_8_1_1_1, df_OrderBy_4_1_1_1)

    return df_Subgraph_8_1_1_1
