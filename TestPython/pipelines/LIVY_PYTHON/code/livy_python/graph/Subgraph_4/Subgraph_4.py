from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_4(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_4_1 = Reformat_4_1(spark, in0)
    df_Reformat_4_1 = collectMetrics(
        spark, 
        df_Reformat_4_1, 
        "Subgraph_4", 
        "vk8HAfMpLwvRZkQLFVW4n$$LcWCMz19kwxrx1vR0ABZN", 
        "hbeSOsXlkodV9aJRrlENj$$xKBZUmYEKITs8wPYAcnXE"
    )
    df_Filter_1_1 = Filter_1_1(spark, df_Reformat_4_1)
    df_Filter_1_1 = collectMetrics(
        spark, 
        df_Filter_1_1, 
        "Subgraph_4", 
        "q65-a2OHFyIBLXFBeCzgQ$$PiaHAM-u7dM-p1qYzZAe8", 
        "fYQM8YA8APuKcDS_cRpLg$$7zhAuqRsX79rKrCT2vIYd"
    )
    df_OrderBy_1_1 = OrderBy_1_1(spark, df_Filter_1_1)
    df_OrderBy_1_1 = collectMetrics(
        spark, 
        df_OrderBy_1_1, 
        "Subgraph_4", 
        "GFIwQtFxtRet0CHKtOY70$$XhPn9Tzyc11xMQKI0wheo", 
        "Fm7hU9737fiGktG5N8mcS$$0fekEU5VtdEXATBBKSvxR"
    )
    df_Subgraph_2_1 = Subgraph_2_1(spark, config.Subgraph_2_1, df_OrderBy_1_1)

    return df_Subgraph_2_1
