package io.prophecy.pipelines.perf_unitest_generate.graph

import io.prophecy.libs._
import io.prophecy.pipelines.perf_unitest_generate.graph.Subgraph_1.config._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_2 = Reformat_2(context, in0)
    df_Reformat_2
  }

}
