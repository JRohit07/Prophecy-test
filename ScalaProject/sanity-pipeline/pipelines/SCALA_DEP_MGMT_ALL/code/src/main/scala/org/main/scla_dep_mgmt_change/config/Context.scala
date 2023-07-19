package org.main.scla_dep_mgmt_change.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
