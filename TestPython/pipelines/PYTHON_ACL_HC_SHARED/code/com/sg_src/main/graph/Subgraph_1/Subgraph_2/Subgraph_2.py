from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_2(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_10 = Reformat_10(spark, in0)
    df_Reformat_10 = collectMetrics(
        spark, 
        df_Reformat_10, 
        "Subgraph_2", 
        "dG4kmJA_V_a0IfHgYimU4$$rP42N2RfemcQL2St6dYlZ", 
        "ySTQPzgScPJp8BbRna5N-$$GExrxR7oz_S7fqne43KNs"
    )

    return df_Reformat_10
