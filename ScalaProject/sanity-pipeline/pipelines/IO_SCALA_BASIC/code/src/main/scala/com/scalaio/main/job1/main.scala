package com.scalaio.main.job1

import io.prophecy.libs._
import com.scalaio.main.job1.config.Context
import com.scalaio.main.job1.config._
import com.scalaio.main.job1.config.ConfigStore.interimOutput
import com.scalaio.main.job1.udfs.UDFs._
import com.scalaio.main.job1.udfs._
import com.scalaio.main.job1.udfs.PipelineInitCode._
import com.scalaio.main.job1.graph._
import com.scalaio.main.job1.graph.Subgraph_1
import com.scalaio.main.job1.graph.Subgraph_3
import com.scalaio.main.job1.graph.Subgraph_1.config.{
  Context => Subgraph_1_Context
}
import com.scalaio.main.job1.graph.Subgraph_3.config.{
  Context => Subgraph_3_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def graph(context: Context): Unit = {
    val df_src_parquet_all_type_and_partition_withspacehyphens1 =
      src_parquet_all_type_and_partition_withspacehyphens1(context).interim(
        "graph",
        "o8K-lNobc6Z8Asi3dRegs$$Buw8lxPhFtSUcFZhGxXbx",
        "Yui765QKx0wOKHaOnjtzk$$Q04y-nxgyv0ZfORhocEUn"
      )
    val df_DONOT_DELETE =
      DONOT_DELETE(context,
                   df_src_parquet_all_type_and_partition_withspacehyphens1
      ).interim("graph",
                "q5SVopO_53zxCEzoNY5Bx$$oC2E7-fEqIbpRytDDI8gD",
                "0imhrueRm1jmWprDhzZ-2$$89rD5IveEoCrb2mL6-BxG"
      )
    df_DONOT_DELETE.cache().count()
    df_DONOT_DELETE.unpersist()
    val df_SQLStatement_1 =
      SQLStatement_1(context,
                     df_src_parquet_all_type_and_partition_withspacehyphens1
      ).interim("graph",
                "zTa3HjcrPr0ScL9QOW8BT$$M0QbyIk9v3R_9OpyenlDu",
                "1PGrDaLBabY__VcXs-VxW$$yrlYSve4Cnw5uVZQjLJpA"
      )
    df_SQLStatement_1.cache().count()
    df_SQLStatement_1.unpersist()
    val df_Reformat_1 = Reformat_1(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Reformat_11 = Reformat_11(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Reformat_2 = Reformat_2(context, df_Reformat_11).interim(
      "graph",
      "7iX5Km4rWd2sIuxVf3pPR$$VY9uAxZ16G3oqVipKV5-l",
      "i2byxsoj6BR7fn1u0Rd1I$$tFXZHl3W3CRLzjEG8M0U4"
    )
    df_Reformat_2.cache().count()
    df_Reformat_2.unpersist()
    val df_Subgraph_1 = Subgraph_1.apply(
      Subgraph_1_Context(context.spark, context.config.Subgraph_1),
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Subgraph_3 = Subgraph_3.apply(
      Subgraph_3_Context(context.spark, context.config.Subgraph_3),
      df_Subgraph_1
    )
    val df_Reformat_7 = Reformat_7(context, df_Subgraph_3).interim(
      "graph",
      "wuThqUc2qpf_FmJCMTj2e$$vhP6lu8CS3r_W42eJUyZ1",
      "H6Z_aAnftBpk4a-USAecW$$DfJIjJOqY8XnYd8OGH-ZP"
    )
    df_Reformat_7.cache().count()
    df_Reformat_7.unpersist()
    val df_Reformat_4 = Reformat_4(context, df_Reformat_1).interim(
      "graph",
      "Jsldsl3d5xD4SRjpdKI-Z$$DuCm45gqMbljkiKqBMQjw",
      "sPVo9omm0xwOufqyXCGI8$$F12AVA_FrP1_w296nytQb"
    )
    withSubgraphName("graph", context.spark) {
      withTargetId("dest_test", context.spark) {
        dest_test(context, df_Reformat_4)
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.getConfig(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
      .newSession()
    val context = Context(spark, config)
    MetricsCollector.initializeMetrics(spark)
    implicit val interimOutputConsole: InterimOutput = InterimOutputHive2("")
    spark.conf.set("prophecy.collect.basic.stats",          "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules",
                   "org.apache.spark.sql.catalyst.optimizer.ColumnPruning"
    )
    spark.conf.set("spark_config1",                  "spark_config_value_1")
    spark.conf.set("spark_config2",                  "spark_config_value_2")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/IO_SCALA_BASIC")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config1", "hadoop_config_value1")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config2",      "hadoop_config_value2")
    MetricsCollector.start(spark, "pipelines/IO_SCALA_BASIC")
    graph(context)
    MetricsCollector.end(spark)
  }

}
