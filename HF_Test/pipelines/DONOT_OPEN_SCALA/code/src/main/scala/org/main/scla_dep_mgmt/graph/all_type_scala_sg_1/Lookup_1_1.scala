package org.main.scla_dep_mgmt.graph.all_type_scala_sg_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config.Context
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Lookup_1_1 {

  def apply(context: Context, in0: DataFrame): Unit =
    createLookup("LookupTest",
                 in0,
                 context.spark,
                 List("customer_id", "first_name"),
                 "last_name",
                 "phone"
    )

}
