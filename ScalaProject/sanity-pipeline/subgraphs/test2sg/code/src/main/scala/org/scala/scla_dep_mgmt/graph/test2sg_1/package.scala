package org.scala.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.graph.test2sg_1.recursive_1
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object test2sg_1 {

  def apply(
    spark: SparkSession,
    in0:   DataFrame,
    in1:   DataFrame,
    in2:   DataFrame
  ): Subgraph3 = {
    val df_src_csv_all_type_no_partition_1 = src_csv_all_type_no_partition_1(
      spark
    )
    Lookup_1_1(spark, df_src_csv_all_type_no_partition_1)
    val df_Reformat_2_1       = Reformat_2_1(spark,       in0)
    val df_Filter_1_1         = Filter_1_1(spark,         df_Reformat_2_1)
    val df_OrderBy_1_1        = OrderBy_1_1(spark,        df_Filter_1_1)
    val df_Limit_1_1          = Limit_1_1(spark,          df_OrderBy_1_1)
    val df_WindowFunction_1_1 = WindowFunction_1_1(spark, df_Limit_1_1)
    val df_SetOperation_1_1 =
      SetOperation_1_1(spark, df_WindowFunction_1_1, df_WindowFunction_1_1)
    val df_SchemaTransform_1_1 = SchemaTransform_1_1(spark, df_SetOperation_1_1)
    val df_Join_1_1 =
      Join_1_1(spark, df_SchemaTransform_1_1, df_SchemaTransform_1_1)
    val df_Deduplicate_1_1 = Deduplicate_1_1(spark,   in1)
    val df_Script_1_1      = Script_1_1(spark,        df_Deduplicate_1_1)
    val df_recursive_1     = recursive_1.apply(spark, df_Script_1_1)
    val (df_RowDistributor_1_1_out0, df_RowDistributor_1_1_out1) =
      RowDistributor_1_1(spark, df_Join_1_1)
    val df_Aggregate_1_1 = Aggregate_1_1(spark, df_RowDistributor_1_1_out0)
    val df_Reformat_7    = Reformat_7(spark,    in2)
    val df_Reformat_1_1 =
      Reformat_1_1(spark, df_src_csv_all_type_no_partition_1)
    val df_FlattenSchema_1_1 = FlattenSchema_1_1(spark, df_Aggregate_1_1)
    val df_OrderBy_2_1       = OrderBy_2_1(spark,       df_RowDistributor_1_1_out1)
    (df_FlattenSchema_1_1, df_OrderBy_2_1, df_recursive_1)
  }

}
