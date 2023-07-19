package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.graph.Subgraph_2.config._
import org.main.scla_dep_mgmt_change.graph.Subgraph_2.config.Config.interimOutput
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_2 {

  def apply(
    context: Context,
    in0:     DataFrame,
    in1:     DataFrame,
    in2:     DataFrame,
    in3:     DataFrame,
    in4:     DataFrame,
    in5:     DataFrame,
    in6:     DataFrame,
    in7:     DataFrame
  ): Subgraph8 = {
    val (df_SQLStatement_2_out,
         df_SQLStatement_2_out1,
         df_SQLStatement_2_out2,
         df_SQLStatement_2_out3,
         df_SQLStatement_2_out4,
         df_SQLStatement_2_out5,
         df_SQLStatement_2_out6,
         df_SQLStatement_2_out7
    ) = {
      val (df_SQLStatement_2_out_temp,
           df_SQLStatement_2_out1_temp,
           df_SQLStatement_2_out2_temp,
           df_SQLStatement_2_out3_temp,
           df_SQLStatement_2_out4_temp,
           df_SQLStatement_2_out5_temp,
           df_SQLStatement_2_out6_temp,
           df_SQLStatement_2_out7_temp
      ) = SQLStatement_2(context, in0, in1, in2, in3, in4, in5, in6, in7)
      (df_SQLStatement_2_out_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "CCA5-WPAQnAwgbk6UrXbb$$z5bpzAkmpH2xbd8cR-Adq"
       ),
       df_SQLStatement_2_out1_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "SimlS8Mh1BlFcKD42qPnu$$LN6_4dzk4V4GZsUrLdmvW"
       ),
       df_SQLStatement_2_out2_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "AnrZMFKx1FALk1sohV_RA$$ySUKNJ6rfqUP-fsC_uTmp"
       ),
       df_SQLStatement_2_out3_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "-xloJZ5VJRyW7cTmyRsze$$_Y73YAqrjyrC2hqfG_t5D"
       ),
       df_SQLStatement_2_out4_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "_iE2tTM3aYTZXxeinS8og$$ziX8ZtQzMjwPBm9YO81xW"
       ),
       df_SQLStatement_2_out5_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "oACdu68G03bN_p6KrCUEo$$ma-6ZWhbLDVuK1lua9A-Y"
       ),
       df_SQLStatement_2_out6_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "W6pVKl_mRQVBAu6Nd1DqC$$KSzS0eGWxb7EYPpNscAF7"
       ),
       df_SQLStatement_2_out7_temp.interim(
         "Subgraph_2",
         "cQbbbHe1NUOIFfp5zjJCf$$wUhqDslAVr9eJ_7yoFqia",
         "SjiJXaYVMxUVDGom5KYPT$$Xfns4mBUysHdWe2t5fpDw"
       )
      )
    }
    val df_Reformat_3 = Reformat_3(context, df_SQLStatement_2_out7).interim(
      "Subgraph_2",
      "eafn5QfSrcZtetv4l8YqO$$BBmloMed8GSlIa7dkXNP3",
      "lDvVye16n8s3c_OlWs194$$nczvYQjGe2RSgVsWX6Qxv"
    )
    (df_SQLStatement_2_out,
     df_SQLStatement_2_out1,
     df_SQLStatement_2_out2,
     df_SQLStatement_2_out3,
     df_SQLStatement_2_out4,
     df_SQLStatement_2_out5,
     df_SQLStatement_2_out6,
     df_Reformat_3
    )
  }

}
