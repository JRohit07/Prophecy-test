from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_9_1_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_10_1_1_1 = Reformat_10_1_1_1(spark, in0)
    df_Reformat_10_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_10_1_1_1, 
        "Subgraph_9_1_1_1", 
        "4J064TlyGZa2l8WYFzyEr$$6XpNqI0DCC7FUptOR40XB", 
        "4ffm2GWJWDJTc40ek2Zbj$$uJBMAfX2J8Q_ZtpyaBV6D"
    )

    return df_Reformat_10_1_1_1
