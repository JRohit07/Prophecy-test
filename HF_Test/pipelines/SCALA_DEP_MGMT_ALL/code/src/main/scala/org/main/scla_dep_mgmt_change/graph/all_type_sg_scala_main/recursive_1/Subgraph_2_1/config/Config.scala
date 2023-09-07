package org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.config

import org.apache.spark.sql._
import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession
import org.main.scla_dep_mgmt_change.graph.all_type_sg_scala_main.recursive_1.Subgraph_2_1.Subgraph_3_1.config.{
  Config => Subgraph_3_1_Config
}

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

case class Config(
  Subgraph_3_1:      Subgraph_3_1_Config = Subgraph_3_1_Config(),
  c_sg2_1_c_string:  String = "asdas tyes asd $$ asdasd ",
  c_sg2_1_c_int:     Int = -121,
  c_sg2_1_c_boolean: Boolean = false,
  c_sg2_1_c_float:   Float = -10.12f
) extends ConfigBase

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
