from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def RemoveSG(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_25 = Reformat_25(spark, in0)
    df_Reformat_25 = collectMetrics(
        spark, 
        df_Reformat_25, 
        "RemoveSG", 
        "ZjSNg4OSqUN5bI5K7FJZ4$$r0EkOAhs1AsFZr74SjpLy", 
        "_-ioMshiuoxuFfXovm25x$$sYuWmrRZFVrgl9UqK3QQQ"
    )

    if Config.c_int_11 < 0:
        df_Limit_2 = Limit_2(spark, df_Reformat_25)
        df_Limit_2 = collectMetrics(
            spark, 
            df_Limit_2, 
            "RemoveSG", 
            "R8tUH9mvtsmhpDskv_GZb$$56xoSbT0kGAyaPiSt2Wgp", 
            "-ab5siDZ9vN_lh8iy94fx$$sxS4NPn2YBH3h3HKK0Vzh"
        )
        df_Filter_8 = Filter_8(spark, df_Limit_2)
        df_Filter_8 = collectMetrics(
            spark, 
            df_Filter_8, 
            "RemoveSG", 
            "ufADOedu6N4rmyt_V_WgH$$I-4usQkSXDgCLTZ5DTCrm", 
            "N2GsyFDPjbjtvAF5tSEyV$$6QFyxLLGCQu6hdEXwKtiD"
        )
    else:
        df_Filter_8 = None

    if (Config.c_int_11 < 0):
        df_Reformat_26 = Reformat_26(spark, in0)
        df_Reformat_26 = collectMetrics(
            spark, 
            df_Reformat_26, 
            "RemoveSG", 
            "ZmDToDj-g2TBEQPKvixGK$$LjXzCPvJRm-KIsdR8nCH-", 
            "0KeAj1wh6yd_er5TmQK1G$$XCfjOg2-T2nddhdDeNOoW"
        )
    else:
        df_Reformat_26 = in0

    df_Limit_3 = Limit_3(spark, df_Reformat_26)
    df_Limit_3 = collectMetrics(
        spark, 
        df_Limit_3, 
        "RemoveSG", 
        "uBVKsaT3jAfLWtmezV2LX$$Yu1ooRZFanReC3yrMGhK3", 
        "HNanhDkqvhmHG7NH8EHMO$$Jqo_BGaF_-pR3n7_qhWCh"
    )
    df_Script_13 = Script_13(spark, df_Limit_3)
    df_Script_13 = collectMetrics(
        spark, 
        df_Script_13, 
        "RemoveSG", 
        "mqU6DM4WsBFs7b1hkA0NN$$_ejLzZzD7mbvxcqxv8c3M", 
        "XuR4IjmpnEopS869Z3z4W$$ISQaqAr7nx5RpCS2BbE5T"
    )
    df_Script_13.cache().count()
    df_Script_13.unpersist()

    return df_Filter_8
