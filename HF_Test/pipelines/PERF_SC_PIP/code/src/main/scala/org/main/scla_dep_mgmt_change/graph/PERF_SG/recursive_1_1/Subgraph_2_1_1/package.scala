package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.config.{
  Context => Subgraph_3_1_1_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_2_1_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Subgraph_3_1_1 = Subgraph_3_1_1.apply(
      Subgraph_3_1_1_Context(context.spark, context.config.Subgraph_3_1_1),
      in0
    )
    val df_Reformat_1 = Reformat_1(context, df_Subgraph_3_1_1).interim(
      "Subgraph_2_1_1",
      "UzhqD871IEfNkIKrKs-qP$$PTY_UbbBSEqBvpqQc8BVe",
      "ngZS1uDhgAY9Sy0fFT6yP$$Gek3pSMT6RHHUBxZs823H"
    )
    df_Reformat_1
  }

}
