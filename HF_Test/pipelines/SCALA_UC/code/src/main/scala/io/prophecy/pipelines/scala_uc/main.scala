package io.prophecy.pipelines.scala_uc

import io.prophecy.libs._
import io.prophecy.pipelines.scala_uc.config.Context
import io.prophecy.pipelines.scala_uc.config._
import io.prophecy.pipelines.scala_uc.udfs.UDFs._
import io.prophecy.pipelines.scala_uc.udfs._
import io.prophecy.pipelines.scala_uc.udfs.PipelineInitCode._
import io.prophecy.pipelines.scala_uc.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_src_parquet_unity_catalog = src_parquet_unity_catalog(context)
    val df_Reformat_1                = Reformat_1(context, df_src_parquet_unity_catalog)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SCALA_UC")
    registerUDFs(spark)
    try MetricsCollector.start(spark, "pipelines/SCALA_UC", context.config)
    catch {
      case _: Throwable =>
        MetricsCollector.start(spark, "pipelines/SCALA_UC")
    }
    apply(context)
    MetricsCollector.end(spark)
  }

}
