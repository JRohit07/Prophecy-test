from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *
from prophecy.utils import *
from livy_python.graph import *

def pipeline(spark: SparkSession) -> None:
    df_livy_src_csv_py = livy_src_csv_py(spark)
    df_livy_src_csv_py = collectMetrics(
        spark, 
        df_livy_src_csv_py, 
        "graph", 
        "zx05CFL6hqZyBtPOu1pkf$$lpZkqTQg5wA92sceBzvlb", 
        "s1Tt_dqrlegFG6g3Zv_GA$$HiT49iNoOhQUhnT5w6ngO"
    )
    Lookup_1(spark, df_livy_src_csv_py)
    df_Reformat_1 = Reformat_1(spark, df_livy_src_csv_py)
    df_Reformat_1 = collectMetrics(
        spark, 
        df_Reformat_1, 
        "graph", 
        "LmVB9Tiv7gOksXKYvwwqv$$vRQhC-glg7Tz8vdDjYpL9", 
        "sEqrqRgL-8RgpQvmEL4qv$$oEdp_cRkhh3jJCtYi3j2w"
    )

    if (Config.c_int > - 100):
        df_Passthis = Passthis(spark, df_Reformat_1)
        df_Passthis = collectMetrics(
            spark, 
            df_Passthis, 
            "graph", 
            "Vrtqa_BfAGegoUtXAoWAZ$$yIAGYIP1HaX2HeCwlgsj4", 
            "jzMN-lPzLaBW2PDCJHdMq$$nuiPjaTadVFNWL8LV7p3L"
        )
    else:
        df_Passthis = df_Reformat_1

    df_Limit_1 = Limit_1(spark, df_Passthis)
    df_Limit_1 = collectMetrics(
        spark, 
        df_Limit_1, 
        "graph", 
        "H-HJjiVMj7uZnrBAQ_k9I$$8_amaO0dfSJ6XWqsH63ke", 
        "Hz7UE9WmYu-cDlCj-n5YL$$-a00eccqb6iaT8aqIeAdI"
    )
    df_Subgraph_4 = Subgraph_4(spark, Config.Subgraph_4, df_livy_src_csv_py)

    if Config.c_int == - 100:
        if (Config.c_int == - 100):
            df_SQLStatement_1_output_1, df_SQLStatement_1_out1, df_SQLStatement_1_out2 = SQLStatement_1(
                spark, 
                df_Subgraph_4, 
                df_Subgraph_4, 
                df_Subgraph_4
            )
            df_SQLStatement_1_output_1 = collectMetrics(
                spark, 
                df_SQLStatement_1_output_1, 
                "graph", 
                "9-xNzDAfIfX0jip9-OCbN$$rgiOyR9RmNVietEkrnYzX", 
                "Zg1yBISd3Xj7tCv1qkHw_$$MO01q71plfyyDKkq0iCRY"
            )
            df_SQLStatement_1_out1 = collectMetrics(
                spark, 
                df_SQLStatement_1_out1, 
                "graph", 
                "9-xNzDAfIfX0jip9-OCbN$$rgiOyR9RmNVietEkrnYzX", 
                "Q970Kv4asYbHlWdUADK3a$$Lj6wCeZUPLMjYT7ZWdk0M"
            )
            df_SQLStatement_1_out2 = collectMetrics(
                spark, 
                df_SQLStatement_1_out2, 
                "graph", 
                "9-xNzDAfIfX0jip9-OCbN$$rgiOyR9RmNVietEkrnYzX", 
                "Lom86pdI8EPn8HYZIUife$$bsR6P5ngNVcCbYTuCqKFZ"
            )
        else:
            df_SQLStatement_1_output_1 = df_Subgraph_4
            df_SQLStatement_1_out1 = df_Subgraph_4
            df_SQLStatement_1_out2 = df_Subgraph_4
    else:
        df_SQLStatement_1_output_1, df_SQLStatement_1_out1, df_SQLStatement_1_out2 = None, None, None

    if Config.c_int == - 100:
        df_Reformat_5 = Reformat_5(spark, df_SQLStatement_1_out1)
        df_Reformat_5 = collectMetrics(
                              spark, 
                              df_Reformat_5, 
                              "graph", 
                              "SAvIjpKonhri_rQm4i94P$$5PfK4KJufGSLrwml4L-L8", 
                              "VJ287DfF_Qxtn3OWXNo13$$jG9xvPkR2IRkOIlpqyUOq"
                            )\
                            .cache()
    else:
        df_Reformat_5 = None

    if Config.c_int == - 100:
        df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_Subgraph_4)
        df_RowDistributor_1_out0 = collectMetrics(
            spark, 
            df_RowDistributor_1_out0, 
            "graph", 
            "okdX0HxsByJytl8-bE0Kt$$lnNRIoVu9tZHpCufDrTEZ", 
            "FbZ5yqx70ILvxmoLM6e4Z$$C0Xl-mX0aCzxIHmVk8rhU"
        )
        df_RowDistributor_1_out1 = collectMetrics(
            spark, 
            df_RowDistributor_1_out1, 
            "graph", 
            "okdX0HxsByJytl8-bE0Kt$$lnNRIoVu9tZHpCufDrTEZ", 
            "2vqZcM6pio0AhP0eYPP7p$$fpPmls3odio2P4nWrxi_9"
        )
    else:
        df_RowDistributor_1_out0, df_RowDistributor_1_out1 = None, None

    df_SetOperation_1 = SetOperation_1(spark, df_Reformat_1, df_Reformat_1)
    df_SetOperation_1 = collectMetrics(
        spark, 
        df_SetOperation_1, 
        "graph", 
        "ZZMLx6qIPkco-6Lzn_Bkq$$W6J4G5WzbXaK0Ev-YvUcS", 
        "ISaF3Q4I-FudtVSXTdXHt$$6W-4kvVqiAX0YhO5TKPng"
    )
    df_pythonLivySG1_1 = pythonLivySG1_1(spark, Config.pythonLivySG1_1, df_SetOperation_1)
    df_Reformat_6 = Reformat_6(spark, df_livy_src_csv_py)
    df_Reformat_6 = collectMetrics(
        spark, 
        df_Reformat_6, 
        "graph", 
        "PNhi4lmIelHMypOn-G-V6$$wWaUyMIBzMWnm9LVoVXyw", 
        "4DXqAMUe4cjwmlGQNilYM$$AcStS37btFdHIOEaC5gKR"
    )
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_Reformat_6)
    df_FlattenSchema_1 = collectMetrics(
        spark, 
        df_FlattenSchema_1, 
        "graph", 
        "PLXJZjPpniwsyKT9H5oQ2$$rhAROnhkWDMD8khXJ86ov", 
        "oDu2VjkQRtQXUJYy-UlAN$$rPnNW_t_L3QL3ciDEnC-V"
    )
    df_FlattenSchema_1.cache().count()
    df_FlattenSchema_1.unpersist()
    df_Script_1 = Script_1(spark, df_pythonLivySG1_1)
    df_Script_1 = collectMetrics(
        spark, 
        df_Script_1, 
        "graph", 
        "fOZph6tqo_K1Rt9vgTVa0$$AiVZhCjnpc0OShMUVKXaN", 
        "yCS9zJWNTbhfBGi7d_rhx$$e5-ARkRu0s7eOa5ZVi_hE"
    )

    if Config.c_int == - 100:
        df_Filter_1 = Filter_1(spark, df_SQLStatement_1_out2)
        df_Filter_1 = collectMetrics(
            spark, 
            df_Filter_1, 
            "graph", 
            "ffkpa2xcEAKQd_V9dtBkb$$cmhhOFAt_zkewnQTRJdl_", 
            "Vl3e150CwE1sSMZmmEx5q$$2E7cNVITsy5IcsyH8j1wB"
        )
    else:
        df_Filter_1 = None

    if ((Config.c_int == - 100) and (Config.c_int == - 100)):
        df_Join_1 = Join_1(spark, df_Reformat_5, df_Filter_1)
        df_Join_1 = collectMetrics(
            spark, 
            df_Join_1, 
            "graph", 
            "mcREc5ULGIDbqTQT4PGMV$$h8W-DxAvdqrRtw3o8UMa2", 
            "TO8KMHbkL8JSdhy5QTkNY$$BA9F3bRXOFpnbcAnDFSEr"
        )
        df_Join_1.cache().count()
        df_Join_1.unpersist()
    else:
        df_Join_1 = None

    df_Reformat_3 = Reformat_3(spark, df_Script_1)
    df_Reformat_3 = collectMetrics(
        spark, 
        df_Reformat_3, 
        "graph", 
        "Jxv_Oyc8PQrWG1PmyrJWU$$NO49MgMTi0uBbmNDIOcvb", 
        "wWK-RoSVQWQkdaGB7wCwl$$gnAu9To4IOgvRScWdZu07"
    )
    df_Reformat_3.cache().count()
    df_Reformat_3.unpersist()
    df_Reformat_7 = Reformat_7(spark, df_Limit_1)
    df_Reformat_7 = collectMetrics(
        spark, 
        df_Reformat_7, 
        "graph", 
        "sC_0hlsvhC-g7VumbUIev$$ihdNR3pHujCuTUXuhVIoe", 
        "xcD14mVtDqPX0ofOMoKyF$$tdfXFi6GPgFpkIXmQHuVv"
    )
    df_Reformat_7.cache().count()
    df_Reformat_7.unpersist()

    if Config.c_int == - 100:
        df_Reformat_2 = Reformat_2(spark, df_RowDistributor_1_out0)
        df_Reformat_2 = collectMetrics(
                              spark, 
                              df_Reformat_2, 
                              "graph", 
                              "-JMYTUou3YiFhB2tmOsc2$$8GHDhvfsV8g3p9540HDNx", 
                              "KOVVuemi6iWTgEkkqxTOu$$sRJ676Y739CsKUd1s-dI6"
                            )\
                            .cache()
        df_SchemaTransform_1 = SchemaTransform_1(spark, df_Reformat_2)
        df_SchemaTransform_1 = collectMetrics(
            spark, 
            df_SchemaTransform_1, 
            "graph", 
            "O2L_X7boFoR4lSoQnpI6s$$cm5YF5lbAABPT2sbudYnJ", 
            "dWkzwBE-t4wT5V0o2eDHv$$aSn9WPFdimLtEtO7-OgrZ"
        )
        df_SchemaTransform_1.cache().count()
        df_SchemaTransform_1.unpersist()
    else:
        df_SchemaTransform_1 = None

    df_Script_2 = Script_2(spark, df_livy_src_csv_py)
    df_Script_2 = collectMetrics(
        spark, 
        df_Script_2, 
        "graph", 
        "HLpRudnxzFDOH6v50FTRn$$8wuAjgdN082A7wiou-BTt", 
        "i1QoJ8dz-D0slSyVrkf6T$$mzY5TGbgYjL3mnvNxoWTI"
    )
    df_Reformat_4 = Reformat_4(spark, df_Script_2)
    df_Reformat_4 = collectMetrics(
        spark, 
        df_Reformat_4, 
        "graph", 
        "_6hu-g0ECNB72wApYb9QS$$-GZRkDJSIv9my71HOnwNS", 
        "SeSwA4cx3e8Bp85gnnw1Q$$xmrsbKC2u-Fmm-E7B6GiD"
    )
    df_Reformat_4.cache().count()
    df_Reformat_4.unpersist()

    if Config.c_int == - 100:
        Script_3(spark, df_SQLStatement_1_output_1)

    if Config.c_int == - 100:
        df_Filter_2 = Filter_2(spark, df_RowDistributor_1_out1)
        df_Filter_2 = collectMetrics(
            spark, 
            df_Filter_2, 
            "graph", 
            "XNaycAFAbJ4hInFkYL4az$$tQzPHz9quEmQPMtKjyRJc", 
            "DSV6Pj9Gmo2SH1NbPcct3$$ZSJEXSajOByNasLwgdWwH"
        )
        df_Filter_2.cache().count()
        df_Filter_2.unpersist()
    else:
        df_Filter_2 = None

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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/LIVY_PYTHON")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/LIVY_PYTHON", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/LIVY_PYTHON")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
