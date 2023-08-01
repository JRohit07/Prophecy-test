package com.scala.main.job12.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
