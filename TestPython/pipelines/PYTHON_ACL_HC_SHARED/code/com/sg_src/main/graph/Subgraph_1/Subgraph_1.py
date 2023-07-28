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
) -> (DataFrame, DataFrame, DataFrame):
    Config.update(config)
    df_Source_1_1_1 = Source_1_1_1(spark)
    df_Source_1_1_1 = collectMetrics(
        spark, 
        df_Source_1_1_1, 
        "Subgraph_1", 
        "1r_pZPVR3jKgUYztuH7tP$$HCzfgjR_8lJN8VyR6K8Uq", 
        "vrGooAVxXtbCLM9W-fF9T$$-KHAu0njsWpG2L_gqpbcT"
    )
    Lookup_1(spark, df_Source_1_1_1)
    df_Reformat_1_1_1 = Reformat_1_1_1(spark, df_Source_1_1_1)
    df_Reformat_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_1_1_1, 
        "Subgraph_1", 
        "Rs1_2W86Fz2uEOx4rSPuK$$osbmM-J62JQQYYImKc0Za", 
        "Xh7JXB8u5rtXUDlUQrCoh$$fMufkUiADpJxYEm80rGuU"
    )
    df_Reformat_2_1_1 = Reformat_2_1_1(spark, in0)
    df_Reformat_2_1_1 = collectMetrics(
        spark, 
        df_Reformat_2_1_1, 
        "Subgraph_1", 
        "QTebrQxcnMAv36Nrl63HZ$$dIUDEnIHEZInk-GBLsk9m", 
        "7nZx0CC34uTUy4PtEZymC$$Z52tIAdl0qk2YjEpKMsN6"
    )
    df_Join_1_1 = Join_1_1(spark, df_Reformat_1_1_1, df_Reformat_2_1_1)
    df_Join_1_1 = collectMetrics(
        spark, 
        df_Join_1_1, 
        "Subgraph_1", 
        "GbN9UX4QagmmdTDy5lRB7$$QJivOOeJN4Ft1G5fLGd9f", 
        "O2iO5NU5HNEsmU520TNq_$$-rIksNtHS1M3s5IENgD5H"
    )
    df_Limit_1_1_1 = Limit_1_1_1(spark, df_Join_1_1)
    df_Limit_1_1_1 = collectMetrics(
        spark, 
        df_Limit_1_1_1, 
        "Subgraph_1", 
        "gyHkhltV014QeqsokWIIQ$$bLHvEIoyVX0bj0U6YV8Jj", 
        "4C61I3tvKmt_X8E29ZH6k$$F2tBA-joW-4Ni8Ydl2jUV"
    )
    df_Filter_1_1_1 = Filter_1_1_1(spark, df_Limit_1_1_1)
    df_Filter_1_1_1 = collectMetrics(
        spark, 
        df_Filter_1_1_1, 
        "Subgraph_1", 
        "C24ulF5fayEDM8juBsH4j$$xitmIFJlLbNipAjTBuG2x", 
        "2rUoefG1Q0m10sbPniEa3$$dChfDyeDtZN69UnntDR45"
    )
    df_OrderBy_1_1_1 = OrderBy_1_1_1(spark, df_Filter_1_1_1)
    df_OrderBy_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_1_1_1, 
        "Subgraph_1", 
        "FdMdMKA9PwdDzQISgBmgv$$oDOH6Ddy73N4x4CMJtZPP", 
        "1BzY1nnb-9FJ1TEI9BHBg$$RgjBLyDUFwsdsl-s9CT9Z"
    )
    df_Reformat_5 = Reformat_5(spark, df_Reformat_2_1_1)
    df_Reformat_5 = collectMetrics(
        spark, 
        df_Reformat_5, 
        "Subgraph_1", 
        "7Lx4J_SbHcFsLK8LlsKM8$$ANO3o_UVD96vKQVjIQ-ti", 
        "TGHCKhuXd1aM7IHgIIuST$$i5bT6wDFzKLNQPd0cFLUX"
    )
    df_Subgraph_1 = Subgraph_1(spark, config.Subgraph_1, df_Reformat_5)
    df_Aggregate_1_1_1 = Aggregate_1_1_1(spark, df_OrderBy_1_1_1)
    df_Aggregate_1_1_1 = collectMetrics(
        spark, 
        df_Aggregate_1_1_1, 
        "Subgraph_1", 
        "OfT5Aq5SMdAyz3OV3xklC$$NARp1z05TzVgf-5K2VcGT", 
        "Ku_NG7h8pJiUsIeAGbt56$$GBjYhtlfMpgFT25pzEssU"
    )
    df_Subgraph_2 = Subgraph_2(spark, config.Subgraph_2, df_Subgraph_1)
    df_Subgraph_2.cache().count()
    df_Subgraph_2.unpersist()
    df_Repartition_1_1_1 = Repartition_1_1_1(spark, df_Limit_1_1_1)
    df_Repartition_1_1_1 = collectMetrics(
        spark, 
        df_Repartition_1_1_1, 
        "Subgraph_1", 
        "HWz_Oa6ZdW5o0Gi_49u-c$$o9iw7O3uiuR9LyXlUPlaH", 
        "o_Bf30uwcijDr4Mqg9J5Q$$2HNyOr5e2V4PAuFyn_pKV"
    )
    df_RowDistributor_1_1_1_out0, df_RowDistributor_1_1_1_out1 = RowDistributor_1_1_1(spark, df_Repartition_1_1_1)
    df_RowDistributor_1_1_1_out0 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_out0, 
        "Subgraph_1", 
        "Luy_AH7IaKcLQoR8ro4Sf$$9ZI3VLJt3lIQU_fUrC7k_", 
        "1E2PiLjmHUqLynLaEnyCk$$Sn6PwBe-7NkfAAkZjnAmT"
    )
    df_RowDistributor_1_1_1_out1 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_out1, 
        "Subgraph_1", 
        "Luy_AH7IaKcLQoR8ro4Sf$$9ZI3VLJt3lIQU_fUrC7k_", 
        "1EwHOqiPZ72rR68y-KeiG$$AFnYfoljvJ4Dk-tpL7JoZ"
    )
    df_OrderBy_3_1_1 = OrderBy_3_1_1(spark, in2)
    df_OrderBy_3_1_1 = collectMetrics(
        spark, 
        df_OrderBy_3_1_1, 
        "Subgraph_1", 
        "N_q0oNs6I9Th86QzopXq3$$zcnFDwL5OalZnBKwj6DN1", 
        "KAU9vWbd6bQb3HTGkuzZB$$uxaUL9SHUZHW8KwqGFCuj"
    )
    df_Deduplicate_3_1_1 = Deduplicate_3_1_1(spark, df_OrderBy_3_1_1)
    df_Deduplicate_3_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_3_1_1, 
        "Subgraph_1", 
        "-Nrb7QUp1eCEqz0AyZHzO$$RqVLXB0KvOT1hBtX-ST4d", 
        "LcvMPPnxzPBzC6QZPp_KJ$$2fyNDszd4bnaRogtJyJ6K"
    )
    df_SchemaTransform_1_1_1 = SchemaTransform_1_1_1(spark, df_Aggregate_1_1_1)
    df_SchemaTransform_1_1_1 = collectMetrics(
        spark, 
        df_SchemaTransform_1_1_1, 
        "Subgraph_1", 
        "iG8957kdxSmfu07RUwfoB$$1EZJOw0WwODQ_yu9OwcBG", 
        "rVo0A5cms8UV5uQLRNcWw$$JHeLmSQqQYIBIXs3BCSmH"
    )
    df_Deduplicate_1_1_1 = Deduplicate_1_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_1_1_1, 
        "Subgraph_1", 
        "uwaoDWL2HnqS9obV8tUjF$$nIQRicDGF7cUAGNCthXg0", 
        "8X76Tt1F5v5IHcr3p28Ft$$1Q1Xi8yaBRI5oy-mPm1_r"
    )
    df_Deduplicate_2_1_1 = Deduplicate_2_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_2_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_2_1_1, 
        "Subgraph_1", 
        "kVRevUdYnj2gVUfwaaQnS$$WWyx1UStxaPc43G3C3SWN", 
        "C7pDD_QjctbPnqOzEhe_J$$t6dUIr1GEnjMNMWe53Q_2"
    )
    df_SetOperation_1_1_1 = SetOperation_1_1_1(spark, df_Deduplicate_1_1_1, df_Deduplicate_2_1_1)
    df_SetOperation_1_1_1 = collectMetrics(
        spark, 
        df_SetOperation_1_1_1, 
        "Subgraph_1", 
        "c2RCqWeCFSP45FFtbXtg6$$edondjvcJQtDmodyDWKKt", 
        "DzE6skFt4WEu_h2op_uU-$$W_hDtX_rDdYikA0zMLV_y"
    )
    df_WindowFunction_1_1_1 = WindowFunction_1_1_1(spark, df_SetOperation_1_1_1)
    df_WindowFunction_1_1_1 = collectMetrics(
        spark, 
        df_WindowFunction_1_1_1, 
        "Subgraph_1", 
        "tnoOANcn_jdGbTDqenzaf$$jJdtN5kozHJJFtQah98Z2", 
        "AQxmVdWuNbRGwuPyaRGNp$$nZ9y2_CNEXGq4l1l2QwkC"
    )
    df_Script_1_1_1 = Script_1_1_1(spark, df_WindowFunction_1_1_1)
    df_Script_1_1_1 = collectMetrics(
        spark, 
        df_Script_1_1_1, 
        "Subgraph_1", 
        "kDtlPVKdWUQf_7XY6ifv3$$R1xtNAjxb0ZkIyifOVlLx", 
        "yfDfY5NcG_9ODRyxLBvMF$$sRj89OSU1-MQEDw1W4EuB"
    )
    df_Subgraph_4_1_1 = Subgraph_4_1_1(
        spark, 
        config.Subgraph_4_1_1, 
        df_RowDistributor_1_1_1_out0, 
        df_RowDistributor_1_1_1_out1, 
        df_Script_1_1_1
    )
    df_Reformat_4 = Reformat_4(spark, df_Source_1_1_1)
    df_Reformat_4 = collectMetrics(
        spark, 
        df_Reformat_4, 
        "Subgraph_1", 
        "doZp9lh3MPrvMLlS8l2o7$$GIK_zV4Wva18b-2Gp3MJD", 
        "2eHJNsaAMqpCTDEffO3wW$$gtX9TBeOXkDLAAqcNzClN"
    )
    df_Reformat_8_1_1 = Reformat_8_1_1(spark, in1)
    df_Reformat_8_1_1 = collectMetrics(
        spark, 
        df_Reformat_8_1_1, 
        "Subgraph_1", 
        "YHIfTUaSlFVhJPOGJROKe$$yx9-kVu3uQzdFC7desbn_", 
        "6SGK1kGgLTQ8zVbOGEyZA$$82LZDFPwwHxw1VwIXLkeb"
    )
    py_sg_target_test_release(spark, df_Reformat_4)
    df_Limit_3_1_1 = Limit_3_1_1(spark, df_Reformat_8_1_1)
    df_Limit_3_1_1 = collectMetrics(
        spark, 
        df_Limit_3_1_1, 
        "Subgraph_1", 
        "upAb93zRvQLP1GxdWLDac$$BgRO2qcyEynwxmsI0sXMt", 
        "IE05rCO7oJ17bB-lvwoQJ$$9Vh9U9Smu44MCs-0-N0Wi"
    )

    return df_Subgraph_4_1_1, df_Limit_3_1_1, df_Deduplicate_3_1_1
