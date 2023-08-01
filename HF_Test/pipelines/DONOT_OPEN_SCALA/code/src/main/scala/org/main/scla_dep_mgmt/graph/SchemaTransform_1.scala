package org.main.scla_dep_mgmt.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object SchemaTransform_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.withColumn("c_concat_new_short_decimal",
                  concat(col("`c_struct-c_short`"), col("`c_struct-c_decimal`"))
      )
      .drop("c_array_long")
      .withColumnRenamed("c_array_boolean", "c_array_boolean_renamed")

}
