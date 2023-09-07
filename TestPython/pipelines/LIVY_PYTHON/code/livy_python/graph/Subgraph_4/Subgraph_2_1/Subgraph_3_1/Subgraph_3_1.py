from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_3_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_6_1 = Reformat_6_1(spark, in0)
    df_Reformat_6_1 = collectMetrics(
        spark, 
        df_Reformat_6_1, 
        "Subgraph_3_1", 
        "1xLXn460ujreIMutMC-0m$$tyFTqWMQe91mVY_jB1Icf", 
        "kpOriftOdJJGBQ_slHfYM$$D4gDuR4AYuT1NtZJO8wQ1"
    )

    return df_Reformat_6_1
