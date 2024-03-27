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
    val df_source_4 = source_4(context)
    val df_source_6 = source_6(context)
    target_6(context, df_source_6)
    target_3(context, df_source_4)
    val df_source_7 = source_7(context)
    target_7(context, df_source_7)
    val df_source_5 = source_5(context)
    target_5(context, df_source_5)
    val df_source_3 = source_3(context)
    target_4(context, df_source_3)
    val df_source_1 = source_1(context)
    val df_source_2 = source_2(context)
    target_2(context, df_source_2)
    target_1(context, df_source_1)
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
    val context = Context(spark, config)
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/FirstPipeline")
    registerUDFs(spark)
    MetricsCollector.instrument(spark, "pipelines/FirstPipeline") {
      apply(context)
    }
  }

}
