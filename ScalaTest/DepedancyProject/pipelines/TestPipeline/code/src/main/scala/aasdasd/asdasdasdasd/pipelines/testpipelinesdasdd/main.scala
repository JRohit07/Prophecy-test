package aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd

import io.prophecy.libs._
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.config.Context
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.config._
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.udfs.UDFs._
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.udfs._
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.udfs.PipelineInitCode._
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.graph._
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
