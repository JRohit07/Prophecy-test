package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.config.{
  Context => Subgraph_7_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_6 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Subgraph_7 = Subgraph_7.apply(
      Subgraph_7_Context(context.spark, context.config.Subgraph_7),
      in0
    )
    df_Subgraph_7
  }

}
