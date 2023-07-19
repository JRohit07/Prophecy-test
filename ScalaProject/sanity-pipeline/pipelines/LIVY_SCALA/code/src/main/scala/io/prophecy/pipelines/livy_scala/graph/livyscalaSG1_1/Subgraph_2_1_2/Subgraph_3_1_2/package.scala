package io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.Subgraph_2_1_2

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.Subgraph_2_1_2.Subgraph_3_1_2.config._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_3_1_2 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_4_1_2 = Reformat_4_1_2(context, in0)
    df_Reformat_4_1_2
  }

}
