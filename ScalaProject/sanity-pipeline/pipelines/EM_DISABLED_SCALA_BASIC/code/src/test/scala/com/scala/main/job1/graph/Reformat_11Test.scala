package com.scala.main.job1.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import com.scala.main.job1.config._
import io.prophecy.libs.registerAllUDFs
import io.prophecy.libs.SparkTestingUtils._
import org.apache.spark.sql.types._
import org.apache.spark.sql.{Column, DataFrame}
import org.apache.spark.sql.functions._
import org.junit.runner.RunWith
import org.junit.Assert
import org.scalatest.FunSuite
import java.time.LocalDateTime
import org.scalatest.junit.JUnitRunner
import java.sql.{Date, Timestamp}
import scala.collection.JavaConverters._
import java.nio.file.{Files, Paths}
import java.math.BigDecimal

@RunWith(classOf[JUnitRunner])
class Reformat_11Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfIn = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/Reformat_11/in/schema.json",
      "/data/com/scala/main/job1/graph/Reformat_11/in/data/unit_test_0.json",
      "in"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/Reformat_11/out/schema.json",
      "/data/com/scala/main/job1/graph/Reformat_11/out/data/unit_test_0.json",
      "out"
    )

    val dfOutComputed = com.scala.main.job1.graph.Reformat_11(context, dfIn)

  }

  test("Unit Test 1") {

    val dfIn = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/Reformat_11/in/schema.json",
      "/data/com/scala/main/job1/graph/Reformat_11/in/data/unit_test_1.json",
      "in"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/Reformat_11/out/schema.json",
      "/data/com/scala/main/job1/graph/Reformat_11/out/data/unit_test_1.json",
      "out"
    )

    val dfOutComputed = com.scala.main.job1.graph.Reformat_11(context, dfIn)

  }

  override def beforeAll() = {
    super.beforeAll()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerAllUDFs(spark)

    val fabricName = System.getProperty("fabric")

    val config = ConfigurationFactoryImpl.getConfig(
      Array("--confFile",
            getClass.getResource(s"/config/${fabricName}.json").getPath
      )
    )

    context = Context(spark, config)
  }

}
