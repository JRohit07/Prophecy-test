from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_4_1_1_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> DataFrame:
    Config.update(config)
    df_Script_2_1_1_1 = Script_2_1_1_1(spark, in0, in1, in2)
    df_Script_2_1_1_1 = collectMetrics(
        spark, 
        df_Script_2_1_1_1, 
        "Subgraph_4_1_1_1", 
        "Sd_e0IMUU42ep0buk6vVD$$aFcT03CTaYO-CTcC4C_5Q", 
        "xJctd_dX0mfp75iCi-ypp$$MalG6WN_5RD7yeVTM-qYS"
    )
    df_Subgraph_3_1_1_1 = Subgraph_3_1_1_1(spark, config.Subgraph_3_1_1_1, df_Script_2_1_1_1)

    return df_Subgraph_3_1_1_1
