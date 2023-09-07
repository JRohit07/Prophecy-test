package org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.Subgraph_8.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.Subgraph_3_1_1.Subgraph_4_1_1.Subgraph_1.Subgraph_2.Subgraph_3.Subgraph_4.Subgraph_5.Subgraph_6.Subgraph_7.Subgraph_8.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_8 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_9 = Reformat_9(context, in0).interim(
      "Subgraph_8",
      "2oi0IiySPPsLvyookmEcP$$TTxMjrevsHpYZ6RnNKnnm",
      "Bq4g1LynU6VD_ZrH49Im6$$PRb6Q4xpTv_jBKpnnFh85"
    )
    df_Reformat_9
  }

}
