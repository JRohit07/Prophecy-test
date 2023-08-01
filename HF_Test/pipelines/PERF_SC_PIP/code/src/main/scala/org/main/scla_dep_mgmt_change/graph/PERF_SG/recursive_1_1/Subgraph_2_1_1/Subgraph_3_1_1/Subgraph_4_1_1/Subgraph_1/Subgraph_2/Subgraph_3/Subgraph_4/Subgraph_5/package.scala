package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.config.{
  Context => Subgraph_6_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_5 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_7 = Reformat_7(context, in0).interim(
      "Subgraph_5",
      "FoiChRJvFxXWB3Rs6VkhT$$mFZasxHuCV-jH6UIu8M5l",
      "7WlhFFf7WYCMZRpK4ZlPG$$1GgmO7gu6Zbr5vP1LWAl1"
    )
    val df_Subgraph_6 = Subgraph_6.apply(
      Subgraph_6_Context(context.spark, context.config.Subgraph_6),
      df_Reformat_7
    )
    df_Subgraph_6
  }

}
