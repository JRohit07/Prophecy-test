package com.scala.main.job1

import io.prophecy.libs._
import com.scala.main.job1.config.Context
import com.scala.main.job1.config._
import com.scala.main.job1.udfs.UDFs._
import com.scala.main.job1.udfs._
import com.scala.main.job1.udfs.PipelineInitCode._
import com.scala.main.job1.graph._
import com.scala.main.job1.graph.Subgraph_1
import com.scala.main.job1.graph.Subgraph_3
import com.scala.main.job1.graph.Subgraph_1.config.{
  Context => Subgraph_1_Context
}
import com.scala.main.job1.graph.Subgraph_3.config.{
  Context => Subgraph_3_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_src_parquet_all_type_and_partition_withspacehyphens1 =
      src_parquet_all_type_and_partition_withspacehyphens1(context)
    val (df_RowDistributor_1_out0, df_RowDistributor_1_out1) =
      if (!(context.config.c_test == "tesdasdasdasdasdasst")) {
        val df_SQLStatement_1 =
          if (!(context.config.c_test == "tesdasdasdasdasdasst"))
            SQLStatement_1(
              context,
              df_src_parquet_all_type_and_partition_withspacehyphens1
            ).cache()
          else df_src_parquet_all_type_and_partition_withspacehyphens1
        RowDistributor_1(context, df_SQLStatement_1)
      } else
        (null, null)
    val df_Join_1 = if (
      !(context.config.c_test == "tesdasdasdasdasdasst" || context.config.c_test == "tesdasdasdasdasdasst")
    )
      Join_1(context, df_RowDistributor_1_out0, df_RowDistributor_1_out1)
    else null
    val df_OrderBy_1 = if (
      !(context.config.c_test == "tesdasdasdasdasdasst" || context.config.c_test == "tesdasdasdasdasdasst")
    ) {
      val df_Reformat_2 = Reformat_2(context, df_Join_1)
      OrderBy_1(context, df_Reformat_2)
    } else
      null
    val df_Filter_1 = if (
      !(context.config.c_test == "tesdasdasdasdasdasst" || context.config.c_test == "tesdasdasdasdasdasst")
    ) {
      val df_Passthrough =
        if (!(context.config.c_test != "test"))
          Passthrough(context, df_OrderBy_1)
        else df_OrderBy_1
      Filter_1(context, df_Passthrough)
    } else
      null
    val df_Reformat_1 = Reformat_1(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Subgraph_1 = Subgraph_1.apply(
      Subgraph_1_Context(context.spark, context.config.Subgraph_1),
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Subgraph_3 = Subgraph_3.apply(
      Subgraph_3_Context(context.spark, context.config.Subgraph_3),
      df_Subgraph_1
    )
    val df_Reformat_7 = Reformat_7(context, df_Subgraph_3).cache()
    val df_Reformat_11 =
      Reformat_11(context,
                  df_src_parquet_all_type_and_partition_withspacehyphens1
      ).cache()
    val df_OrderBy_1_1 = if (
      !(context.config.c_test == "tesdasdasdasdasdasst" || context.config.c_test == "tesdasdasdasdasdasst" || context.config.c_test != "test")
    ) {
      val df_Removal = Removal(context, df_Join_1)
      OrderBy_1_1(context, df_Removal)
    } else
      null
    val df_Reformat_4 = Reformat_4(context, df_Reformat_1)
    dest_test(context, df_Reformat_4)
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
    spark.conf.set("spark_config1", "spark_config_value_1")
    spark.conf.set("spark_config2", "spark_config_value_2")
    spark.conf.set("prophecy.metadata.pipeline.uri",
                   "pipelines/EM_DISABLED_SCALA_BASIC"
    )
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config1", "hadoop_config_value1")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config2", "hadoop_config_value2")
    registerUDFs(spark)
    MetricsCollector.start(spark, "pipelines/EM_DISABLED_SCALA_BASIC")
    apply(context)
    MetricsCollector.end(spark)
  }

}
