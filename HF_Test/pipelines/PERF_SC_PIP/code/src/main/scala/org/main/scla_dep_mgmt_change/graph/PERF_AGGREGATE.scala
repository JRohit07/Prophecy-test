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

object PERF_AGGREGATE {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.groupBy(col("cmls_3ds_authntn_mthd"))
      .agg(first(col("cmls_3ds_authntn_mthd")).as("cmls_3ds_authntn_mthd"),
           first(col("cmls_acct_cobrnd_bus_id_drvd"))
             .as("cmls_acct_cobrnd_bus_id_drvd")
      )

}
