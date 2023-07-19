package com.main.sub_graph_src1.graph.all_type_sg_scala_main

import io.prophecy.libs._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_1
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.config.{
  Context => Subgraph_2_1_Context
}
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.Subgraph_1.config.{
  Context => Subgraph_1_Context
}
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.config._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object recursive_1 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_very_complex_dataset = very_complex_dataset(context).interim(
      "recursive_1",
      "Zzyl2VxNguPIf8bRXuy7-$$VTcJylQhpb0rIf8ZPongR",
      "WLUuKWXWPHnuNFa04SDZ-$$byjQgdbuVJ1SQeocv_mxd"
    )
    val df_FlattenSchema_1_2 =
      FlattenSchema_1_2(context, df_very_complex_dataset).interim(
        "recursive_1",
        "vehdNg0TFg1AOWCJmMrSY$$GwC516Yy59XGlkXX6iw-R",
        "uBtyJRv-1w9sZ7aVV3ErM$$DSxblDO_2xT6pGoekFShI"
      )
    val df_Reformat_12 = Reformat_12(context, df_very_complex_dataset).interim(
      "recursive_1",
      "40EzUwDikmpMZBTmes6oT$$35KX0GkrBzSoCezpLanCU",
      "03pqQEjtlaSIRdbDcxCJZ$$EizCxAeeJv7lt85tGby9k"
    )
    val df_Reformat_3_1 = Reformat_3_1(context, in0).interim(
      "recursive_1",
      "jiGNL3C_2hXv9zvRilmeP$$ESSC4eRR6Ot-f_rIcw_pP",
      "k3m-wgXN7AdI1qeeM3boA$$XARlawNbqKAnTSVK-m1Ub"
    )
    val df_Subgraph_2_1 = Subgraph_2_1.apply(
      Subgraph_2_1_Context(context.spark, context.config.Subgraph_2_1),
      df_Reformat_3_1
    )
    val df_Reformat_13 = Reformat_13(context, df_FlattenSchema_1_2).interim(
      "recursive_1",
      "k0G6kyneWPxo7Hlkw_y6h$$LYQYy8LqgXNRbn9Rg3yL-",
      "UZRhl2KrXOKp5m0p6DuOh$$KMyN_0FlnWpt3BgykAv6A"
    )
    df_Reformat_13.cache().count()
    df_Reformat_13.unpersist()
    val df_Subgraph_1 = Subgraph_1.apply(
      Subgraph_1_Context(context.spark, context.config.Subgraph_1),
      df_Subgraph_2_1
    )
    df_Subgraph_1.cache().count()
    df_Subgraph_1.unpersist()
    val df_Reformat_14 = Reformat_14(context, df_Reformat_12).interim(
      "recursive_1",
      "4Yix_IhdJtLp1F4CtgwYy$$VI9xk0M0_XWHKsnBEkWO0",
      "coofe004xetvdMSU4bihs$$_yjJT7XXknFkcjDRfOAXu"
    )
    df_Reformat_14.cache().count()
    df_Reformat_14.unpersist()
    df_Subgraph_2_1
  }

}
