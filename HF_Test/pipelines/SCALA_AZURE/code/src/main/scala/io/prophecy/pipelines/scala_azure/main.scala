package io.prophecy.pipelines.scala_azure

import io.prophecy.libs._
import io.prophecy.pipelines.scala_azure.config.Context
import io.prophecy.pipelines.scala_azure.config._
import io.prophecy.pipelines.scala_azure.config.ConfigStore.interimOutput
import io.prophecy.pipelines.scala_azure.udfs.UDFs._
import io.prophecy.pipelines.scala_azure.udfs._
import io.prophecy.pipelines.scala_azure.udfs.PipelineInitCode._
import io.prophecy.pipelines.scala_azure.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def graph(context: Context): Unit = {
    val df_src_azure = src_azure(context).interim(
      "graph",
      "g8vlGiSReidxau317o1CM$$LiP-pUUs_VAmJKrGV-4b8",
      "L0PT63aDke-uUpajUBEUw$$pk4-M8i_RKccxMqJKj-sD"
    )
    val df_Reformat_1 = Reformat_1(context, df_src_azure).interim(
      "graph",
      "CPZCbIbM4XggVOSp0Dx8x$$mXRH2I1gL17lBQP48QMdE",
      "jz4MLCfDnpkFwiJqbOmU4$$z7vTGA6xPenzdlbBurLa_"
    )
    df_Reformat_1.cache().count()
    df_Reformat_1.unpersist()
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
    MetricsCollector.initializeMetrics(spark)
    implicit val interimOutputConsole: InterimOutput = InterimOutputHive2("")
    spark.conf.set("prophecy.collect.basic.stats",          "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules",
                   "org.apache.spark.sql.catalyst.optimizer.ColumnPruning"
    )
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SCALA_AZURE")
    MetricsCollector.start(spark,                    "pipelines/SCALA_AZURE")
    graph(context)
    MetricsCollector.end(spark)
  }

}
