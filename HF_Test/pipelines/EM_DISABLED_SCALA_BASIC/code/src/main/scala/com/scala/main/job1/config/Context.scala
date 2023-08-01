package com.scala.main.job1.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
