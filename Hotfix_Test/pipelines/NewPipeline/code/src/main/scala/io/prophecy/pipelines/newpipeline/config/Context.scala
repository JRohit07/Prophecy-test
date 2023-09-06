package io.prophecy.pipelines.newpipeline.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
