package io.prophecy.pipelines.pip1

import io.prophecy.libs._
import io.prophecy.pipelines.pip1.config._
import io.prophecy.pipelines.pip1.functions.UDFs._
import io.prophecy.pipelines.pip1.functions.PipelineInitCode._
import io.prophecy.pipelines.pip1.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_fgdfg            = fgdfg(context)
    val df_reformat_columns = reformat_columns(context, df_fgdfg)
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.getConfig(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Pip1")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
    val context = Context(spark, config)
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pip1")
    registerUDFs(spark)
    MetricsCollector.instrument(spark, "pipelines/Pip1") {
      apply(context)
    }
  }

}
