from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *
from prophecy.utils import *
from livy_python.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataproc_livy_src_annual_enterprise = dataproc_livy_src_annual_enterprise(spark)
    df_dataproc_livy_src_annual_enterprise = collectMetrics(
        spark, 
        df_dataproc_livy_src_annual_enterprise, 
        "graph", 
        "3iRNyhQn4c2t7Y3gErD7U$$2b6D6gUofrM8RJccNXY-2", 
        "PaBXPGFSPFzbYJdJVu84P$$PQ3AoYH2a4JHwMTpZEkFK"
    )
    Lookup_1(spark, df_dataproc_livy_src_annual_enterprise)
    df_Reformat_1 = Reformat_1(spark, df_dataproc_livy_src_annual_enterprise)
    df_Reformat_1 = collectMetrics(
        spark, 
        df_Reformat_1, 
        "graph", 
        "LmVB9Tiv7gOksXKYvwwqv$$vRQhC-glg7Tz8vdDjYpL9", 
        "sEqrqRgL-8RgpQvmEL4qv$$oEdp_cRkhh3jJCtYi3j2w"
    )
    df_Subgraph_4 = Subgraph_4(spark, Config.Subgraph_4, df_dataproc_livy_src_annual_enterprise)
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
    df_SQLStatement_1_output_1.cache().count()
    df_SQLStatement_1_output_1.unpersist()
    df_Reformat_5 = Reformat_5(spark, df_SQLStatement_1_out1)
    df_Reformat_5 = collectMetrics(
                          spark, 
                          df_Reformat_5, 
                          "graph", 
                          "SAvIjpKonhri_rQm4i94P$$5PfK4KJufGSLrwml4L-L8", 
                          "VJ287DfF_Qxtn3OWXNo13$$jG9xvPkR2IRkOIlpqyUOq"
                        )\
                        .cache()
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
    df_RowDistributor_1_out0.cache().count()
    df_RowDistributor_1_out0.unpersist()
    df_RowDistributor_1_out1.cache().count()
    df_RowDistributor_1_out1.unpersist()
    df_SetOperation_1 = SetOperation_1(spark, df_Reformat_1, df_Reformat_1)
    df_SetOperation_1 = collectMetrics(
        spark, 
        df_SetOperation_1, 
        "graph", 
        "ZZMLx6qIPkco-6Lzn_Bkq$$W6J4G5WzbXaK0Ev-YvUcS", 
        "ISaF3Q4I-FudtVSXTdXHt$$6W-4kvVqiAX0YhO5TKPng"
    )
    df_pythonLivySG1_1 = pythonLivySG1_1(spark, Config.pythonLivySG1_1, df_SetOperation_1)
    df_pythonLivySG1_1.cache().count()
    df_pythonLivySG1_1.unpersist()
    df_Reformat_6 = Reformat_6(spark, df_dataproc_livy_src_annual_enterprise)
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
    df_Filter_1 = Filter_1(spark, df_SQLStatement_1_out2)
    df_Filter_1 = collectMetrics(
        spark, 
        df_Filter_1, 
        "graph", 
        "ffkpa2xcEAKQd_V9dtBkb$$cmhhOFAt_zkewnQTRJdl_", 
        "Vl3e150CwE1sSMZmmEx5q$$2E7cNVITsy5IcsyH8j1wB"
    )
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Livy_DataProc_Python")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Livy_DataProc_Python")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
