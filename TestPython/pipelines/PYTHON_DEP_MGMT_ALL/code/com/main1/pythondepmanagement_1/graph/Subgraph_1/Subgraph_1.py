from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> DataFrame:
    Config.update(config)
    df_Reformat_2_1_1_1 = Reformat_2_1_1_1(spark, in0)
    df_Reformat_2_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_2_1_1_1, 
        "Subgraph_1", 
        "HRxFdBYuSsb2We7BpvsJC$$DfKpfW8QvJd_BTki4Z63g", 
        "NqmCw2zv-S6BcWFElBWq_$$Ffuv220Xl9VMotBXNiRSA"
    )
    df_Reformat_8_1_1_1 = Reformat_8_1_1_1(spark, in1)
    df_Reformat_8_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_8_1_1_1, 
        "Subgraph_1", 
        "Bxa4OeQuBkGHlIPdUJFUw$$Lodniijalv7nESCos-yF1", 
        "aaCZLJFzohqVSL-xUMQHo$$x5avKFrhJuos2UMbItBb_"
    )
    df_Source_1_1_1_1 = Source_1_1_1_1(spark)
    df_Source_1_1_1_1 = collectMetrics(
        spark, 
        df_Source_1_1_1_1, 
        "Subgraph_1", 
        "bObmBIQtxyylF6jj-eOQf$$i-ZLiuLk057n9vYRWEdTp", 
        "2GKnm-ic_0revwDoKFRqh$$KCmjGYSRUsHOGq03YgqA8"
    )
    df_Reformat_1_1_1_1 = Reformat_1_1_1_1(spark, df_Source_1_1_1_1)
    df_Reformat_1_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_1_1_1_1, 
        "Subgraph_1", 
        "DRzOUN7AkOrwQ_B_NvT7O$$H8YMuj7eXf4FxlXfV6J09", 
        "K0ADT_Hvs8NavVMBh0cfg$$Jujxr7kbkDRcyE3_Mq2ar"
    )
    df_Join_1_1_1 = Join_1_1_1(spark, df_Reformat_1_1_1_1, df_Reformat_2_1_1_1)
    df_Join_1_1_1 = collectMetrics(
        spark, 
        df_Join_1_1_1, 
        "Subgraph_1", 
        "tZ2qapOM4ZhMeVoaEYJzM$$LmOHeslXqOxzVi6sJw_Ua", 
        "RA9ju_6DMYf9NcgOs0VAD$$XuAmqIWWcj7TX5_SSlTjl"
    )

    if (Config.config_int_here != - 1001):
        df_PassMe = PassMe(spark, df_Join_1_1_1)
        df_PassMe = collectMetrics(
            spark, 
            df_PassMe, 
            "Subgraph_1", 
            "kIOfy0qVS5a7QBsOQ7VBa$$Z7tE-IIC3p-34eqKMi1Df", 
            "BDkk_Nepqp3a-0AM8sR6V$$vg-O7VwMcJJWgmdC21c3j"
        )
    else:
        df_PassMe = df_Join_1_1_1

    if Config.config_int_here == - 1001:

        if (Config.config_int_here == - 1001):
            df_Limit_1_1_1_1 = Limit_1_1_1_1(spark, df_Join_1_1_1)
            df_Limit_1_1_1_1 = collectMetrics(
                spark, 
                df_Limit_1_1_1_1, 
                "Subgraph_1", 
                "p1N-RK514WNhfFKwxyULx$$OMjX9EBT1cYGr-1sj0DpY", 
                "LAPQJxikt0Kq8vNqyXiDV$$9y8dIPk_OfUJPo_4I3NTo"
            )
        else:
            df_Limit_1_1_1_1 = df_Join_1_1_1

        df_Filter_1_1_1_1 = Filter_1_1_1_1(spark, df_Limit_1_1_1_1)
        df_Filter_1_1_1_1 = collectMetrics(
            spark, 
            df_Filter_1_1_1_1, 
            "Subgraph_1", 
            "6CUAHPQg9r7HOhdHJ0dkS$$3zMZmtKLiehCKgOIp2kXH", 
            "HPj67q3WiAXV30KVL3vk_$$Dxy5aHxQJX9HIlFY5g9lo"
        )
        df_OrderBy_1_1_1_1 = OrderBy_1_1_1_1(spark, df_Filter_1_1_1_1)
        df_OrderBy_1_1_1_1 = collectMetrics(
            spark, 
            df_OrderBy_1_1_1_1, 
            "Subgraph_1", 
            "MhGhnzgIKxq0gYRLDUHdp$$tnUEckjhcYWycAhUlCFQb", 
            "OFMzXXYMEBk_SX4iZh_yQ$$YiIKFXZ7NM-4XiWeBpUaI"
        )
        df_Aggregate_1_1_1_1 = Aggregate_1_1_1_1(spark, df_OrderBy_1_1_1_1)
        df_Aggregate_1_1_1_1 = collectMetrics(
            spark, 
            df_Aggregate_1_1_1_1, 
            "Subgraph_1", 
            "ytb3uwtD43qXi6-kPYMYv$$KPxswWjFBuFw-dy9_qlRi", 
            "MN_NB6mkCiKxUT5vfZan3$$XFm62zM2TOQSrwT9mAlLN"
        )
        df_SchemaTransform_1_1_1_1 = SchemaTransform_1_1_1_1(spark, df_Aggregate_1_1_1_1)
        df_SchemaTransform_1_1_1_1 = collectMetrics(
            spark, 
            df_SchemaTransform_1_1_1_1, 
            "Subgraph_1", 
            "crAmp_6Z-pcdL82MgVOdq$$EkjiVUoGCfxArt1VyOt5k", 
            "WlnqlexL6tKNmTblipspl$$L3CTsUlRvBCGGZitb5OJT"
        )
        df_Deduplicate_2_1_1_1 = Deduplicate_2_1_1_1(spark, df_SchemaTransform_1_1_1_1)
        df_Deduplicate_2_1_1_1 = collectMetrics(
            spark, 
            df_Deduplicate_2_1_1_1, 
            "Subgraph_1", 
            "l6iOK2oM1m17AzAYh5-xI$$AZwYUHXIIDgCWp9BF0K8k", 
            "jTMLW77iU3ZTMKSNMkOtM$$TsOJEEgSeFKK1hWbbSIpy"
        )
    else:
        df_Deduplicate_2_1_1_1 = None

    if Config.config_int_here == - 1001:
        df_Repartition_1_1_1_1 = Repartition_1_1_1_1(spark, df_Limit_1_1_1_1)
        df_Repartition_1_1_1_1 = collectMetrics(
            spark, 
            df_Repartition_1_1_1_1, 
            "Subgraph_1", 
            "MteBSbsq-Ner5He5FelKp$$946_75iIOcype38HUqIt6", 
            "E4BOgXz6GF5RgZwc16Rwm$$ir_oX7kHygERIql0b1da7"
        )
        df_RowDistributor_1_1_1_1_out0, df_RowDistributor_1_1_1_1_out1 = RowDistributor_1_1_1_1(
            spark, 
            df_Repartition_1_1_1_1
        )
        df_RowDistributor_1_1_1_1_out0 = collectMetrics(
            spark, 
            df_RowDistributor_1_1_1_1_out0, 
            "Subgraph_1", 
            "XTWcjSG_z1VN-ioS11SMM$$6P6iUNLgrmm5V1MEPFPM5", 
            "8jdN-HIJzECqc8w6ZHvsE$$nmJIquDxfKuXUHDLMviOM"
        )
        df_RowDistributor_1_1_1_1_out1 = collectMetrics(
            spark, 
            df_RowDistributor_1_1_1_1_out1, 
            "Subgraph_1", 
            "XTWcjSG_z1VN-ioS11SMM$$6P6iUNLgrmm5V1MEPFPM5", 
            "LEV126CPB417qxdJVx8yj$$RWqTq2QTD2vc4e05pWtRK"
        )
    else:
        df_RowDistributor_1_1_1_1_out0, df_RowDistributor_1_1_1_1_out1 = None, None

    if Config.config_int_here == - 1001:
        df_Deduplicate_1_1_1_1 = Deduplicate_1_1_1_1(spark, df_SchemaTransform_1_1_1_1)
        df_Deduplicate_1_1_1_1 = collectMetrics(
            spark, 
            df_Deduplicate_1_1_1_1, 
            "Subgraph_1", 
            "PEI-m4zTWUCFCmXVJnUZs$$zF1mjwd1xRInCE4Dbm17U", 
            "cy9q-xVl9y7VW2fplofDX$$He-54lpME0RBOjlh6jCt2"
        )
    else:
        df_Deduplicate_1_1_1_1 = None

    df_Limit_2 = Limit_2(spark, df_PassMe)
    df_Limit_2 = collectMetrics(
        spark, 
        df_Limit_2, 
        "Subgraph_1", 
        "81FzEK0YFhki6xbidMpaV$$qV44CtYzuNBLd5_IUduT9", 
        "omPN3G4I1A_GVOsrIrT0i$$8YpWRRhheyAwXMCvzrv7g"
    )
    df_Limit_2.cache().count()
    df_Limit_2.unpersist()

    if Config.config_int_here != - 1001:
        df_RemoveMe = RemoveMe(spark, df_Join_1_1_1)
        df_RemoveMe = collectMetrics(
            spark, 
            df_RemoveMe, 
            "Subgraph_1", 
            "L8LGKp9uq2yd9evGFwsk1$$rFR3hh3fJTB4Ik_DHTyvJ", 
            "VE-8w1wtj2dI_l_DQwv2l$$lthxuc4o8bRRgxagMvvGv"
        )
        df_OrderBy_3 = OrderBy_3(spark, df_RemoveMe)
        df_OrderBy_3 = collectMetrics(
            spark, 
            df_OrderBy_3, 
            "Subgraph_1", 
            "rYSngJBbKDrr0f6szHAxD$$TWRa2vb2XbuxWCjZYCyxY", 
            "D66W9KoLutFg7zcJQ66Bp$$k_tCZ6Yf1_B8s2ZYFiMdm"
        )
        df_OrderBy_3.cache().count()
        df_OrderBy_3.unpersist()
    else:
        df_OrderBy_3 = None

    if ((Config.config_int_here == - 1001) or (Config.config_int_here == - 1001)):
        df_SetOperation_1_1_1_1 = SetOperation_1_1_1_1(spark, df_Deduplicate_1_1_1_1, df_Deduplicate_2_1_1_1)
        df_SetOperation_1_1_1_1 = collectMetrics(
            spark, 
            df_SetOperation_1_1_1_1, 
            "Subgraph_1", 
            "vcDN1yRcCO4w3u_ozLdCP$$3N8Iqfx0Mf88oKau4-ALN", 
            "ktkdcJ3pPqF6OK2x9jVMM$$fz_T8H23o6o2YT4ibygm0"
        )
        df_WindowFunction_1_1_1_1 = WindowFunction_1_1_1_1(spark, df_SetOperation_1_1_1_1)
        df_WindowFunction_1_1_1_1 = collectMetrics(
            spark, 
            df_WindowFunction_1_1_1_1, 
            "Subgraph_1", 
            "ikPUbf5N7H9jvQG_pAOxg$$8hO1Bd5WjH5bH6qvASL3K", 
            "GL0FAz1I6-IXu19pLNI5j$$fVTmeTtgfqgbHht1bBQug"
        )
        df_Script_1_1_1_1 = Script_1_1_1_1(spark, df_WindowFunction_1_1_1_1)
        df_Script_1_1_1_1 = collectMetrics(
            spark, 
            df_Script_1_1_1_1, 
            "Subgraph_1", 
            "_goKoPl_d_h-zlzeHbbXO$$n9ZWj0mvaKqlvNB4j-8Vt", 
            "FuY-25pnL_i_2W0YcitKx$$LkJs_XLtt4QDFL5qrBMpa"
        )
    else:
        df_Script_1_1_1_1 = None

    df_OrderBy_3_1_1_1 = OrderBy_3_1_1_1(spark, in2)
    df_OrderBy_3_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_3_1_1_1, 
        "Subgraph_1", 
        "hQ-ZcFacTHLr3CXkzVXmS$$QzUXZOzfigaoeYstb_sEO", 
        "PdaCtV9vo4MasJ8IRDqtt$$e3ARA3avfDhOBPii-a4s6"
    )
    df_Deduplicate_3_1_1_1 = Deduplicate_3_1_1_1(spark, df_OrderBy_3_1_1_1)
    df_Deduplicate_3_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_3_1_1_1, 
        "Subgraph_1", 
        "RjX--JVcdPL3uBLbRDsra$$I2RIPoLeRHDtWjXQuir4c", 
        "GIaAXZfUm9FNbKaCV3DFZ$$t8GfttCaQFhSfAiUoaK5T"
    )
    df_Deduplicate_3_1_1_1.cache().count()
    df_Deduplicate_3_1_1_1.unpersist()

    if (
        (
          (
          (Config.config_int_here == - 1001)
          and (Config.config_int_here == - 1001)
        )
        )
        and (
          (
          (Config.config_int_here == - 1001)
          or (Config.config_int_here == - 1001)
        )
        )
    ):
        df_Subgraph_4_1_1_1 = Subgraph_4_1_1_1(
            spark, 
            config.Subgraph_4_1_1_1, 
            df_RowDistributor_1_1_1_1_out0, 
            df_RowDistributor_1_1_1_1_out1, 
            df_Script_1_1_1_1
        )
    else:
        df_Subgraph_4_1_1_1 = None

    df_Limit_3_1_1_1 = Limit_3_1_1_1(spark, df_Reformat_8_1_1_1)
    df_Limit_3_1_1_1 = collectMetrics(
        spark, 
        df_Limit_3_1_1_1, 
        "Subgraph_1", 
        "zp7HQfS7RhIpMRngWwyuU$$Q9xiy1JplfwBABWKxro47", 
        "Z4pnlhuiyzjda-V6WaGFP$$FgfmqjsT5zyjTGpI6gj73"
    )
    df_Limit_3_1_1_1.cache().count()
    df_Limit_3_1_1_1.unpersist()

    return df_Subgraph_4_1_1_1
