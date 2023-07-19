package org.main.scla_dep_mgmt.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
