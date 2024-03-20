package io.prophecy.pipelines.firstpipeline

import io.prophecy.libs._
import io.prophecy.pipelines.firstpipeline.config._
import io.prophecy.pipelines.firstpipeline.udfs.UDFs._
import io.prophecy.pipelines.firstpipeline.udfs.PipelineInitCode._
import io.prophecy.pipelines.firstpipeline.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_source6       = source6(context)
    val df_JDBC_SOURCE_2 = JDBC_SOURCE_2(context)
    TARGET_2(context, df_JDBC_SOURCE_2)
    val df_JDBC_Gem_source_1 = JDBC_Gem_source_1(context)
    val df_source_7          = source_7(context)
    jdbc_write_to_test_table_1(context, df_source6)
    val df_source_4 = source_4(context)
    target_3(context, df_source_4)
    val df_jdbc_table_reader = jdbc_table_reader(context)
    target_4(context,                 df_jdbc_table_reader)
    jdbc_write_to_test_table(context, df_JDBC_Gem_source_1)
    target_7(context,                 df_source_7)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/FirstPipeline")
    registerUDFs(spark)
    try MetricsCollector.start(spark, "pipelines/FirstPipeline", context.config)
    catch {
      case _: Throwable =>
        MetricsCollector.start(spark, "pipelines/FirstPipeline")
    }
    apply(context)
    MetricsCollector.end(spark)
  }

}
