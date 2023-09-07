from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *
from prophecy.utils import *
from pythondoanything.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_special_char_column_name = src_csv_special_char_column_name(spark)
    df_src_csv_special_char_column_name = collectMetrics(
        spark, 
        df_src_csv_special_char_column_name, 
        "graph", 
        "Q3B60_IDj1-PvB-3ycl1u$$eMslKZ3HG1Tyh8w5g8gnn", 
        "TXc4DmQNTK8TJLuC6o90M$$3BJUHI306XR_rI5G_0OGP"
    )
    df_Join_1 = Join_1(spark, df_src_csv_special_char_column_name, df_src_csv_special_char_column_name)
    df_Join_1 = collectMetrics(
        spark, 
        df_Join_1, 
        "graph", 
        "137K80y3J_y2nKIPveWdo$$YONheq58-hA9M-DeYkmC-", 
        "U46BB73bjEtFcl76lH0jo$$DcndQOeVDhSuNJ7kd0NI7"
    )
    df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_Join_1)
    df_RowDistributor_1_out0 = collectMetrics(
        spark, 
        df_RowDistributor_1_out0, 
        "graph", 
        "XGXl9wfBKmLBSsTgjSsbh$$RFMt3EcTJQQqW0kgj2_4A", 
        "abz6umNhKY7c7RG9y7PcP$$CqBTCxQjT7teRY5BytsJk"
    )
    df_RowDistributor_1_out1 = collectMetrics(
        spark, 
        df_RowDistributor_1_out1, 
        "graph", 
        "XGXl9wfBKmLBSsTgjSsbh$$RFMt3EcTJQQqW0kgj2_4A", 
        "K8FrS65keLz_jwy4xTYA7$$tXXesx4KUJ5X8TlBZ7qup"
    )
    df_src_parquet_all_type_and_partition_withspacehyphens = src_parquet_all_type_and_partition_withspacehyphens(spark)
    df_src_parquet_all_type_and_partition_withspacehyphens = collectMetrics(
        spark, 
        df_src_parquet_all_type_and_partition_withspacehyphens, 
        "graph", 
        "XaGxmUPFtr_k4A8tLik2o$$AhBIr_aJ-tSMwpbPBiu1o", 
        "tnCcyAVzzpmwLlE7FGpPw$$6NRK7Sq3s1g4S_5CqFMcy"
    )
    df_Reformat_1 = Reformat_1(spark, df_src_parquet_all_type_and_partition_withspacehyphens)
    df_Reformat_1 = collectMetrics(
        spark, 
        df_Reformat_1, 
        "graph", 
        "_iNAm7lo9gdqrRYPIuTiu$$7XZodQORqQv7yawOYzmoe", 
        "tq3e0STyAuuGeKvrKGk-x$$kk8e7yoFxP2nHm76ujL6P"
    )
    df_Filter_1 = Filter_1(spark, df_Reformat_1)
    df_Filter_1 = collectMetrics(
        spark, 
        df_Filter_1, 
        "graph", 
        "VcBmwe3XOQe-qVeQrhtRT$$XP69Nab5TLmlHiljeeutt", 
        "VSRdCuzX2NsePkmTPKAvE$$oJQ71SDQ-QDb5tF6N3ueO"
    )
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_1)
    df_OrderBy_1 = collectMetrics(
        spark, 
        df_OrderBy_1, 
        "graph", 
        "EavADLPc09FE5RyApIieX$$qYEUTeDkG72-HEmslozpE", 
        "aeYHpSU-YVYDxsdnLsu6x$$l2dk0AYFDtmvHCxNxU7ET"
    )
    df_Aggregate_1 = Aggregate_1(spark, df_OrderBy_1)
    df_Aggregate_1 = collectMetrics(
        spark, 
        df_Aggregate_1, 
        "graph", 
        "LGhqoSM55KcqAv0xjEg8r$$_6iCCInJwTgkmWYi7MUaV", 
        "ovEg--bx_9xXoEP8mCJVi$$BdmLAKRIPKQSnQVAGkgv1"
    )
    df_Aggregate_1.cache().count()
    df_Aggregate_1.unpersist()
    df_Repartition_1 = Repartition_1(spark, df_RowDistributor_1_out0)
    df_Repartition_1 = collectMetrics(
        spark, 
        df_Repartition_1, 
        "graph", 
        "Zm7rlIW8y5pPv6MgVGnB_$$VBSJLRR02W6fp5pocAJeC", 
        "JzqK9V271yFHbWn3QDKl5$$W88k9A1qi0Kt4kATD0fks"
    )
    df_Repartition_1.cache().count()
    df_Repartition_1.unpersist()
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_OrderBy_1)
    df_FlattenSchema_1 = collectMetrics(
        spark, 
        df_FlattenSchema_1, 
        "graph", 
        "pOYnY_3Fn5opLBsUjSU0c$$xLn_SyBmXZJjXO8HOCscI", 
        "Loh1GX6uIbF2HmVIi3bi8$$iifjWAzwIbjW-vPZWYKS9"
    )
    df_FlattenSchema_1.cache().count()
    df_FlattenSchema_1.unpersist()
    df_Script_1 = Script_1(spark, df_RowDistributor_1_out1)
    df_Script_1 = collectMetrics(
        spark, 
        df_Script_1, 
        "graph", 
        "mG2bKHRyiCbhqmxSIg1te$$MFR1W06kF12mONepQOnRC", 
        "5zl-SwpaRSWF8lXJjQh5z$$rySr23YBaPR-BM0vdzGyf"
    )
    df_Script_1.cache().count()
    df_Script_1.unpersist()
    df_src_orc_all_type_no_partition = src_orc_all_type_no_partition(spark)
    df_src_orc_all_type_no_partition = collectMetrics(
        spark, 
        df_src_orc_all_type_no_partition, 
        "graph", 
        "5N9hhKBRPM-oUfzHev4aY$$6jg37fCX5PCST2gRWgXvc", 
        "A-qOIGw7tv8nP1Jkus3hu$$Y01P7VXFjKXV3xcKEhSRd"
    )
    df_Limit_1 = Limit_1(spark, df_src_orc_all_type_no_partition)
    df_Limit_1 = collectMetrics(
        spark, 
        df_Limit_1, 
        "graph", 
        "gGKUb-_8JknkNG0n8UZYC$$yr2JmAKhQ5asJDJgEeClE", 
        "iTjeK6LghpBEcX9082b3P$$0UEJJ0wyZPZPaE9c3q8wr"
    )
    df_SetOperation_1 = SetOperation_1(
        spark, 
        df_src_parquet_all_type_and_partition_withspacehyphens, 
        df_src_parquet_all_type_and_partition_withspacehyphens
    )
    df_SetOperation_1 = collectMetrics(
        spark, 
        df_SetOperation_1, 
        "graph", 
        "prKanP_fC66HBfSplJchA$$Qav4mvQOy9Ck-0HYyUvNX", 
        "Dq1SboDC6bTAHNfImqQeh$$XFbQKvqeQFYL1biSrcVym"
    )
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_SetOperation_1)
    df_SchemaTransform_1 = collectMetrics(
        spark, 
        df_SchemaTransform_1, 
        "graph", 
        "aJWTvPk3pcRM4NVFwDKqF$$DWPgBM3pK_K5q4jQGPoVr", 
        "PW85G3fiER5_LevGFJArg$$TydKPqXpAOU9cZC17Iyog"
    )
    df_Deduplicate_1 = Deduplicate_1(spark, df_SchemaTransform_1)
    df_Deduplicate_1 = collectMetrics(
        spark, 
        df_Deduplicate_1, 
        "graph", 
        "VZLFT5Rzkx50ofjyU3OO-$$JoTjl1iuiJL_dHphwAgFc", 
        "jx9TD_4zOb8TdM6AGSP9I$$oFpi7JvBoHndwsD89S4Hf"
    )
    df_WindowFunction_1 = WindowFunction_1(spark, df_OrderBy_1)
    df_WindowFunction_1 = collectMetrics(
        spark, 
        df_WindowFunction_1, 
        "graph", 
        "habXdUxkB1YSw0F4WgEK_$$JMDXbjvyLSX24KMFxfF_k", 
        "dljLQVrhpc5Ic-pIULMix$$vC3DPufrh-9assgzKhlJq"
    )
    df_WindowFunction_1.cache().count()
    df_WindowFunction_1.unpersist()
    df_OrderBy_2 = OrderBy_2(spark, df_Limit_1)
    df_OrderBy_2 = collectMetrics(
        spark, 
        df_OrderBy_2, 
        "graph", 
        "HytKPoc2pRfcEWIbU8CdH$$lfQmTWXF2Mt14RjzRoHx3", 
        "fz5eaFER_KvPf1N-5VTFZ$$MXmRuvyj5ZAcGT4wE4W7u"
    )
    df_OrderBy_2.cache().count()
    df_OrderBy_2.unpersist()
    df_SQLStatement_1_out, df_SQLStatement_1_out1 = SQLStatement_1(spark, df_Deduplicate_1)
    df_SQLStatement_1_out = collectMetrics(
        spark, 
        df_SQLStatement_1_out, 
        "graph", 
        "bnWsAJKOEKd4kKqt1j4GT$$3_88kM_ESb9l2c0LHur5Q", 
        "mEyTHd0mPFvDW7vO8cs9z$$TZMyvix2epEtX87Ydb2RJ"
    )
    df_SQLStatement_1_out1 = collectMetrics(
        spark, 
        df_SQLStatement_1_out1, 
        "graph", 
        "bnWsAJKOEKd4kKqt1j4GT$$3_88kM_ESb9l2c0LHur5Q", 
        "jijn277YMwCE-ZRFWk1AT$$9Y19wgwcixNlenxMl1h3t"
    )
    df_SQLStatement_1_out.cache().count()
    df_SQLStatement_1_out.unpersist()
    df_SQLStatement_1_out1.cache().count()
    df_SQLStatement_1_out1.unpersist()

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules", "org.apache.spark.sql.catalyst.optimizer.ColumnPruning")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_GCP")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_GCP", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_GCP")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
