package io.prophecy.pipelines.newpipeline

import io.prophecy.libs._
import io.prophecy.pipelines.newpipeline.config.Context
import io.prophecy.pipelines.newpipeline.config._
import io.prophecy.pipelines.newpipeline.udfs.UDFs._
import io.prophecy.pipelines.newpipeline.udfs._
import io.prophecy.pipelines.newpipeline.udfs.PipelineInitCode._
import io.prophecy.pipelines.newpipeline.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    Lookup_0_2(context)
    Lookup_0(context)
    Lookup_0_1(context)
    val df_Deduplicate_1 = Deduplicate_1(context)
    val (df_DataValidator_1_2_out0, df_DataValidator_1_2_out1) =
      DataValidator_1_2(context)
    val df_Deduplicate_1_1 = Deduplicate_1_1(context)
    val (df_DataValidator_1_1_out0, df_DataValidator_1_1_out1) =
      DataValidator_1_1(context)
    val df_Deduplicate_1_2 = Deduplicate_1_2(context)
    val (df_DataValidator_1_out0, df_DataValidator_1_out1) = DataValidator_1(
      context
    )
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/NewPipeline")
    registerUDFs(spark)
    try MetricsCollector.start(spark, "pipelines/NewPipeline", context.config)
    catch {
      case _: Throwable =>
        MetricsCollector.start(spark, "pipelines/NewPipeline")
    }
    apply(context)
    MetricsCollector.end(spark)
  }

}
