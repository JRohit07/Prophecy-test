package org.main.scla_dep_mgmt_change.graph.PERF_SG

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.Subgraph_2_1_1.config.{
  Context => Subgraph_2_1_1_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object recursive_1_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_4 = Reformat_4(context, in0).interim(
      "recursive_1_1",
      "sbEXz-Cfbz8e9Hj7Gk55M$$_4IDiFk0UllKlLFIINI8g",
      "n3talgcDcWMeJx2dkLNYw$$bR__vMzPFEJpIjQaZy14Y"
    )
    val df_Subgraph_2_1_1 = Subgraph_2_1_1.apply(
      Subgraph_2_1_1_Context(context.spark, context.config.Subgraph_2_1_1),
      df_Reformat_4
    )
    df_Subgraph_2_1_1
  }

}
