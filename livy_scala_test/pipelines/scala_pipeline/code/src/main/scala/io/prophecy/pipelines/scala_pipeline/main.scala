package io.prophecy.pipelines.scala_pipeline

import io.prophecy.libs._
import io.prophecy.pipelines.scala_pipeline.config.Context
import io.prophecy.pipelines.scala_pipeline.config._
import io.prophecy.pipelines.scala_pipeline.udfs.UDFs._
import io.prophecy.pipelines.scala_pipeline.udfs._
import io.prophecy.pipelines.scala_pipeline.udfs.PipelineInitCode._
import io.prophecy.pipelines.scala_pipeline.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_customer_dataset = customer_dataset(context)
    val df_Reformat_1       = Reformat_1(context, df_customer_dataset)
    val df_Limit_1          = Limit_1(context,    df_Reformat_1)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/scala_pipeline")
    registerUDFs(spark)
    try MetricsCollector.start(spark,
                               "pipelines/scala_pipeline",
                               context.config
    )
    catch {
      case _: Throwable =>
        MetricsCollector.start(spark, "pipelines/scala_pipeline")
    }
    apply(context)
    MetricsCollector.end(spark)
  }

}
