package io.prophecy.pipelines.testpipeline

import io.prophecy.libs._
import io.prophecy.pipelines.testpipeline.config.Context
import io.prophecy.pipelines.testpipeline.config._
import io.prophecy.pipelines.testpipeline.udfs.UDFs._
import io.prophecy.pipelines.testpipeline.udfs._
import io.prophecy.pipelines.testpipeline.udfs.PipelineInitCode._
import io.prophecy.pipelines.testpipeline.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_test = test(context)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/TestPipeline")
    registerUDFs(spark)
    try MetricsCollector.start(spark, "pipelines/TestPipeline", context.config)
    catch {
      case _: Throwable =>
        MetricsCollector.start(spark, "pipelines/TestPipeline")
    }
    apply(context)
    MetricsCollector.end(spark)
  }

}
