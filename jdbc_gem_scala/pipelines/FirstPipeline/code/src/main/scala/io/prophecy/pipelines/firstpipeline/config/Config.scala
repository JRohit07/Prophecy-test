package io.prophecy.pipelines.firstpipeline.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(
  var JDBC_URL:             Option[String] = None,
  var JDBC_TABLE:           Option[String] = None,
  var SQL_QUERY:            String = "select * from test_table",
  var SQL_CONFIG_QUERY:     String = "select * from ${SQL_QUERY}",
  var DRIVER_NAME:          String = "com.mysql.jdbc.Driver",
  var JDBC_USER_SECRET:     Option[DatabricksSecret] = None,
  var JDBC_PASSWORD_SECRET: Option[DatabricksSecret] = None,
  var JDBC_USER_STRING:     String = "test_user",
  var JDBC_PASSWORD_STRING: String = "admin",
  var ENV_JDBC_USERNAME:    String = "JDBC_USERNAME",
  var ENV_JDBC_PASSWORD:    Option[String] = None,
  var ENV_JDBC_URL:         String = "JDBC_URL",
  var TARGET_TABLE:         String = "test_table_destination",
  var SOURCE_TABLE:         Option[String] = None
) extends ConfigBase

object DatabricksSecret {

  implicit val myIntReader: ConfigReader[DatabricksSecret] =
    ConfigReader[String].map { s =>
      val Array(scope, key) = s.split(":")
      DatabricksSecret(scope, key)
    }

}

case class DatabricksSecret(var scope: String, var key: String) {

  override def toString: String = {
    import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
    dbutils.secrets.get(scope = scope, key = key)
  }

}
