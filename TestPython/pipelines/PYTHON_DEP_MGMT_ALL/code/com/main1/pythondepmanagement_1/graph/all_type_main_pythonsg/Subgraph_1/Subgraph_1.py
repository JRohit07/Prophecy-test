from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_9 = Reformat_9(spark, in0)
    df_Reformat_9 = collectMetrics(
        spark, 
        df_Reformat_9, 
        "Subgraph_1", 
        "CcAnysfagHsdSZVuF1HHT$$tO_lHbPJcZoiOGhVaz3A1", 
        "BlQeawSgop5tLxjjjo39U$$6xpOJdi0iI3b8x_9u40jl"
    )

    return df_Reformat_9
