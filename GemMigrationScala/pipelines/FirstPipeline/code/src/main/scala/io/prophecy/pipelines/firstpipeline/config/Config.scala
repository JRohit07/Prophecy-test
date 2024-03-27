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
  var JDBC_USER_SECRET: SecretValue = SecretValue(
    providerType = Some("Databricks"),
    secretScope = Some("rohit_mysql"),
    secretKey = Some("username")
  ),
  var JDBC_PASSWORD_SECRET: SecretValue = SecretValue(
    providerType = Some("Databricks"),
    secretScope = Some("rohit_mysql"),
    secretKey = Some("password")
  ),
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
