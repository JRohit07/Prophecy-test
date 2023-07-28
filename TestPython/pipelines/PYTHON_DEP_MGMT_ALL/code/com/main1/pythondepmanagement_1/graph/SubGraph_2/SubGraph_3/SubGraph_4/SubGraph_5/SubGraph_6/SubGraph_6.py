from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def SubGraph_6(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_3 = Reformat_3(spark, in0)
    df_Reformat_3 = collectMetrics(
        spark, 
        df_Reformat_3, 
        "SubGraph_6", 
        "EU2w5Q7DT5q_Ezrvvk9vm$$FsHwRBFt_Fcnw3nQVpqLg", 
        "OJSgtPcLdvZAYK_boMALe$$uHKWp3ta9CaGh4-_D8Ijx"
    )

    return df_Reformat_3
