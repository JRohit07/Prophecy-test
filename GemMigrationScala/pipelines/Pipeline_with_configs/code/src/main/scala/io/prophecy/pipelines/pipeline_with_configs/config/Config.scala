package io.prophecy.pipelines.pipeline_with_configs.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(
  var JDBC_USER_SECRET: DatabricksSecret =
    DatabricksSecret(scope = "rohit_mysql", key = "username"),
  var JDBC_PASSWORD_SECRET: DatabricksSecret =
    DatabricksSecret(scope = "rohit_mysql", key = "password")
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
