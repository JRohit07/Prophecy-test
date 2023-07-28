from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_7_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_OrderBy_4_1_1 = OrderBy_4_1_1(spark, in0)
    df_OrderBy_4_1_1 = collectMetrics(
        spark, 
        df_OrderBy_4_1_1, 
        "Subgraph_7_1_1", 
        "gVKMNC9dxiWr34PMCTYhQ$$gJqxI7EqBPIe_8_4eajDO", 
        "bvGbcYH7KE2BGIgZcjfzI$$ZIoK48PGauAfJPeXWsEKv"
    )
    df_Subgraph_8_1_1 = Subgraph_8_1_1(spark, config.Subgraph_8_1_1, df_OrderBy_4_1_1)
    df_Reformat_3 = Reformat_3(spark, df_OrderBy_4_1_1)
    df_Reformat_3 = collectMetrics(
        spark, 
        df_Reformat_3, 
        "Subgraph_7_1_1", 
        "kaz90rZgoco30TfvRAidJ$$h2TCGP7m-X8kzg2aKbYB8", 
        "oniBrVyglowifQ03iujZZ$$m5s5lQS_iBVns9HmYeVhb"
    )
    df_Reformat_3.cache().count()
    df_Reformat_3.unpersist()

    return df_Subgraph_8_1_1
