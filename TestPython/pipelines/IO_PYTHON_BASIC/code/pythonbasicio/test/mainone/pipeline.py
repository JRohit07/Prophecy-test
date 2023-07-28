from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pythonbasicio.test.mainone.config.ConfigStore import *
from pythonbasicio.test.mainone.udfs.UDFs import *
from prophecy.utils import *
from pythonbasicio.test.mainone.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_special_char_column_name = src_csv_special_char_column_name(spark)
    df_src_csv_special_char_column_name = collectMetrics(
        spark, 
        df_src_csv_special_char_column_name, 
        "graph", 
        "vlcUd7KAM_zvifvMwu9pZ$$8MswNyzCALGAeJjSxRNDZ", 
        "CHZEgFOxU2vx1Q32ysboc$$LB9injlM6BGINFq1djzRE"
    )
    df_Reformat_1 = Reformat_1(spark, df_src_csv_special_char_column_name)
    df_Reformat_1 = collectMetrics(
        spark, 
        df_Reformat_1, 
        "graph", 
        "oSnCy6FWydBV675_CTMv8$$In5C4VfAlHsx5qLzItDuW", 
        "OgcPwunAgx_Y_Y3m8Krd0$$2IcX9S_gny3CS3TcShBZe"
    )
    df_Script_4 = Script_4(spark, df_Reformat_1)
    df_Script_4 = collectMetrics(
        spark, 
        df_Script_4, 
        "graph", 
        "Uooc3h8tVmdPw5lJv48-v$$8fU6UMC7OvanJjkndel2x", 
        "1DpbGVDq4gDguuxlp-FsI$$a6wwBFUElAoCP-OZd2Dyj"
    )
    df_Script_4.cache().count()
    df_Script_4.unpersist()
    df_DONOT_DELETE = DONOT_DELETE(spark, df_src_csv_special_char_column_name)
    df_DONOT_DELETE = collectMetrics(
        spark, 
        df_DONOT_DELETE, 
        "graph", 
        "QkILG1xdwXUxI1thdhnHs$$HX-nL8BicRrKIOLcVgxCK", 
        "13fvaMfG6O23PExl0wi9W$$UX6E4x_CAa5BY2z4I32uE"
    )
    df_DONOT_DELETE.cache().count()
    df_DONOT_DELETE.unpersist()
    df_Script_5 = Script_5(spark, df_src_csv_special_char_column_name)
    df_Reformat_3 = Reformat_3(spark, df_Script_5)
    df_Reformat_3 = collectMetrics(
        spark, 
        df_Reformat_3, 
        "graph", 
        "Z2MampB4oCcGewquXgPE1$$jta-gpnDuEhM598aJtDiT", 
        "CdFT_y4Eg_9ZqT8q7xG0q$$0DgBGM5ndnDRhNPCkYNI5"
    )
    df_Reformat_3.cache().count()
    df_Reformat_3.unpersist()
    dest_csv_py_io_only(spark, df_Reformat_1)

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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/IO_PYTHON_BASIC")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/IO_PYTHON_BASIC", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/IO_PYTHON_BASIC")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
