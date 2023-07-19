package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.config.{
  Context => Subgraph_4_1_1_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_3_1_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Subgraph_4_1_1 = Subgraph_4_1_1.apply(
      Subgraph_4_1_1_Context(context.spark, context.config.Subgraph_4_1_1),
      in0
    )
    val df_Reformat_2 = Reformat_2(context, df_Subgraph_4_1_1).interim(
      "Subgraph_3_1_1",
      "ZfEnDr4i72er_2pwVZHIZ$$2A6Sg2ludSS_yREdsfEM6",
      "TrEckl9ewfI5Y5Xge99BN$$F5fRoXN_4aQWcWDRZERSw"
    )
    df_Reformat_2
  }

}
