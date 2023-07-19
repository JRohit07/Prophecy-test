package io.prophecy.pipelines.livy_scala

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.config.Context
import io.prophecy.pipelines.livy_scala.config._
import io.prophecy.pipelines.livy_scala.udfs.UDFs._
import io.prophecy.pipelines.livy_scala.udfs._
import io.prophecy.pipelines.livy_scala.udfs.PipelineInitCode._
import io.prophecy.pipelines.livy_scala.graph._
import io.prophecy.pipelines.livy_scala.graph.Subgraph_4
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1
import io.prophecy.pipelines.livy_scala.graph.Subgraph_4.config.{
  Context => Subgraph_4_Context
}
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.config.{
  Context => livyscalaSG1_1_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_livy_src_csv = livy_src_csv(context)
    Lookup_1(context, df_livy_src_csv)
    val df_Reformat_1 = Reformat_1(context, df_livy_src_csv)
    val df_Subgraph_4 = Subgraph_4.apply(
      Subgraph_4_Context(context.spark, context.config.Subgraph_4),
      df_livy_src_csv
    )
    val (df_SQLStatement_1_out,
         df_SQLStatement_1_out1,
         df_SQLStatement_1_out2,
         df_SQLStatement_1_out3
    )                 = SQLStatement_1(context, df_Subgraph_4)
    val df_Reformat_2 = Reformat_2(context,     df_SQLStatement_1_out)
    val df_Reformat_3 = Reformat_3(context,     df_livy_src_csv).cache()
    val df_PassThrough =
      if (!(context.config.c_int > -1001)) PassThrough(context, df_Reformat_3)
      else df_Reformat_3
    val (df_RowDistributor_1_out0, df_RowDistributor_1_out1) = {
      val (df_RowDistributor_1_out0_temp, df_RowDistributor_1_out1_temp) =
        RowDistributor_1(context, df_Subgraph_4)
      (df_RowDistributor_1_out0_temp.cache(),
       df_RowDistributor_1_out1_temp.cache()
      )
    }
    val df_Reformat_5        = Reformat_5(context,        df_RowDistributor_1_out0)
    val df_SchemaTransform_1 = SchemaTransform_1(context, df_Reformat_5).cache()
    val df_Reformat_4        = Reformat_4(context,        df_SchemaTransform_1)
    val df_OrderBy_1         = OrderBy_1(context,         df_SQLStatement_1_out2).cache()
    val df_SetOperation_1 =
      SetOperation_1(context, df_Reformat_1, df_Reformat_1)
    val df_livyscalaSG1_1 = livyscalaSG1_1.apply(
      livyscalaSG1_1_Context(context.spark, context.config.livyscalaSG1_1),
      df_SetOperation_1
    )
    val df_Script_1   = Script_1(context,   df_livyscalaSG1_1)
    val df_Reformat_6 = Reformat_6(context, df_Script_1)
    val df_Filter_1   = Filter_1(context,   df_SQLStatement_1_out1)
    Script_2(context, df_SQLStatement_1_out3)
    val df_FlattenSchema_1  = FlattenSchema_1(context,  df_Reformat_3)
    val df_Join_1           = Join_1(context,           df_SetOperation_1, df_Reformat_1)
    val df_Reformat_7       = Reformat_7(context,       df_livy_src_csv)
    val df_Filter_2         = Filter_2(context,         df_RowDistributor_1_out1)
    val df_Aggregate_1      = Aggregate_1(context,      df_Filter_1)
    val df_Reformat_9       = Reformat_9(context,       df_PassThrough)
    val df_WindowFunction_1 = WindowFunction_1(context, df_OrderBy_1)
    val df_Deduplicate_1    = Deduplicate_1(context,    df_Filter_2)
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
    spark.conf.set("spark.sql.optimizer.excludedRules",
                   "org.apache.spark.sql.catalyst.optimizer.ColumnPruning"
    )
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/LIVY_SCALA")
    registerUDFs(spark)
    MetricsCollector.start(spark, "pipelines/LIVY_SCALA")
    apply(context)
    MetricsCollector.end(spark)
  }

}
