package io.prophecy.pipelines.livy_scala.graph

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.config._
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.Subgraph_2_1_2
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.Subgraph_2_1_2.config.{
  Context => Subgraph_2_1_2_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object livyscalaSG1_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_2_1_2 = Reformat_2_1_2(context, in0)
    val df_Filter_1_1_2   = Filter_1_1_2(context,   df_Reformat_2_1_2)
    val df_OrderBy_1_1_2  = OrderBy_1_1_2(context,  df_Filter_1_1_2)
    val df_Subgraph_2_1_2 = Subgraph_2_1_2.apply(
      Subgraph_2_1_2_Context(context.spark, context.config.Subgraph_2_1_2),
      df_OrderBy_1_1_2
    )
    df_Subgraph_2_1_2
  }

}
