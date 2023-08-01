package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object PERF_WINDOW {

  def apply(context: Context, in: DataFrame): DataFrame = {
    import org.apache.spark.sql.expressions.{Window, WindowSpec}
    in.withColumn("cmls_acct_ctry_cd_drvd",
                  row_number().over(
                    Window
                      .partitionBy(col("cmls_3ds_authntn_mthd"))
                      .orderBy(col("cmls_acct_cobrnd_bus_id_drvd").asc)
                  )
    )
  }

}
