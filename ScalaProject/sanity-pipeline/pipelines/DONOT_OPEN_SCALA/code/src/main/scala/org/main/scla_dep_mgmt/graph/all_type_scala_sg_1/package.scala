package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.recursive_1.config.{
  Context => recursive_1_Context
}
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object all_type_scala_sg_1 {

  def apply(
    context: Context,
    in0:     DataFrame,
    in1:     DataFrame,
    in2:     DataFrame
  ): Subgraph3 = {
    val df_src_csv_all_type_no_partition_1 =
      src_csv_all_type_no_partition_1(context).interim(
        "all_type_scala_sg_1",
        "A9rElKDgLrUiv9NV-Gb_N$$mi4sLlIrGMW1nQ1YUnY2r",
        "0NwLDePbq8XoET6rLo-n3$$Uvm9UP7hQLP4SNVdSWazS"
      )
    Lookup_1_1(context, df_src_csv_all_type_no_partition_1)
    val df_Reformat_2_1 = Reformat_2_1(context, in0).interim(
      "all_type_scala_sg_1",
      "hUP1i867OpQpUfEFUJCQy$$7TtS_V7R0-_efBZwTIkWg",
      "IOGnwjIuO1YjIb-sLJyha$$z-m88Ih-4MuofF6x72-3l"
    )
    val df_Filter_1_1 = Filter_1_1(context, df_Reformat_2_1).interim(
      "all_type_scala_sg_1",
      "lgmqnTtMR3qcVjlH2Ep35$$xEIGcFFxRp7ARl7oyvMaP",
      "UULbpwesGwistLf0QlHPk$$YtgAts6E0a4nfRfpAQFnT"
    )
    val df_OrderBy_1_1 = OrderBy_1_1(context, df_Filter_1_1).interim(
      "all_type_scala_sg_1",
      "l-CYWkwAxWLBq7BtZXNmc$$MVOjmDP64qcYLKVYv_MLG",
      "Ddaz4jJQzSi44fZRicVSW$$dACb-pEeKjRuZzSmirR03"
    )
    val df_Limit_1_1 = Limit_1_1(context, df_OrderBy_1_1).interim(
      "all_type_scala_sg_1",
      "4zrXJ1pBVISuC3q-XDTmZ$$xDm9tMz7He7Ro_BUjTCLl",
      "g6spxFdnq3qgPqw265z3O$$TnlBMLQK4x1vkubSaLMKk"
    )
    val df_WindowFunction_1_1 =
      WindowFunction_1_1(context, df_Limit_1_1).interim(
        "all_type_scala_sg_1",
        "thGcHosI_1BgWDJrHjFoV$$kd-lpKiS1zulY50Lc9-IB",
        "gtWt2VSgvUB0J7hcxUL0n$$QKwGYTH68d1VkrBSH0dU5"
      )
    val df_SetOperation_1_1 = SetOperation_1_1(context,
                                               df_WindowFunction_1_1,
                                               df_WindowFunction_1_1
    ).interim("all_type_scala_sg_1",
              "2364u3XyEfqkcOFGPdruQ$$wYi-pe2wpipIQJpQQ_7vO",
              "Vd1zEA7MfS5nw7LTlqhDD$$mC1nOH0_rnG7RekIClcXo"
    )
    val df_SchemaTransform_1_1 =
      SchemaTransform_1_1(context, df_SetOperation_1_1).interim(
        "all_type_scala_sg_1",
        "Cpp-eSDWFOydUile7Uyio$$XH_csNiGRHX09IKDnC4gt",
        "xLJkxvbQqP8DuRgGsUUiP$$ib2bSfpt-XiNNtn198ZHJ"
      )
    val df_Join_1_1 =
      Join_1_1(context, df_SchemaTransform_1_1, df_SchemaTransform_1_1).interim(
        "all_type_scala_sg_1",
        "YsPCyfeLBsN_-gEeTFtDN$$LtZUN6qGgQCokve8xkhku",
        "RD_fpo-eYIkVlGHMOhi40$$tcQ3wxcvkOvswZk6WrV-r"
      )
    val (df_RowDistributor_1_1_out0, df_RowDistributor_1_1_out1) = {
      val (df_RowDistributor_1_1_out0_temp, df_RowDistributor_1_1_out1_temp) =
        RowDistributor_1_1(context, df_Join_1_1)
      (df_RowDistributor_1_1_out0_temp.interim(
         "all_type_scala_sg_1",
         "PgUYSxgP6yAYJcJ3ppHfX$$wW3w4iSFraq_VsMT8bnT0",
         "HxaQX0nF88aUd633ycAPm$$xDbwDdLriA_ABtA3qYMIb"
       ),
       df_RowDistributor_1_1_out1_temp.interim(
         "all_type_scala_sg_1",
         "PgUYSxgP6yAYJcJ3ppHfX$$wW3w4iSFraq_VsMT8bnT0",
         "PwWx57iOUAbAqGLDKsfGQ$$W6aYvjrxQ4MaE5AUifyIs"
       )
      )
    }
    val df_Aggregate_1_1 =
      Aggregate_1_1(context, df_RowDistributor_1_1_out0).interim(
        "all_type_scala_sg_1",
        "40x82-YyIIUk7pIhht2LX$$ZCIeq9myjalNVX9WxojC2",
        "JSwGY5d6RoYVcwEbme7Hq$$2VP80ojDY3nc7WLQ9_7UE"
      )
    val df_Deduplicate_1_1 = Deduplicate_1_1(context, in1).interim(
      "all_type_scala_sg_1",
      "6ITI0NEHkk-C0PzFrl3JB$$ZgHDP7prfcwBpq3NNXj-L",
      "djg3J1fGmwlsK4U4kIhZ1$$2sgXnfeFAu-dTIA0r_mN1"
    )
    val df_Script_1_1 = Script_1_1(context, df_Deduplicate_1_1).interim(
      "all_type_scala_sg_1",
      "NhC1SRdJyLJ_imHbm-SGU$$Nadsi_X2dixmX7ZoVy5tv",
      "cix9b7hiz5GT6SHK1a2ey$$M_p9K0N_yjTjl6eEal2kg"
    )
    val df_Reformat_7 = Reformat_7(context, in2).interim(
      "all_type_scala_sg_1",
      "rTy83DSuASMaEv6ATwCpc$$URlQTPFbMeb83Gg5DBnwm",
      "5LiZljahU3bU_Rym0A-1p$$5EnktdKLqT42j1JIco1cw"
    )
    df_Reformat_7.cache().count()
    df_Reformat_7.unpersist()
    val df_Reformat_1_1 =
      Reformat_1_1(context, df_src_csv_all_type_no_partition_1).interim(
        "all_type_scala_sg_1",
        "WwV8YcgqfDbTr1Qjw-_ub$$pnS8qdrEHHcUrAYFZLdQT",
        "y-_P0LZWdJ6sodhEZaaQ6$$9axgrkS6-bnnp4-zOmcyr"
      )
    val df_FlattenSchema_1_1 =
      FlattenSchema_1_1(context, df_Aggregate_1_1).interim(
        "all_type_scala_sg_1",
        "7dSYHS4ccxtaDQIA58yGB$$0vGQ4fdsK8r7WYVDqZPNA",
        "1TNe7-gys_ySzJscz90bs$$U5UKRBjPcsxN0mxhMpDcs"
      )
    val df_Reformat_3 = Reformat_3(context, df_Filter_1_1).interim(
      "all_type_scala_sg_1",
      "hlCiNUUN4-N1dhJqgjw_N$$m53kkOweyoa0tqNBzjFUA",
      "WIIEsa_6EAsbIWCfQEA1i$$2MTFbS89-FgUXHHgHxwpZ"
    )
    df_Reformat_3.cache().count()
    df_Reformat_3.unpersist()
    val df_OrderBy_2_1 =
      OrderBy_2_1(context, df_RowDistributor_1_1_out1).interim(
        "all_type_scala_sg_1",
        "Q732qOBLhcrT2x0MvHU_E$$Bq-CHD0qeTb6ke1F_1KM8",
        "Nljh_h-Q4z_oo_ltnGgSe$$8WZQIha0hUl_nuHdx2aCl"
      )
    val df_recursive_1 = recursive_1.apply(
      recursive_1_Context(context.spark, context.config.recursive_1),
      df_Script_1_1
    )
    withSubgraphName("all_type_scala_sg_1", context.spark) {
      withTargetId("scala_random_target_subgraph_donotuse", context.spark) {
        scala_random_target_subgraph_donotuse(context, df_Reformat_1_1)
      }
    }
    val df_SQLStatement_1 =
      SQLStatement_1(context, df_SetOperation_1_1).interim(
        "all_type_scala_sg_1",
        "LcKgbTCXM4s71Zw5K7_U-$$iw4liVD4ogiYLMk9A6Luq",
        "SMB10nqnNy5840kTondLS$$tdxUazXGndo0cdogp8Kxr"
      )
    df_SQLStatement_1.cache().count()
    df_SQLStatement_1.unpersist()
    (df_FlattenSchema_1_1, df_OrderBy_2_1, df_recursive_1)
  }

}
