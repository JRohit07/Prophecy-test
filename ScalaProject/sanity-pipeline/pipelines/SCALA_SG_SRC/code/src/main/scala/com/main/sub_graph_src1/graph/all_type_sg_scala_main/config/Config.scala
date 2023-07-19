package com.main.sub_graph_src1.graph.all_type_sg_scala_main.config

import org.apache.spark.sql._
import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.recursive_1.config.{
  Config => recursive_1_Config
}

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

case class Config(
  recursive_1:    recursive_1_Config = recursive_1_Config(),
  c_sg1_c_string: String = "this is a test",
  c_sg1_c_bool:   Boolean = true,
  c_sg1_c_double: Double = 1.23214123e8d,
  c_sg1_c_float:  Float = 2343.4233f,
  c_sg1_c_int:    Int = 12312,
  c_sg1_c_long:   Long = 23432423423L,
  c_sg1_c_short:  Short = 21,
  c_sg1_c_array_string: List[String] =
    List("value1this is not $$ son $$$$#-1(2)", "value2$$this is son"),
  c_sg1_c_record: C_sg1_c_record = C_sg1_c_record(),
  c_sg1_c_db_secrets: DatabricksSecret =
    DatabricksSecret(scope = "qasecrets_mysql", key = "username"),
  c_sg1_c_spark_expression: String = "concat('a', 'b', 'c', 'd')",
  c_sg1_c_limit:            Int = 15,
  c_sg1_c_orderby: String =
    "concat(`c- short`, `c -  boolean _  `, `c-string`, `c  - int`)",
  c_sg1_c_rowdistributor:    String = "`c- short` > -10",
  c_sg1_join_expr_timestamp: String = "in0.`c_timestamp  __ for--today`",
  c_sg1_aggregate:           String = "first(`- c long`)"
) extends ConfigBase

object C_sg1_c_record {

  implicit val confHint: ProductHint[C_sg1_c_record] =
    ProductHint[C_sg1_c_record](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_sg1_c_record(
  c_sg1_c_record_c_bool:             Boolean = false,
  c_sg1_c_record_c_string:           String = "this is another $$ value some-1(1)",
  c_sg1_c_record_c_spark_expression: String = "concat('a', 'b')",
  c_sg1_c_record_c_db_secrets: DatabricksSecret =
    DatabricksSecret(scope = "qasecrets_mysql", key = "username")
)

object DatabricksSecret {

  implicit val myIntReader: ConfigReader[DatabricksSecret] =
    ConfigReader[String].map { s =>
      val Array(scope, key) = s.split(":")
      DatabricksSecret(scope, key)
    }

}

case class DatabricksSecret(scope: String, key: String) {

  override def toString: String = {
    import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
    dbutils.secrets.get(scope = scope, key = key)
  }

}

case class Context(spark: SparkSession, config: Config)
