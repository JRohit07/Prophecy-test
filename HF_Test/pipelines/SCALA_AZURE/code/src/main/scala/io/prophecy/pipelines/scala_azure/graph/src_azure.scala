package io.prophecy.pipelines.scala_azure.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scala_azure.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object src_azure {

  def apply(context: Context): DataFrame =
    context.spark.read
      .format("csv")
      .option("header", true)
      .option("sep",    ",")
      .schema(
        StructType(
          Array(
            StructField("order_id",       IntegerType, true),
            StructField("customer_id",    IntegerType, true),
            StructField("order_status",   StringType,  true),
            StructField("order_category", StringType,  true),
            StructField("order_date",     StringType,  true),
            StructField("amount",         DoubleType,  true)
          )
        )
      )
      .load(
        "dbfs:/Prophecy/abhisheks+azure1@prophecy.io/OrdersDatasetInput.csv"
      )

}
