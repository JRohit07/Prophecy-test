package io.prophecy.pipelines.pipeline_first

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_first.config._
import io.prophecy.pipelines.pipeline_first.udfs.UDFs._
import io.prophecy.pipelines.pipeline_first.udfs.PipelineInitCode._
import io.prophecy.pipelines.pipeline_first.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_source_2 = source_2(context)
    target_2(context, df_source_2)
    val df_source_4 = source_4(context)
    val df_source_1 = source_1(context)
    target_1(context, df_source_1)
    target_4(context, df_source_4)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipline_first")
    registerUDFs(spark)
    try MetricsCollector.start(spark, "pipelines/Pipline_first", context.config)
    catch {
      case _: Throwable =>
        MetricsCollector.start(spark, "pipelines/Pipline_first")
    }
    apply(context)
    MetricsCollector.end(spark)
  }

}
