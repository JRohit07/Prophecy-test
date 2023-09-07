package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.pm_shared_graph.Subgraph_1
import org.main.scla_dep_mgmt_change.graph.pm_shared_graph.Subgraph_1.config.{
  Context => Subgraph_1_Context
}
import org.main.scla_dep_mgmt_change.graph.pm_shared_graph.config._
import org.main.scla_dep_mgmt_change.graph.pm_shared_graph.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object pm_shared_graph {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_10 = Reformat_10(context, in0).interim(
      "pm_shared_graph",
      "Ly2IBGE1CPgoC51992Ii-$$nmbRGZ9oVlFASTMUoNGHZ",
      "dbBBb_rXY6Y3Tjj_5R8FF$$uP4-_O4RwIMeoywviDbo9"
    )
    val df_Subgraph_1 = Subgraph_1.apply(
      Subgraph_1_Context(context.spark, context.config.Subgraph_1),
      df_Reformat_10
    )
    df_Subgraph_1
  }

}
