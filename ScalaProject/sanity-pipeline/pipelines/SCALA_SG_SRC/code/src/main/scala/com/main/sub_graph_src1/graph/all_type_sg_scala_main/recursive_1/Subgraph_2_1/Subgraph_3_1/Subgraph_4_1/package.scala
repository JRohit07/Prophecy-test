package com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1

import io.prophecy.libs._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.Subgraph_4_1.config._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.Subgraph_4_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_4_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_6_1 = Reformat_6_1(context, in0).interim(
      "Subgraph_4_1",
      "GINAx9UxLYxYEacHmRR4N$$is7xJA6hq7KABBEg-vHZd",
      "napEovIX7XPJo3LvhF_EI$$Aa-SRRGOOyThscVWkEM2r"
    )
    df_Reformat_6_1
  }

}
