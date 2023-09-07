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
        "jXAIarxmRsKCNmKuiGDQW$$xSNUfrf8gREL5gsrZwKbR", 
        "LtJNJ9K2E3T5WSgm96Hxv$$izEyii0Ns2SpwRAqd1aPb"
    )
    df_very_complex_source = very_complex_source(spark)
    df_very_complex_source = collectMetrics(
        spark, 
        df_very_complex_source, 
        "Subgraph_4_1_1", 
        "bGqBYh1gqT_Fnu93L9qwq$$zTwvBzi3nBVPeAOIgvcm1", 
        "M3ibby-kF9lIK7HooHIVH$$4WXs_Wx1tFhFRV__lRFj2"
    )
    df_Reformat_7 = Reformat_7(spark, df_very_complex_source)
    df_Reformat_7 = collectMetrics(
        spark, 
        df_Reformat_7, 
        "Subgraph_4_1_1", 
        "qEJWfnwJR76kSFtIBgZPb$$DFYadIR2wuKEVCoZ4rhZz", 
        "tmsCvLHc2eHashGx13P4N$$fXS4SaNxq7pBrGWMvfzvf"
    )
    df_Reformat_8 = Reformat_8(spark, df_Reformat_7)
    df_Reformat_8 = collectMetrics(
        spark, 
        df_Reformat_8, 
        "Subgraph_4_1_1", 
        "Oh2Ozg_7MfWPR7DekBwSj$$94_24qajQ3DnU9TTc5yp1", 
        "2XD4ffmLGFBRWd5zTVzOK$$-mbfSXy0Hf1XXPRdO-kpS"
    )
    df_Reformat_8.cache().count()
    df_Reformat_8.unpersist()
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_very_complex_source)
    df_FlattenSchema_1 = collectMetrics(
        spark, 
        df_FlattenSchema_1, 
        "Subgraph_4_1_1", 
        "6dinuQB3ZYTAYC-Y1E_G8$$1daD2oxiqUiZjijYINbLU", 
        "QUH1fUY_0ZT8vhQQ1mLxf$$D-lmWbIl9G6IL_Dj_527R"
    )
    df_Subgraph_3_1_1 = Subgraph_3_1_1(spark, config.Subgraph_3_1_1, df_Script_2_1_1)
    df_Reformat_6 = Reformat_6(spark, df_FlattenSchema_1)
    df_Reformat_6 = collectMetrics(
        spark, 
        df_Reformat_6, 
        "Subgraph_4_1_1", 
        "rWP4vorZ-qCbwhDz__E-W$$cAp49QKY0V4LP2QNTMbue", 
        "UAkLGZXizfcO4s-EFj1Sf$$fZdjuU51H9-yk1iBdtdR_"
    )
    df_Reformat_6.cache().count()
    df_Reformat_6.unpersist()
    df_Reformat_2 = Reformat_2(spark, df_Script_2_1_1)
    df_Reformat_2 = collectMetrics(
        spark, 
        df_Reformat_2, 
        "Subgraph_4_1_1", 
        "uO641onqNbuvrG69asLC4$$D-4UiG2a47V4u6lZOwswc", 
        "Uis7YXQybZGwQKxiIeor7$$8khwvFbO4puxjGvhmF9EX"
    )
    df_Reformat_2.cache().count()
    df_Reformat_2.unpersist()

    return df_Subgraph_3_1_1
