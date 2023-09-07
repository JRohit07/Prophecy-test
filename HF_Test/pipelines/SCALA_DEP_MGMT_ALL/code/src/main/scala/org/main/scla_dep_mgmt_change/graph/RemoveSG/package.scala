package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.RemoveSG.config._
import org.main.scla_dep_mgmt_change.graph.RemoveSG.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object RemoveSG {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_17 =
      if (context.config.c_array_complex(0).car_record.carr_short < -10)
        Reformat_17(context, in0).interim(
          "RemoveSG",
          "tpFdqF3990DNwhs3nCZst$$3Q5Ya2X-hasnjxSzEV3qS",
          "NrsBPSWDJswaDSvUkPiCm$$TWDiucQ0JyMngT2JZFC-R"
        )
      else in0
    val df_Limit_4 = Limit_4(context, df_Reformat_17).interim(
      "RemoveSG",
      "thnowz1O3XAceiYJlV2L6$$0fpvKJL1cYdP04UZB4TOi",
      "dVGNYHElKsow0USZhgnAn$$typsJy5KzZmTjb_8btdkF"
    )
    val df_Reformat_16 = Reformat_16(context, in0).interim(
      "RemoveSG",
      "WADcjffbqwsPbgEF5Zm-L$$XGdRx3HV1d-W4TwNnbuxA",
      "CKOeVssqUh3fWFlAgKi47$$Gw40QW81qTgFRlSxu56ly"
    )
    val df_Filter_10 =
      if (context.config.c_array_complex(0).car_record.carr_short < -10) {
        val df_Limit_2 = Limit_2(context, df_Reformat_16).interim(
          "RemoveSG",
          "vIK0DJ0dZaMfWCFc3bdtX$$_q45sduOCbMjbr92olfvT",
          "fzPF-lnoVcMUCWom95IeI$$c3Dgw4ze3UQR8qZm47rll"
        )
        Filter_10(context, df_Limit_2).interim(
          "RemoveSG",
          "g-IZxf7NJ2muKVJ_vvUYR$$2pOSeM3ToXXPPgljK5Ic9",
          "EAKfc9mWhQjmmay5m7irh$$6KOlLQ0pRSZMvjIoiZzTL"
        )
      } else
        null
    val df_Script_15 = Script_15(context, df_Limit_4).interim(
      "RemoveSG",
      "pUhAz3DFBeYo3PFPvwZya$$mej7wEgo-hxLFwWAuaC_5",
      "PAKZX_f-2k9B-JUZxfJg6$$_nQUP72Hx7g8RBLhMfBAt"
    )
    df_Script_15.cache().count()
    df_Script_15.unpersist()
    df_Filter_10
  }

}
