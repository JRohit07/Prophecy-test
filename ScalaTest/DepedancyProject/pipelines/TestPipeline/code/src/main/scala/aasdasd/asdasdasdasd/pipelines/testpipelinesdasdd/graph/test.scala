package aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.graph

import io.prophecy.libs._
import aasdasd.asdasdasdasd.pipelines.testpipelinesdasdd.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object test {

  def apply(context: Context): DataFrame =
    context.spark.read
      .format("csv")
      .option("header",                         true)
      .option("sep",                            ",")
      .schema(StructType(Array(StructField("a", StringType, true))))
      .load("dbfs:/tmp/random/rohite2e")

}
