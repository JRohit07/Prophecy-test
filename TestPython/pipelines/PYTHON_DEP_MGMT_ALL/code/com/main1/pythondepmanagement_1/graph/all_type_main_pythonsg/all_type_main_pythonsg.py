from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def all_type_main_pythonsg(
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
        "all_type_main_pythonsg", 
        "1r_pZPVR3jKgUYztuH7tP$$c8x91UWqkhUr2xdfXv4hN", 
        "vrGooAVxXtbCLM9W-fF9T$$ePua0f02FpKYgOnMkPUfD"
    )
    Lookup_1(spark, df_Source_1_1_1)
    df_Reformat_1_1_1 = Reformat_1_1_1(spark, df_Source_1_1_1)
    df_Reformat_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_1_1_1, 
        "all_type_main_pythonsg", 
        "Rs1_2W86Fz2uEOx4rSPuK$$yHeu10MZOkk9el_vMQYlq", 
        "Xh7JXB8u5rtXUDlUQrCoh$$k2GT-o0fD-Rsq_Cg6kGZp"
    )
    df_Reformat_2_1_1 = Reformat_2_1_1(spark, in0)
    df_Reformat_2_1_1 = collectMetrics(
        spark, 
        df_Reformat_2_1_1, 
        "all_type_main_pythonsg", 
        "QTebrQxcnMAv36Nrl63HZ$$efgkoglFHSkxHbpz8JQt6", 
        "7nZx0CC34uTUy4PtEZymC$$cHV6S0ZvxadbvkWsKPphi"
    )
    df_Join_1_1 = Join_1_1(spark, df_Reformat_1_1_1, df_Reformat_2_1_1)
    df_Join_1_1 = collectMetrics(
        spark, 
        df_Join_1_1, 
        "all_type_main_pythonsg", 
        "GbN9UX4QagmmdTDy5lRB7$$d-5eA9aUTHSMb_MWxtKix", 
        "O2iO5NU5HNEsmU520TNq_$$xeNv7CBuFULizdJ2yQppG"
    )
    df_Limit_1_1_1 = Limit_1_1_1(spark, df_Join_1_1)
    df_Limit_1_1_1 = collectMetrics(
        spark, 
        df_Limit_1_1_1, 
        "all_type_main_pythonsg", 
        "gyHkhltV014QeqsokWIIQ$$IkJJH-D6Lv-NDKemSaL3b", 
        "4C61I3tvKmt_X8E29ZH6k$$stKXJoYfzssr3abSPSzGw"
    )
    df_Filter_1_1_1 = Filter_1_1_1(spark, df_Limit_1_1_1)
    df_Filter_1_1_1 = collectMetrics(
        spark, 
        df_Filter_1_1_1, 
        "all_type_main_pythonsg", 
        "C24ulF5fayEDM8juBsH4j$$uGm_KCjn2Jj-4ZZLg2TMm", 
        "2rUoefG1Q0m10sbPniEa3$$9T-ukUxQZADTpciPPg7gu"
    )
    df_OrderBy_1_1_1 = OrderBy_1_1_1(spark, df_Filter_1_1_1)
    df_OrderBy_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_1_1_1, 
        "all_type_main_pythonsg", 
        "FdMdMKA9PwdDzQISgBmgv$$_KK9hA9VOEizcEen0tBYA", 
        "1BzY1nnb-9FJ1TEI9BHBg$$rDW0Qmc4tBTIxYOAk63id"
    )
    df_Aggregate_1_1_1 = Aggregate_1_1_1(spark, df_OrderBy_1_1_1)
    df_Aggregate_1_1_1 = collectMetrics(
        spark, 
        df_Aggregate_1_1_1, 
        "all_type_main_pythonsg", 
        "OfT5Aq5SMdAyz3OV3xklC$$cAHGapvWjPRcDsY5tPUDm", 
        "Ku_NG7h8pJiUsIeAGbt56$$fVaZe1qQf5evP1Lke49AO"
    )
    df_SchemaTransform_1_1_1 = SchemaTransform_1_1_1(spark, df_Aggregate_1_1_1)
    df_SchemaTransform_1_1_1 = collectMetrics(
        spark, 
        df_SchemaTransform_1_1_1, 
        "all_type_main_pythonsg", 
        "iG8957kdxSmfu07RUwfoB$$cBmNpuNDwVpIFLXwRz4ui", 
        "rVo0A5cms8UV5uQLRNcWw$$Lvg6OD6jLJOLoCVf_VShF"
    )
    df_Deduplicate_1_1_1 = Deduplicate_1_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_1_1_1, 
        "all_type_main_pythonsg", 
        "uwaoDWL2HnqS9obV8tUjF$$9CJ3kWh_F7_PWE5yP6aQg", 
        "8X76Tt1F5v5IHcr3p28Ft$$Q4b-jxdEIRaawabqzQ9Op"
    )
    df_Deduplicate_2_1_1 = Deduplicate_2_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_2_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_2_1_1, 
        "all_type_main_pythonsg", 
        "kVRevUdYnj2gVUfwaaQnS$$6R8QtEi-da_OVvJLuGDeH", 
        "C7pDD_QjctbPnqOzEhe_J$$uKEM4B9t0-pRSP4lFRPUd"
    )
    df_SetOperation_1_1_1 = SetOperation_1_1_1(spark, df_Deduplicate_1_1_1, df_Deduplicate_2_1_1)
    df_SetOperation_1_1_1 = collectMetrics(
        spark, 
        df_SetOperation_1_1_1, 
        "all_type_main_pythonsg", 
        "c2RCqWeCFSP45FFtbXtg6$$4OqMX9y6MUwLpw163tAo3", 
        "DzE6skFt4WEu_h2op_uU-$$vY4alF0GFLqwrQfQEjG0A"
    )
    df_WindowFunction_1_1_1 = WindowFunction_1_1_1(spark, df_SetOperation_1_1_1)
    df_WindowFunction_1_1_1 = collectMetrics(
        spark, 
        df_WindowFunction_1_1_1, 
        "all_type_main_pythonsg", 
        "tnoOANcn_jdGbTDqenzaf$$XRRR4Ky9JVvda0ONlQaIe", 
        "AQxmVdWuNbRGwuPyaRGNp$$w1y3sW1U82-0gHsLPr61p"
    )
    df_Script_1_1_1 = Script_1_1_1(spark, df_WindowFunction_1_1_1)
    df_Script_1_1_1 = collectMetrics(
        spark, 
        df_Script_1_1_1, 
        "all_type_main_pythonsg", 
        "kDtlPVKdWUQf_7XY6ifv3$$ugsf2Hcqs6OK-QQ6fmKi9", 
        "yfDfY5NcG_9ODRyxLBvMF$$SQDMKtHFg1nwuUajPiiY5"
    )
    df_Repartition_1_1_1 = Repartition_1_1_1(spark, df_Limit_1_1_1)
    df_Repartition_1_1_1 = collectMetrics(
        spark, 
        df_Repartition_1_1_1, 
        "all_type_main_pythonsg", 
        "HWz_Oa6ZdW5o0Gi_49u-c$$DuD1eZlM8yyDp8J0YNa59", 
        "o_Bf30uwcijDr4Mqg9J5Q$$ZKR8bjdr3zYeSYFS8qvzx"
    )
    df_RowDistributor_1_1_1_out0, df_RowDistributor_1_1_1_out1 = RowDistributor_1_1_1(spark, df_Repartition_1_1_1)
    df_RowDistributor_1_1_1_out0 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_out0, 
        "all_type_main_pythonsg", 
        "Luy_AH7IaKcLQoR8ro4Sf$$KHGdNcTVDNJobJJAUDdEO", 
        "1E2PiLjmHUqLynLaEnyCk$$190FSKzeDuisXc5lwjBp6"
    )
    df_RowDistributor_1_1_1_out1 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_out1, 
        "all_type_main_pythonsg", 
        "Luy_AH7IaKcLQoR8ro4Sf$$KHGdNcTVDNJobJJAUDdEO", 
        "1EwHOqiPZ72rR68y-KeiG$$nTY30FdpnByg7D2RQDroS"
    )
    df_Reformat_4 = Reformat_4(spark, df_Source_1_1_1)
    df_Reformat_4 = collectMetrics(
        spark, 
        df_Reformat_4, 
        "all_type_main_pythonsg", 
        "doZp9lh3MPrvMLlS8l2o7$$anMe7Ptt_GbeGRa_-oBFH", 
        "2eHJNsaAMqpCTDEffO3wW$$yCE8K4RFi_yjTh4f_Q1Ra"
    )
    py_sg_target_test_release(spark, df_Reformat_4)
    df_Subgraph_4_1_1 = Subgraph_4_1_1(
        spark, 
        config.Subgraph_4_1_1, 
        df_RowDistributor_1_1_1_out0, 
        df_RowDistributor_1_1_1_out1, 
        df_Script_1_1_1
    )
    df_Reformat_5 = Reformat_5(spark, df_Reformat_2_1_1)
    df_Reformat_5 = collectMetrics(
        spark, 
        df_Reformat_5, 
        "all_type_main_pythonsg", 
        "7Lx4J_SbHcFsLK8LlsKM8$$Hxd6_ln8Vjw4ZV-LltKwS", 
        "TGHCKhuXd1aM7IHgIIuST$$UPk8WuPU-YGpE6g8DfQHC"
    )
    df_OrderBy_3_1_1 = OrderBy_3_1_1(spark, in2)
    df_OrderBy_3_1_1 = collectMetrics(
        spark, 
        df_OrderBy_3_1_1, 
        "all_type_main_pythonsg", 
        "N_q0oNs6I9Th86QzopXq3$$P_Pau4ysDoCpxTJ3yshK5", 
        "KAU9vWbd6bQb3HTGkuzZB$$4ZYgUc8sclRAk8OBOg9mH"
    )
    df_Deduplicate_3_1_1 = Deduplicate_3_1_1(spark, df_OrderBy_3_1_1)
    df_Deduplicate_3_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_3_1_1, 
        "all_type_main_pythonsg", 
        "-Nrb7QUp1eCEqz0AyZHzO$$a6zhSA6Gdx94o9StIiW_z", 
        "LcvMPPnxzPBzC6QZPp_KJ$$1TmSKXe2RNj6NQRzRtyB9"
    )
    df_Subgraph_1 = Subgraph_1(spark, config.Subgraph_1, df_Reformat_5)
    df_Subgraph_2 = Subgraph_2(spark, config.Subgraph_2, df_Subgraph_1)
    df_Subgraph_2.cache().count()
    df_Subgraph_2.unpersist()
    df_Reformat_8_1_1 = Reformat_8_1_1(spark, in1)
    df_Reformat_8_1_1 = collectMetrics(
        spark, 
        df_Reformat_8_1_1, 
        "all_type_main_pythonsg", 
        "YHIfTUaSlFVhJPOGJROKe$$CNMfQMj4_qKcidaMNFIM_", 
        "6SGK1kGgLTQ8zVbOGEyZA$$dhi4ffm1R8G0URvHtcaq8"
    )
    df_Limit_3_1_1 = Limit_3_1_1(spark, df_Reformat_8_1_1)
    df_Limit_3_1_1 = collectMetrics(
        spark, 
        df_Limit_3_1_1, 
        "all_type_main_pythonsg", 
        "upAb93zRvQLP1GxdWLDac$$iO91s6dvK4axbg4y75uRQ", 
        "IE05rCO7oJ17bB-lvwoQJ$$UI6quSPNliDLTTnN0tMxC"
    )

    return df_Subgraph_4_1_1, df_Limit_3_1_1, df_Deduplicate_3_1_1
