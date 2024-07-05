package io.prophecy.pipelines.firstpipeline.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(
  var JDBC_URL:      String = "jdbc:mysql://3.101.152.38:3306/test_database",
  var JDBC_TABLE:    String = "test_table_automation",
  var JDBC:          String = "jdbc:mysql://3.101.152.38:3306/",
  var JDBC_DATABASE: String = "test_database",
  var DRIVER_NAME:   String = "com.mysql.jdbc.Driver",
  var JDBC_USER_SECRET: DatabricksSecret =
    DatabricksSecret(scope = "rohit_mysql", key = "username"),
  var JDBC_PASSWORD_SECRET: DatabricksSecret =
    DatabricksSecret(scope = "rohit_mysql", key = "password"),
  var JDBC_USER_STRING:     String = "test_user",
  var JDBC_PASSWORD_STRING: String = "admin",
  var ENV_JDBC_USERNAME:    String = "JDBC_USERNAME",
  var ENV_JDBC_PASSWORD:    String = "JDBC_PASSWORD",
  var TEST:                 String = "test",
  var ADM:                  String = "adm",
  var IN:                   String = "in",
  var JDBC_DEST_TABLE:      String = "test_table_destination",
  var USER:                 String = "user"
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
