package org.main.scla_dep_mgmt.graph.all_type_scala_sg_1

import io.prophecy.libs._
import org.main.scla_dep_mgmt.udfs.UDFs._
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object WindowFunction_1_1 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    import org.apache.spark.sql.expressions.{Window, WindowSpec}
    in.withColumn(
        "c -  boolean _  ",
        row_number().over(
          Window
            .partitionBy(col("`c- short`"),       col("`c  - int`"))
            .orderBy(col("`c_decimal  -  `").asc, col("`c_float-__  `").asc)
        )
      )
      .withColumn(
        "c_double",
        row_number().over(
          Window
            .partitionBy(col("`c- short`"),       col("`c  - int`"))
            .orderBy(col("`c_decimal  -  `").asc, col("`c_float-__  `").asc)
        )
      )
      .withColumn(
        "c-string",
        row_number().over(
          Window
            .partitionBy(col("`c- short`"),       col("`c  - int`"))
            .orderBy(col("`c_decimal  -  `").asc, col("`c_float-__  `").asc)
        )
      )
  }

}
