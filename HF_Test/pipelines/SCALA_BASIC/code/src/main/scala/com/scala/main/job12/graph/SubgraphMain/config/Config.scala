package com.scala.main.job12.graph.SubgraphMain.config

import org.apache.spark.sql._
import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

case class Config(
  @Description("test_str") c_test: Option[String] = None,
  @Description("array desc") c_array: List[String] =
    List("dasdsad", "sadasdsad", "yes sir", "2yes sir"),
  @Description("record ddesc") c_record3: C_record3 = C_record3(),
  @Description("bool desc") bool:         Boolean = true,
  @Description("double desc") double:     Double = 234324.0d,
  @Description("sewr") record_array:      Record_array = Record_array(),
  @Description("sdf") array_record: List[Array_record] = List(
    Array_record(werw = "332", ewr = List("12", "w"))
  )
) extends ConfigBase

object C_record3 {

  implicit val confHint: ProductHint[C_record3] =
    ProductHint[C_record3](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_record3(@Description("c value record") c_val3: C_val3 = C_val3())

object C_val3 {

  implicit val confHint: ProductHint[C_val3] =
    ProductHint[C_val3](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_val3(@Description("crr desc") crr: String = "asdasdasd")

object Record_array {

  implicit val confHint: ProductHint[Record_array] =
    ProductHint[Record_array](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Record_array(@Description("wer") array: List[String] = List("23"))

object Array_record {

  implicit val confHint: ProductHint[Array_record] =
    ProductHint[Array_record](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Array_record(werw: String, ewr: List[String])
case class Context(spark: SparkSession, config: Config)
