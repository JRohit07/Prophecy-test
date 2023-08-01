package io.prophecy.pipelines.perf_unitest_generate

import io.prophecy.libs._
import io.prophecy.pipelines.perf_unitest_generate.config.ConfigStore._
import io.prophecy.pipelines.perf_unitest_generate.config.Context
import io.prophecy.pipelines.perf_unitest_generate.config._
import io.prophecy.pipelines.perf_unitest_generate.udfs.UDFs._
import io.prophecy.pipelines.perf_unitest_generate.udfs._
import io.prophecy.pipelines.perf_unitest_generate.graph._
import io.prophecy.pipelines.perf_unitest_generate.graph.Subgraph_1
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_src_json_input_custs = src_json_input_custs(context)
    Lookup_1(context, df_src_json_input_custs)
    val df_SchemaTransform_1 =
      SchemaTransform_1(context, df_src_json_input_custs)
    val df_Aggregate_1 = Aggregate_1(context, df_SchemaTransform_1)
    val df_Limit_1     = Limit_1(context,     df_Aggregate_1)
    val (df_RowDistributor_1_out0, df_RowDistributor_1_out1) =
      RowDistributor_1(context, df_Limit_1)
    val df_SQLStatement_1   = SQLStatement_1(context,   df_RowDistributor_1_out1)
    val df_Reformat_1       = Reformat_1(context,       df_src_json_input_custs)
    val df_Filter_1         = Filter_1(context,         df_Reformat_1)
    val df_OrderBy_1        = OrderBy_1(context,        df_Filter_1)
    val df_SetOperation_1   = SetOperation_1(context,   df_OrderBy_1,     df_OrderBy_1)
    val df_WindowFunction_1 = WindowFunction_1(context, df_SchemaTransform_1)
    val df_Repartition_1    = Repartition_1(context,    df_RowDistributor_1_out0)
    val df_Script_1         = Script_1(context,         df_Repartition_1)
    val df_FlattenSchema_1  = FlattenSchema_1(context,  df_src_json_input_custs)
    val df_Subgraph_1       = Subgraph_1.apply(context, df_SQLStatement_1)
    val df_Deduplicate_1    = Deduplicate_1(context,    df_SetOperation_1)
    val df_Join_1           = Join_1(context,           df_Deduplicate_1, df_Deduplicate_1)
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.fromCLI(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
      .newSession()
    val context = Context(spark, config)
    spark.conf.set("prophecy.metadata.pipeline.uri",
                   "pipelines/CloneUTGenerate_PerfPipeline"
    )
    MetricsCollector.start(spark, "pipelines/CloneUTGenerate_PerfPipeline")
    apply(context)
    MetricsCollector.end(spark)
  }

}
