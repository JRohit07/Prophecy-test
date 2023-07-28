from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def pythonLivySG1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_4_1 = Reformat_4_1(spark, in0)
    df_Reformat_4_1 = collectMetrics(
        spark, 
        df_Reformat_4_1, 
        "pythonLivySG1_1", 
        "vk8HAfMpLwvRZkQLFVW4n$$yHMrzTZ-s5FsU6EFloTBC", 
        "hbeSOsXlkodV9aJRrlENj$$Cocwih1y8JyvBM7sIVB5t"
    )
    df_Filter_1_1 = Filter_1_1(spark, df_Reformat_4_1)
    df_Filter_1_1 = collectMetrics(
        spark, 
        df_Filter_1_1, 
        "pythonLivySG1_1", 
        "q65-a2OHFyIBLXFBeCzgQ$$5WZKWGQP3MWw-uUFaSp7g", 
        "fYQM8YA8APuKcDS_cRpLg$$Vk-CB0WSvE8qZqj2XG-n3"
    )
    df_OrderBy_1_1 = OrderBy_1_1(spark, df_Filter_1_1)
    df_OrderBy_1_1 = collectMetrics(
        spark, 
        df_OrderBy_1_1, 
        "pythonLivySG1_1", 
        "GFIwQtFxtRet0CHKtOY70$$WVvcf-p1YtYub3sCKv-cq", 
        "Fm7hU9737fiGktG5N8mcS$$Om2W1wM17lciQ4yn3R3DW"
    )
    df_Subgraph_2_1 = Subgraph_2_1(spark, config.Subgraph_2_1, df_OrderBy_1_1)

    return df_Subgraph_2_1
