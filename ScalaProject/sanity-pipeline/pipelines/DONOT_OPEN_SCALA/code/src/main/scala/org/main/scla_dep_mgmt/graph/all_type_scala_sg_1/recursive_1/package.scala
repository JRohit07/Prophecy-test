package org.main.scla_dep_mgmt.graph.all_type_scala_sg_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.Subgraph_2_1
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.Subgraph_1
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.Subgraph_2_1.config.{
  Context => Subgraph_2_1_Context
}
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.Subgraph_1.config.{
  Context => Subgraph_1_Context
}
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.config._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.config.Config.interimOutput
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
      "Zzyl2VxNguPIf8bRXuy7-$$FUvoT8KbAzTMl9sFIDRJl",
      "WLUuKWXWPHnuNFa04SDZ-$$WnbEXDX0kr_2apSwA6T_w"
    )
    val df_FlattenSchema_1_2 =
      FlattenSchema_1_2(context, df_very_complex_dataset).interim(
        "recursive_1",
        "vehdNg0TFg1AOWCJmMrSY$$toibagSxdbpxrxbsUmt8P",
        "uBtyJRv-1w9sZ7aVV3ErM$$6qrP4BcTINlsoA2t5WQqu"
      )
    val df_Reformat_3_1 = Reformat_3_1(context, in0).interim(
      "recursive_1",
      "jiGNL3C_2hXv9zvRilmeP$$g96P8g-RqRLoYY44JOCMu",
      "k3m-wgXN7AdI1qeeM3boA$$Ggs7e_9S5UOmofHJaeLUS"
    )
    val df_Reformat_12 = Reformat_12(context, df_very_complex_dataset).interim(
      "recursive_1",
      "40EzUwDikmpMZBTmes6oT$$xaw1dx62rMdxkEi2Pkjd4",
      "03pqQEjtlaSIRdbDcxCJZ$$nI7_kTV05MIXdL-CpLhOs"
    )
    val df_Reformat_14 = Reformat_14(context, df_Reformat_12).interim(
      "recursive_1",
      "4Yix_IhdJtLp1F4CtgwYy$$Z6csrVfXdZJgUBXZhArDw",
      "coofe004xetvdMSU4bihs$$1-nxBRKlLeCsi4r931mnH"
    )
    df_Reformat_14.cache().count()
    df_Reformat_14.unpersist()
    val df_Reformat_13 = Reformat_13(context, df_FlattenSchema_1_2).interim(
      "recursive_1",
      "k0G6kyneWPxo7Hlkw_y6h$$-95tzfslB3-E76pAkfs92",
      "UZRhl2KrXOKp5m0p6DuOh$$bKC7rpQ3t3Q9TuCfrHaxT"
    )
    df_Reformat_13.cache().count()
    df_Reformat_13.unpersist()
    val df_Subgraph_2_1 = Subgraph_2_1.apply(
      Subgraph_2_1_Context(context.spark, context.config.Subgraph_2_1),
      df_Reformat_3_1
    )
    val df_Subgraph_1 = Subgraph_1.apply(
      Subgraph_1_Context(context.spark, context.config.Subgraph_1),
      df_Subgraph_2_1
    )
    df_Subgraph_1.cache().count()
    df_Subgraph_1.unpersist()
    df_Subgraph_2_1
  }

}
