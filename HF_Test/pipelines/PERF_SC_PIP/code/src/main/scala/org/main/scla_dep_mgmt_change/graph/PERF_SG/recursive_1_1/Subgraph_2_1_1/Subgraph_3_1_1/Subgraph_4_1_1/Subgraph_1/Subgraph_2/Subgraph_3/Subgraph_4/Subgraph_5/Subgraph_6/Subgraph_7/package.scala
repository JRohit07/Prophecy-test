package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.Subgraph_8
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.Subgraph_8.config.{
  Context => Subgraph_8_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_7 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_8 = Reformat_8(context, in0).interim(
      "Subgraph_7",
      "mC7Me28mrgHSfCN9CEr3U$$1oOPnCPlmGmlLE2aPwnNa",
      "1No54yqglVbzy2bSUXMvH$$7D1A4FE8Ny7xWFmUmo3cB"
    )
    val df_Subgraph_8 = Subgraph_8.apply(
      Subgraph_8_Context(context.spark, context.config.Subgraph_8),
      df_Reformat_8
    )
    df_Subgraph_8
  }

}
