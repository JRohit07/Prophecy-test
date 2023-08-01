package org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.Subgraph_4_1
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.Subgraph_4_1.config.{
  Context => Subgraph_4_1_Context
}
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.config._
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_3_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Subgraph_4_1 = Subgraph_4_1.apply(
      Subgraph_4_1_Context(context.spark, context.config.Subgraph_4_1),
      in0
    )
    val df_Reformat_5_1 = Reformat_5_1(context, df_Subgraph_4_1).interim(
      "Subgraph_3_1",
      "VB1OCxqmxaAw8IKh1SXDg$$--zuf0DxIJWRXnxKV096_",
      "Bohxyl3etMpUL76SFhG2z$$rcf1ufHUSuRiu6dTqUp7V"
    )
    df_Reformat_5_1
  }

}
