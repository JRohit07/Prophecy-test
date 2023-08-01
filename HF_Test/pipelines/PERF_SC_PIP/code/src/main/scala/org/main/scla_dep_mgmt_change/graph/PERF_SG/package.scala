package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1
import org.main.scla_dep_mgmt_change.graph.PERF_SG.recursive_1_1.config.{
  Context => recursive_1_1_Context
}
import org.main.scla_dep_mgmt_change.graph.PERF_SG.config._
import org.main.scla_dep_mgmt_change.graph.PERF_SG.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object PERF_SG {

  def apply(
    context: Context,
    in0:     DataFrame,
    in1:     DataFrame,
    in2:     DataFrame
  ): Subgraph3 = {
    val df_src_csv_all_type_no_partition_1_1 =
      src_csv_all_type_no_partition_1_1(context).interim(
        "PERF_SG",
        "z5Du1bwIZ82rQA2CdyG63$$OCrNaxIvtvQaoz8s_7zlb",
        "HJYN58J1QJzCy2jlQbQDu$$WCzgeJ0XkhN7iRAASTn5a"
      )
    Lookup_1_1_1(context, df_src_csv_all_type_no_partition_1_1)
    val df_PERF_SG_REFORMAT = PERF_SG_REFORMAT(context, in0).interim(
      "PERF_SG",
      "4hGVpT0DFJwU3z7N175hr$$EPoXMSOn_hUm0ETAEdU6K",
      "3EaRaX3ibs1LA-Kpzz-rF$$fZcgJ2MZ9IY-4kIIvHink"
    )
    val df_Filter_1_1_1 = Filter_1_1_1(context, df_PERF_SG_REFORMAT).interim(
      "PERF_SG",
      "6DkXbdH3NlLTCZboBca6Q$$VNatRgt3UZH4_PhqFFhn3",
      "786cAPV8OmtT4v51saaBv$$BzWYlDP-HNVT-IIK8oDX5"
    )
    val df_OrderBy_1_1_1 = OrderBy_1_1_1(context, df_Filter_1_1_1).interim(
      "PERF_SG",
      "PpfB7nN0M6RTM7z24K0rR$$JnNolRLuwsKGv_mvTVouB",
      "6QFLSL3ohXj_BZCgU1Eoo$$Q8q-7Nl1E6-bEu92s-Qe7"
    )
    val df_UTGenReformat_1_1_1 = UTGenReformat_1_1_1(
      context,
      df_src_csv_all_type_no_partition_1_1
    ).interim("PERF_SG",
              "N4GbQ37MiVlqJOKV-8A7n$$av1PqVjmQOh2wSkK_eyhD",
              "72tZXuerzEsCg-amdOrKW$$lrLo42lW-fUR7pFiFrZ3y"
    )
    df_UTGenReformat_1_1_1.cache().count()
    df_UTGenReformat_1_1_1.unpersist()
    val df_Deduplicate_1_1_1 = Deduplicate_1_1_1(context, in1).interim(
      "PERF_SG",
      "BstTFeBQXqnyzfZAA1CAe$$b6MqVExQYQqjv_BNL55Ks",
      "wGyiGD6l1x5Nojwg8jNoM$$QE86As1PTGcR0RUG92Rmr"
    )
    val df_Script_1_1_1 = Script_1_1_1(context, df_Deduplicate_1_1_1).interim(
      "PERF_SG",
      "j8unj6CKp8Sn5sY09vijj$$6S59lhTRAI8NyevBhN-IR",
      "IHwe68RY-kUX1i8Jh3iEl$$6CVLiQaxN4QPUeTDHXDA6"
    )
    val df_recursive_1_1 = recursive_1_1.apply(
      recursive_1_1_Context(context.spark, context.config.recursive_1_1),
      df_Script_1_1_1
    )
    val df_Limit_1_1_1 = Limit_1_1_1(context, df_OrderBy_1_1_1).interim(
      "PERF_SG",
      "tpBLg_VKeT4Kg6yOhH9Sz$$dnVo0YttmXYvNkhl7Hw3Y",
      "hRuYI3eN7zKxKqoa1zpdu$$yYm7GT_QISrfMyeuD3xhJ"
    )
    val df_WindowFunction_1_1_1 =
      WindowFunction_1_1_1(context, df_Limit_1_1_1).interim(
        "PERF_SG",
        "OxP_pkBtbhPhlyg79eEx-$$I2doJRAU8NGu8md5-gxAM",
        "8g7inlr_8PxSP9CPhWura$$K2jpjBMu181xoeP4D4mno"
      )
    val df_SetOperation_1_1_1 = SetOperation_1_1_1(context,
                                                   df_WindowFunction_1_1_1,
                                                   df_WindowFunction_1_1_1
    ).interim("PERF_SG",
              "SEURe6pbn4HlawuySzixO$$ucwgtLm9VdCFvw6rw57MS",
              "twyZfMMlQEAmEz21Bg0w6$$ELQs3cIherPplVeQAszV-"
    )
    val df_SchemaTransform_1_1_1 =
      SchemaTransform_1_1_1(context, df_SetOperation_1_1_1).interim(
        "PERF_SG",
        "Y9HfFyweV6y1SmCCETIbZ$$ojqMZ6ezIvTZnFnvsY2ho",
        "heBZHoVEuuEz0DlK6T1lT$$1PIZQLS2e6u07zprMZ2lg"
      )
    val df_Join_1_1_1 = Join_1_1_1(context,
                                   df_SchemaTransform_1_1_1,
                                   df_SchemaTransform_1_1_1
    ).interim("PERF_SG",
              "knuOKz9dzgOEK8s71hnpY$$Wl3LRc6N9ck3BhQYBdMRV",
              "HZ4xGuSWUEm7ic3ZQT-Oz$$LD0sy3TjFWKoWnX9FHVHF"
    )
    val (df_RowDistributor_1_1_1_out0, df_RowDistributor_1_1_1_out1) = {
      val (df_RowDistributor_1_1_1_out0_temp,
           df_RowDistributor_1_1_1_out1_temp
      ) = RowDistributor_1_1_1(context, df_Join_1_1_1)
      (df_RowDistributor_1_1_1_out0_temp.interim(
         "PERF_SG",
         "GkbPdg6CgtmdguRnGD5p7$$MsIG2u9QrmJsaPr0R0iGM",
         "_O1CHv4_k4nWE_Fsm0UvR$$1Yji8oxXJk-ZZLWWGDHUf"
       ),
       df_RowDistributor_1_1_1_out1_temp.interim(
         "PERF_SG",
         "GkbPdg6CgtmdguRnGD5p7$$MsIG2u9QrmJsaPr0R0iGM",
         "X7cI9ZXkX_4tu01wyK7w6$$KKwVe2jwCffPwET_Vc-1x"
       )
      )
    }
    val df_OrderBy_2_1_1 =
      OrderBy_2_1_1(context, df_RowDistributor_1_1_1_out1).interim(
        "PERF_SG",
        "9QnAsdKbbD1IFgF0U02EQ$$uRxlUpucD0AJqJDyEsvaS",
        "zkegYfsq_LBLEgp-x5JfM$$6GsCwHcDh9x89W4pLypGS"
      )
    val df_Aggregate_1_1_1 =
      Aggregate_1_1_1(context, df_RowDistributor_1_1_1_out0).interim(
        "PERF_SG",
        "NdlTwHqaSu-ZNXLNVYqjr$$10S9lvUfjw6yquvu6pxvT",
        "55PBaZISovD53ixZ4RkR5$$RmTVPFhIY6-fQ_Oy9TN-j"
      )
    df_Aggregate_1_1_1.cache().count()
    df_Aggregate_1_1_1.unpersist()
    val df_FlattenSchema_3 =
      FlattenSchema_3(context, df_RowDistributor_1_1_1_out0).interim(
        "PERF_SG",
        "sPSzTLsI8ToypWkPxzWdb$$YZka2zT4tSh7jnY6pNWGU",
        "P9Hv_1cup0I2zP2-efwNz$$7NPABCe7xaeXh4Xr11o4n"
      )
    df_FlattenSchema_3.cache().count()
    df_FlattenSchema_3.unpersist()
    val df_Reformat_7_1 = Reformat_7_1(context, in2).interim(
      "PERF_SG",
      "I0ZFNslgH6Hlqo97KT4yr$$D0mFZ1FL5XmAyzExfHAzp",
      "8nWlBUDk519hbjnlaF7WF$$-YvY5pRvpWFOUgjDUe_na"
    )
    df_Reformat_7_1.cache().count()
    df_Reformat_7_1.unpersist()
    (df_RowDistributor_1_1_1_out0, df_OrderBy_2_1_1, df_recursive_1_1)
  }

}
