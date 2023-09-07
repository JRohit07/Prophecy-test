package com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1

import io.prophecy.libs._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.config.{
  Context => Subgraph_3_1_Context
}
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.config._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_2_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Subgraph_3_1 = Subgraph_3_1.apply(
      Subgraph_3_1_Context(context.spark, context.config.Subgraph_3_1),
      in0
    )
    val df_Reformat_4_1 = Reformat_4_1(context, df_Subgraph_3_1).interim(
      "Subgraph_2_1",
      "-ppXcjnTV-2HsQtnE7AqM$$Ql2IK78tFO6fChAdTnPrw",
      "fm5CFh16l0ffbWK_W8ULz$$4YJ6-joqsao9saXcRaj1x"
    )
    df_Reformat_4_1
  }

}
