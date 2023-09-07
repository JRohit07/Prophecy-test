package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.PipelineInitCode._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object WindowFunction_1 {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    import org.apache.spark.sql.expressions.{Window, WindowSpec}
    in.withColumn(
        "c_date-for today",
        expr(Config.c_row).over(
          Window
            .partitionBy(lit(Config.c_short),
                         col("`c  - int`"),
                         col("`- c long`")
            )
            .orderBy(col("`c_float-__  `").asc,
                     lit(Config.c_bool).desc,
                     col("c_double").asc,
                     col("`c-string`").asc
            )
        )
      )
      .withColumn(
        "c_timestamp  __ for--today",
        row_number().over(
          Window
            .partitionBy(lit(Config.c_short),
                         col("`c  - int`"),
                         col("`- c long`")
            )
            .orderBy(col("`c_float-__  `").asc,
                     lit(Config.c_bool).desc,
                     col("c_double").asc,
                     col("`c-string`").asc
            )
        )
      )
  }

}
