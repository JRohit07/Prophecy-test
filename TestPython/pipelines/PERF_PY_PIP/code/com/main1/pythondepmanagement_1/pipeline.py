from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from com.main1.pythondepmanagement_1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_PERF_2k_COLS = PERF_2k_COLS(spark)
    df_PERF_2k_COLS = collectMetrics(
        spark, 
        df_PERF_2k_COLS, 
        "graph", 
        "of9dwhtl9scobjEwxsOSW$$RvYbitqWb_IuA8Vdu3_u9", 
        "WBfgTX7MYUVrikEutfz2a$$dSjIhcuUJCIJ_A0ytwyE0"
    )
    df_REFORMAT_TES = REFORMAT_TES(spark, df_PERF_2k_COLS)
    df_REFORMAT_TES = collectMetrics(
        spark, 
        df_REFORMAT_TES, 
        "graph", 
        "8hewuyAVIhPHnqq2_XMqg$$pXQKzKEN9SaDhH7jhDbm8", 
        "xUk9SuXYD1FlJeprz8FLM$$s0-hc2ynRhztlRgH79B-M"
    )
    df_PERF_REFORMAT = PERF_REFORMAT(spark, df_REFORMAT_TES)
    df_PERF_REFORMAT = collectMetrics(
        spark, 
        df_PERF_REFORMAT, 
        "graph", 
        "q-KlzXOoYEb4f7C-umZ4c$$6GWsc-CZFQvOEHhD9DQXT", 
        "Z0Ug8QUgP4r35za26e7iT$$2F7Lr7Dgus2nnS7yLljsL"
    )
    df_PERF_FILTER = PERF_FILTER(spark, df_PERF_REFORMAT)
    df_PERF_FILTER = collectMetrics(
        spark, 
        df_PERF_FILTER, 
        "graph", 
        "6EL1Nr9NeffENBmKtitSB$$c2iFw-Yo9hYqVrOMrW4EL", 
        "TqDE3Z3hrgSO36_YFr6-M$$wqzaG9E9hohCLerPEDLLK"
    )
    df_PERF_ORDERBY = PERF_ORDERBY(spark, df_PERF_FILTER)
    df_PERF_ORDERBY = collectMetrics(
        spark, 
        df_PERF_ORDERBY, 
        "graph", 
        "CwnOBwh7qWOUEmBkeTMSz$$RfCr5p0M0qMwJvgFD33--", 
        "dHa8ELWbm8nI5k7TZze_z$$KdqOQ1oc2Z7fyUwG0jQ5c"
    )
    df_PERF_SET = PERF_SET(spark, df_PERF_ORDERBY, df_PERF_ORDERBY)
    df_PERF_SET = collectMetrics(
        spark, 
        df_PERF_SET, 
        "graph", 
        "DhmpmWudLKd-hrMHOmh1q$$3htFu-6FRSU0bVVmY3hmC", 
        "MBIxOe9fG2Dy-b7Ctck0F$$MqBhdWhpsYLCvTVEu_0tP"
    )
    df_PERF_SCHEMATRANSFORM = PERF_SCHEMATRANSFORM(spark, df_PERF_SET)
    df_PERF_SCHEMATRANSFORM = collectMetrics(
        spark, 
        df_PERF_SCHEMATRANSFORM, 
        "graph", 
        "aMwVy0sLbCI4FzLBdnYfq$$XEp60Db3fnm-ayrqGktls", 
        "4nUTOLxwzhRBKJ1r6Kk1-$$SB_kvLBuM-3tLT2RaJRGE"
    )
    df_PERF_LIMIT = PERF_LIMIT(spark, df_PERF_SCHEMATRANSFORM)
    df_PERF_LIMIT = collectMetrics(
        spark, 
        df_PERF_LIMIT, 
        "graph", 
        "dn-ht0jhfT6HhGEvo-t24$$sXpacbzyjJpnpvdOCafqd", 
        "DNHdy6Od4MZqsWmlytfQw$$5OwivSlzx10JmtiDraGrQ"
    )
    df_PERF_DEDUPLICATE = PERF_DEDUPLICATE(spark, df_PERF_LIMIT)
    df_PERF_DEDUPLICATE = collectMetrics(
        spark, 
        df_PERF_DEDUPLICATE, 
        "graph", 
        "Ypy8pKKGA9NUlK-HBUnIm$$RBHm52baqXaeBg1z_Q2CS", 
        "b4P4jafjXKIYnZp5ZWmFG$$VuzcbGDa8d55Q_Lim54gM"
    )
    df_PERF_DEDUPLICATE.cache().count()
    df_PERF_DEDUPLICATE.unpersist()
    df_PERF_ROWDISTRIBUTOR_out0, df_PERF_ROWDISTRIBUTOR_out1 = PERF_ROWDISTRIBUTOR(spark, df_PERF_REFORMAT)
    df_PERF_ROWDISTRIBUTOR_out0 = collectMetrics(
        spark, 
        df_PERF_ROWDISTRIBUTOR_out0, 
        "graph", 
        "aKdeRS8Sl0uOlIcZgbSEb$$nvVMssPCT7TR17UvES-aI", 
        "U7X15Ecr3OrBiJC9r0v3G$$jT2XjhLYS7vlxHcdtBPbF"
    )
    df_PERF_ROWDISTRIBUTOR_out1 = collectMetrics(
        spark, 
        df_PERF_ROWDISTRIBUTOR_out1, 
        "graph", 
        "aKdeRS8Sl0uOlIcZgbSEb$$nvVMssPCT7TR17UvES-aI", 
        "aHT7Tnu6uSy-2N6MQoPWQ$$Os6GT1kCs0guxSxyyoEMl"
    )
    df_PERF_SCRIPT = PERF_SCRIPT(spark, df_PERF_ROWDISTRIBUTOR_out1)
    df_PERF_SCRIPT = collectMetrics(
        spark, 
        df_PERF_SCRIPT, 
        "graph", 
        "x59392gAoQqX953fQPEbW$$6FZGeVP6TsShn4IhpUJag", 
        "24y4VBSGA3nSihSi4nEcZ$$xExsxhE3VaFzD9xAed8QB"
    )
    df_PERF_SCRIPT.cache().count()
    df_PERF_SCRIPT.unpersist()
    df_PERF_WINDOWFUNCTION = PERF_WINDOWFUNCTION(spark, df_PERF_2k_COLS)
    df_PERF_WINDOWFUNCTION = collectMetrics(
        spark, 
        df_PERF_WINDOWFUNCTION, 
        "graph", 
        "tNTURQXfUkyZS_UErD-t6$$V-zragh82Vs17fXETCIUn", 
        "i2ujs5HoUbGO4xSjDBG01$$0yzM0EYq8O4ZQWz2QIWEo"
    )
    df_PERF_WINDOWFUNCTION.cache().count()
    df_PERF_WINDOWFUNCTION.unpersist()
    df_PERF_AGGREGATE = PERF_AGGREGATE(spark, df_PERF_2k_COLS)
    df_PERF_AGGREGATE = collectMetrics(
        spark, 
        df_PERF_AGGREGATE, 
        "graph", 
        "cCwlYI7F2pAkIPVH2dnfh$$wYAxBDWqdbV-PHeHDKxEB", 
        "aMhDDCoghYJLeTzK8zMDm$$-uWH4yYhQUdbkmJSg3wQN"
    )
    df_PERF_AGGREGATE.cache().count()
    df_PERF_AGGREGATE.unpersist()
    df_PERF_JOIN = PERF_JOIN(spark, df_PERF_LIMIT, df_PERF_LIMIT)
    df_PERF_JOIN = collectMetrics(
        spark, 
        df_PERF_JOIN, 
        "graph", 
        "LrRRvah3um1f9aGvRr86k$$2m1sNfIBsPN-DuIX54s8A", 
        "0frmKeMnZUhdRbiQ08Bjg$$-e4G03HAeiaqTLpoi1CVw"
    )
    df_PERF_JOIN.cache().count()
    df_PERF_JOIN.unpersist()
    df_PERF_FLATTENSCHEMA = PERF_FLATTENSCHEMA(spark, df_PERF_2k_COLS)
    df_PERF_FLATTENSCHEMA = collectMetrics(
        spark, 
        df_PERF_FLATTENSCHEMA, 
        "graph", 
        "nWbQO-1VgZqvuKnmT8Ch5$$WclK_BLwUTnqWu-79Cl2q", 
        "RVHPUSmmtFtuq4XkXamtA$$OO58O-eyaR41w1OD7mdG4"
    )
    df_PERF_FLATTENSCHEMA.cache().count()
    df_PERF_FLATTENSCHEMA.unpersist()
    df_PERF_SG_out0, df_PERF_SG_out1, df_PERF_SG_out2 = PERF_SG(
        spark, 
        Config.PERF_SG, 
        df_REFORMAT_TES, 
        df_REFORMAT_TES, 
        df_REFORMAT_TES
    )
    df_PERF_SG_out0.cache().count()
    df_PERF_SG_out0.unpersist()
    df_PERF_SG_out1.cache().count()
    df_PERF_SG_out1.unpersist()
    df_PERF_SG_out2.cache().count()
    df_PERF_SG_out2.unpersist()
    df_PERF_SQLSTATEMENT = PERF_SQLSTATEMENT(spark, df_PERF_ROWDISTRIBUTOR_out0)
    df_PERF_SQLSTATEMENT = collectMetrics(
        spark, 
        df_PERF_SQLSTATEMENT, 
        "graph", 
        "q42Kc4QTbu125Z60TYmXK$$22MiOue51XZ1hD4CJrXYY", 
        "GROWkLIgSvUSY99pYYk47$$4u3QcWGFfimfKzSeo7A6R"
    )
    df_PERF_SQLSTATEMENT.cache().count()
    df_PERF_SQLSTATEMENT.unpersist()

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
    spark.conf.set("spark_config1", "spark_config1 value")
    spark.conf.set("spark_config2", "spark_config2 value")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PERF_PY_PIP")
    spark.sparkContext._jsc.hadoopConfiguration().set("hadoop_config1", "hadoop_config1 value")
    spark.sparkContext._jsc.hadoopConfiguration().set("hadoop_config2", "hadoop_config2 value")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PERF_PY_PIP")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
