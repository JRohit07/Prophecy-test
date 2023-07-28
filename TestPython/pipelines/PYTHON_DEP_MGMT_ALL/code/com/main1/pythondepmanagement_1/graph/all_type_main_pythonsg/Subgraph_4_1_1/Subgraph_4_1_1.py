from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_4_1_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> DataFrame:
    Config.update(config)
    df_Script_2_1_1 = Script_2_1_1(spark, in0, in1, in2)
    df_Script_2_1_1 = collectMetrics(
        spark, 
        df_Script_2_1_1, 
        "Subgraph_4_1_1", 
        "jXAIarxmRsKCNmKuiGDQW$$PTwrvN7JP44hstMojqHr0", 
        "LtJNJ9K2E3T5WSgm96Hxv$$q9qObYoorGVekbmcqaNgB"
    )
    df_very_complex_source = very_complex_source(spark)
    df_very_complex_source = collectMetrics(
        spark, 
        df_very_complex_source, 
        "Subgraph_4_1_1", 
        "bGqBYh1gqT_Fnu93L9qwq$$WEAAty96GfYlMe1jacNjU", 
        "M3ibby-kF9lIK7HooHIVH$$yruiIsLkjIpBn8MH94ypA"
    )
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_very_complex_source)
    df_FlattenSchema_1 = collectMetrics(
        spark, 
        df_FlattenSchema_1, 
        "Subgraph_4_1_1", 
        "6dinuQB3ZYTAYC-Y1E_G8$$9IFYD6bbJMoxXvyHcBOkE", 
        "QUH1fUY_0ZT8vhQQ1mLxf$$FXSL9TOF_fnp1aAbExQhX"
    )
    df_Reformat_6 = Reformat_6(spark, df_FlattenSchema_1)
    df_Reformat_6 = collectMetrics(
        spark, 
        df_Reformat_6, 
        "Subgraph_4_1_1", 
        "rWP4vorZ-qCbwhDz__E-W$$s06jHY1gxjidXtGEBFyI3", 
        "UAkLGZXizfcO4s-EFj1Sf$$mnw42N-dP6ReZM6hTllZn"
    )
    df_Reformat_6.cache().count()
    df_Reformat_6.unpersist()
    df_Subgraph_3_1_1 = Subgraph_3_1_1(spark, config.Subgraph_3_1_1, df_Script_2_1_1)
    df_Reformat_2 = Reformat_2(spark, df_Script_2_1_1)
    df_Reformat_2 = collectMetrics(
        spark, 
        df_Reformat_2, 
        "Subgraph_4_1_1", 
        "uO641onqNbuvrG69asLC4$$4-nqDLwvHFxea_doDf_G1", 
        "Uis7YXQybZGwQKxiIeor7$$AWN05_sCX5008KMd-Uxxj"
    )
    df_Reformat_2.cache().count()
    df_Reformat_2.unpersist()
    df_Reformat_7 = Reformat_7(spark, df_very_complex_source)
    df_Reformat_7 = collectMetrics(
        spark, 
        df_Reformat_7, 
        "Subgraph_4_1_1", 
        "qEJWfnwJR76kSFtIBgZPb$$JRThCkmH4xraX9dwUcmnx", 
        "tmsCvLHc2eHashGx13P4N$$jhqubAjlmfnGMJc2HSD15"
    )
    df_Reformat_8 = Reformat_8(spark, df_Reformat_7)
    df_Reformat_8 = collectMetrics(
        spark, 
        df_Reformat_8, 
        "Subgraph_4_1_1", 
        "Oh2Ozg_7MfWPR7DekBwSj$$okHm9R91srVZfmtZZt9sZ", 
        "2XD4ffmLGFBRWd5zTVzOK$$YsrKInv8a4bpf8xqcFjn_"
    )
    df_Reformat_8.cache().count()
    df_Reformat_8.unpersist()

    return df_Subgraph_3_1_1
