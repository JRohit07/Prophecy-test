package io.prophecy.pipelines.pipeline_with_configs.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(
  var JDBC_USER_SECRET_databricks: SecretValue = SecretValue(
    providerType = Some("Databricks"),
    secretScope = Some("rohit_mysql"),
    secretKey = Some("username")
  ),
  var JDBC_PASSWORD_SECRET_databricks: SecretValue = SecretValue(
    providerType = Some("Databricks"),
    secretScope = Some("rohit_mysql"),
    secretKey = Some("password")
  ),
  var jdbc_url_databricks: SecretValue = SecretValue(
    providerType = Some("Databricks"),
    secretScope = Some("qasecrets"),
    secretKey = Some("JDBC_URL")
  ),
  var JDBC_USER_SECRET_hashicorp: SecretValue = SecretValue(
    providerType = Some("HashiCorp"),
    secretScope = Some("secrets/qa"),
    secretKey = Some("JDBC_USERNAME")
  ),
  var JDBC_PASSWORD_SECRET_hashicorp: SecretValue = SecretValue(
    providerType = Some("HashiCorp"),
    secretScope = Some("secrets/qa"),
    secretKey = Some("JDBC_PASSWORD")
  ),
  var JDBC_URL_SECRET_hashicorp: SecretValue = SecretValue(
    providerType = Some("HashiCorp"),
    secretScope = Some("secrets/qa"),
    secretKey = Some("JDBC_URL")
  )
) extends ConfigBase
