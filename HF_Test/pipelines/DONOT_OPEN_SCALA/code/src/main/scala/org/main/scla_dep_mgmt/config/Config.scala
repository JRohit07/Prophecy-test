package org.main.scla_dep_mgmt.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._
import org.main.scla_dep_mgmt.graph.SubGraph_1.config.{
  Config => SubGraph_1_Config
}
import org.main.scla_dep_mgmt.graph.all_type_scala_sg_1.config.{
  Config => all_type_scala_sg_1_Config
}

case class Config(
  JDBC_USER:           String = "test_user",
  SOURCE_TABLE:        String = "test_table",
  db_secrets:          Option[DatabricksSecret] = None,
  JDBC_URL:            String = "jdbc:mysql://18.144.156.219:3306/test_database",
  JDBC_SOURCE_TABLE:   String = "test_table",
  CONFIG_STR:          String = "jdbc_url-${JDBC_URL}",
  CONFIG_BOOLEAN:      Boolean = true,
  CONFIG_DOUBLE:       Double = 123123.12321321d,
  CONFIG_INT:          Int = 3243423,
  CONFIG_FLOAT:        Float = 3454.3455f,
  SubGraph_1:          SubGraph_1_Config = SubGraph_1_Config(),
  all_type_scala_sg_1: all_type_scala_sg_1_Config = all_type_scala_sg_1_Config()
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
