from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def SubGraph_7(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_8 = Reformat_8(spark, in0)
    df_Reformat_8 = collectMetrics(
        spark, 
        df_Reformat_8, 
        "SubGraph_7", 
        "ZEY3gafK1VkNqpgbPwW2X$$5mgoHwsKLyaA9V1Hmj45S", 
        "rsfeFdbRoZoIorpsJ7a5K$$5ZjURBrwlP_Z0T5UwSmET"
    )
    df_Script_9 = Script_9(spark, df_Reformat_8)
    df_Script_9 = collectMetrics(
        spark, 
        df_Script_9, 
        "SubGraph_7", 
        "xy9u1yRheK2LmdUyIUlMq$$Kc0KrrpX78XdufkNGAIuZ", 
        "X_hexzbsx5Jh0govk82w-$$N_ZR4u8ankr112Exdn1gw"
    )

    return df_Script_9
