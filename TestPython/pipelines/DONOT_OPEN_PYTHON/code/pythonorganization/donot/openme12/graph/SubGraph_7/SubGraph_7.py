from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def SubGraph_7(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_8 = Reformat_8(spark, in0)
    df_Script_4 = Script_4(spark, df_Reformat_8)

    return df_Script_4
