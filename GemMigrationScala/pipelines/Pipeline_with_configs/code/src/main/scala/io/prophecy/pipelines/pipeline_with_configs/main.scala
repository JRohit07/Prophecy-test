package io.prophecy.pipelines.pipeline_with_configs

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline_with_configs.config._
import io.prophecy.pipelines.pipeline_with_configs.udfs.UDFs._
import io.prophecy.pipelines.pipeline_with_configs.udfs.PipelineInitCode._
import io.prophecy.pipelines.pipeline_with_configs.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_source_1   = source_1(context)
    val df_jdbc_fixed = jdbc_fixed(context)
    target_1_1(context, df_jdbc_fixed)
    val df_source_1_1 = source_1_1(context)
    target_1_2(context, df_source_1_1)
    target_1(context,   df_source_1)
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
    spark.conf
      .set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline_with_configs")
    registerUDFs(spark)
    MetricsCollector.instrument(spark, "pipelines/Pipeline_with_configs") {
      apply(context)
    }
  }

}
