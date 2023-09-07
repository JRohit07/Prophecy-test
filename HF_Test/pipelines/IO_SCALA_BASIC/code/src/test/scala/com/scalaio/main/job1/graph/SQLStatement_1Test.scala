package com.scalaio.main.job1.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import com.scalaio.main.job1.config._
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
class SQLStatement_1Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfIn0 = createDfFromResourceFiles(
      spark,
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/in0/schema.json",
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/in0/data/unit_test_0.json",
      "in0"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/out/schema.json",
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/out/data/unit_test_0.json",
      "out"
    )

    val dfOutComputed =
      com.scalaio.main.job1.graph.SQLStatement_1(context, dfIn0)
    val res = assertDFEquals(
      dfOut.select("c   short  --",
                   "c-int-column type",
                   "-- c-long",
                   "c-decimal",
                   "c  float",
                   "c--boolean",
                   "c- - -double",
                   "c___-- string",
                   "c  date",
                   "c_timestamp"
      ),
      dfOutComputed.select("c   short  --",
                           "c-int-column type",
                           "-- c-long",
                           "c-decimal",
                           "c  float",
                           "c--boolean",
                           "c- - -double",
                           "c___-- string",
                           "c  date",
                           "c_timestamp"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msg = if (res.isLeft) res.left.get.getMessage else ""
    Assert.assertTrue(msg, res.isRight)
  }

  test("Unit Test 1") {

    val dfIn0 = createDfFromResourceFiles(
      spark,
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/in0/schema.json",
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/in0/data/unit_test_1.json",
      "in0"
    )
    val dfOut = createDfFromResourceFiles(
      spark,
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/out/schema.json",
      "/data/com/scalaio/main/job1/graph/SQLStatement_1/out/data/unit_test_1.json",
      "out"
    )

    val dfOutComputed =
      com.scalaio.main.job1.graph.SQLStatement_1(context, dfIn0)
    val res = assertDFEquals(
      dfOut.select("c   short  --",
                   "c-int-column type",
                   "-- c-long",
                   "c-decimal",
                   "c  float",
                   "c--boolean",
                   "c- - -double",
                   "c___-- string",
                   "c  date",
                   "c_timestamp"
      ),
      dfOutComputed.select("c   short  --",
                           "c-int-column type",
                           "-- c-long",
                           "c-decimal",
                           "c  float",
                           "c--boolean",
                           "c- - -double",
                           "c___-- string",
                           "c  date",
                           "c_timestamp"
      ),
      maxUnequalRowsToShow,
      1.0
    )
    val msg = if (res.isLeft) res.left.get.getMessage else ""
    Assert.assertTrue(msg, res.isRight)
  }

  override def beforeAll() = {
    super.beforeAll()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerAllUDFs(spark)

    val fabricName = System.getProperty("fabric")

    val config = ConfigurationFactoryImpl.getConfig(
      Array(
        "--confFile",
        getClass
          .getResource(s"/com/scalaio/configs/configs_all/${fabricName}.json")
          .getPath
      )
    )

    context = Context(spark, config)
  }

}
