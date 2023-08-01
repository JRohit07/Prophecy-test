package io.prophecy.pipelines.scinterimsdatabrickspipeline

import io.prophecy.libs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config.Context
import io.prophecy.pipelines.scinterimsdatabrickspipeline.config._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.udfs.UDFs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.udfs._
import io.prophecy.pipelines.scinterimsdatabrickspipeline.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_src_databricks_livy_csv = src_databricks_livy_csv(context)
    val df_SQLStatement_2          = SQLStatement_2(context, df_src_databricks_livy_csv)
    Lookup_1(context, df_SQLStatement_2)
    val df_SQLStatement_2_1 =
      SQLStatement_2_1(context, df_src_databricks_livy_csv)
    val df_Reformat_1_3_3   = Reformat_1_3_3(context,   df_SQLStatement_2_1)
    val df_WindowFunction_2 = WindowFunction_2(context, df_Reformat_1_3_3)
    val df_Filter_3         = Filter_3(context,         df_WindowFunction_2)
    Lookup_1_1_1(context, df_Filter_3)
    val df_src_csv_2_3_1 = src_csv_2_3_1(context)
    Lookup_1_1(context, df_src_csv_2_3_1)
    val df_src_csv_2_3_2_1_1 = src_csv_2_3_2_1_1(context)
    val df_Reformat_1_3_3_1_1_1 =
      Reformat_1_3_3_1_1_1(context, df_src_csv_2_3_2_1_1)
    val df_SchemaTransform_1_2_1 =
      SchemaTransform_1_2_1(context, df_Reformat_1_3_3_1_1_1)
    val df_Filter_4_2_1       = Filter_4_2_1(context,       df_SchemaTransform_1_2_1)
    val df_Reformat_1_3_1     = Reformat_1_3_1(context,     df_Filter_4_2_1)
    val df_Filter_4_1_1_1     = Filter_4_1_1_1(context,     df_Reformat_1_3_1)
    val df_Reformat_1_2_1     = Reformat_1_2_1(context,     df_Filter_4_1_1_1)
    val df_src_csv_2_3_2_1    = src_csv_2_3_2_1(context)
    val df_Reformat_1_3_3_1_1 = Reformat_1_3_3_1_1(context, df_src_csv_2_3_2_1)
    val df_SchemaTransform_1_2 =
      SchemaTransform_1_2(context, df_Reformat_1_3_3_1_1)
    val df_Filter_4_2        = Filter_4_2(context,        df_SchemaTransform_1_2)
    val df_Reformat_1_3      = Reformat_1_3(context,      df_Filter_4_2)
    val df_src_csv_2_3_2     = src_csv_2_3_2(context)
    val df_Reformat_1_3_3_1  = Reformat_1_3_3_1(context,  df_src_csv_2_3_2)
    val df_SchemaTransform_1 = SchemaTransform_1(context, df_Reformat_1_3_3_1)
    val df_Filter_4          = Filter_4(context,          df_SchemaTransform_1)
    val df_Reformat_1        = Reformat_1(context,        df_Filter_4)
    val df_SetOperation_2_1 =
      SetOperation_2_1(context, df_Reformat_1, df_Reformat_1_3)
    val df_Filter_4_1_1 = Filter_4_1_1(context, df_SetOperation_2_1)
    val df_Script_3     = Script_3(context,     df_Filter_4_1_1)
    val df_SetOperation_2_1_1 =
      SetOperation_2_1_1(context, df_Script_3, df_Reformat_1_2_1)
    val df_Filter_5_1     = Filter_5_1(context,     df_SetOperation_2_1_1)
    val df_Reformat_5_2   = Reformat_5_2(context,   df_Filter_5_1)
    val df_csv_dataset    = csv_dataset(context)
    val df_Reformat_5_2_1 = Reformat_5_2_1(context, df_csv_dataset)
    val df_Reformat_5_2_2 = Reformat_5_2_2(context, df_Reformat_5_2_1)
    val df_SetOperation_1 =
      SetOperation_1(context, df_Reformat_5_2, df_Reformat_5_2_2)
    val df_Aggregate_2 = Aggregate_2(context, df_SetOperation_1)
    val df_Reformat_7  = Reformat_7(context,  df_Aggregate_2)
    target_dataset(context, df_Reformat_7)
    val df_SetOperation_2 =
      SetOperation_2(context, df_Reformat_1, df_Reformat_1_3, df_Reformat_1_3_1)
    val df_Filter_4_1        = Filter_4_1(context,        df_SetOperation_2)
    val df_Reformat_1_2      = Reformat_1_2(context,      df_Filter_4_1)
    val df_Aggregate_1       = Aggregate_1(context,       df_Reformat_1_2)
    val df_Reformat_4        = Reformat_4(context,        df_Aggregate_1)
    val df_Reformat_3        = Reformat_3(context,        df_Reformat_4)
    val df_SchemaTransform_3 = SchemaTransform_3(context, df_Reformat_3)
    val df_Script_2          = Script_2(context,          df_SchemaTransform_3)
    val df_SchemaTransform_2 = SchemaTransform_2(context, df_Filter_4_1)
    val df_Reformat_2        = Reformat_2(context,        df_Filter_4_1_1)
    val df_Script_12_1       = Script_12_1(context)
    val df_Script_12         = Script_12(context)
    val df_Script_3_1        = Script_3_1(context,        df_Script_12)
    val df_Script_7          = Script_7(context,          df_Script_3_1)
    val (df_Script_9_out0, df_Script_9_out1, df_Script_9_out2) =
      Script_9(context, df_Script_12_1, df_Script_7)
    val df_Filter_1       = Filter_1(context,       df_Reformat_3)
    val df_Limit_2        = Limit_2(context,        df_Filter_1)
    val df_OrderBy_1      = OrderBy_1(context,      df_Filter_1)
    val df_SQLStatement_1 = SQLStatement_1(context, df_OrderBy_1)
    val df_Reformat_6_2   = Reformat_6_2(context,   df_Filter_4_1)
    target_dataset_1_1_1(context, df_Reformat_6_2)
    val df_Join_1 = Join_1(context, df_Reformat_2, df_Reformat_2)
    val (df_RowDistributor_1_out0, df_RowDistributor_1_out1) =
      RowDistributor_1(context, df_Join_1)
    val df_Limit_1       = Limit_1(context,       df_RowDistributor_1_out0)
    val df_Repartition_1 = Repartition_1(context, df_Limit_1)
    val df_Filter_2      = Filter_2(context,      df_Repartition_1)
    val df_Filter_5      = Filter_5(context,      df_SchemaTransform_2)
    val df_Deduplicate_1 = Deduplicate_1(context, df_RowDistributor_1_out1)
    val df_Script_10_1   = Script_10_1(context,   df_Script_9_out0)
    val df_src_jdbc_userandpass_test_table = src_jdbc_userandpass_test_table(
      context
    )
    val df_Script_10 = Script_10(context, df_Script_9_out1)
    val df_Script_11 = Script_11(context, df_Script_10)
    val df_Script_13 = Script_13(context, df_Script_11).cache()
    val df_Script_14 = Script_14(context, df_Script_13)
    val df_Script_15 = Script_15(context, df_Script_14)
    target_dataset_1(context, df_Reformat_4)
    Script_1(context)
    val df_Reformat_5 = Reformat_5(context, df_Filter_5)
    val df_Reformat_6 = Reformat_6(context, df_Reformat_5)
    target_dataset_1_1(context, df_Reformat_6)
    val df_Script_10_1_1   = Script_10_1_1(context,   df_Script_9_out2)
    val df_Repartition_2   = Repartition_2(context,   df_Limit_2)
    val df_Script_10_1_2_1 = Script_10_1_2_1(context, df_Script_13)
    val df_Script_10_1_2   = Script_10_1_2(context,   df_Script_11)
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
                   "pipelines/ScInterimsDatabricksPipeline"
    )
    registerUDFs(spark)
    MetricsCollector.start(spark, "pipelines/ScInterimsDatabricksPipeline")
    apply(context)
    MetricsCollector.end(spark)
  }

}
