package com.main.sub_graph_src1.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._
import com.main.sub_graph_src1.graph.all_type_sg_scala_main.config.{
  Config => all_type_sg_scala_main_Config
}

case class Config(
  all_type_sg_scala_main: all_type_sg_scala_main_Config =
    all_type_sg_scala_main_Config()
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
