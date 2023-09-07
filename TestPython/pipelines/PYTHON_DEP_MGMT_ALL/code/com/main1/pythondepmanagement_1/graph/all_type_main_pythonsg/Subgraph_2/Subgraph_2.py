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
        "dG4kmJA_V_a0IfHgYimU4$$ayQhQiwi1UMj1NqyEAhOJ", 
        "ySTQPzgScPJp8BbRna5N-$$gyQ1Fg44lPByGzCaKCRE_"
    )

    return df_Reformat_10
