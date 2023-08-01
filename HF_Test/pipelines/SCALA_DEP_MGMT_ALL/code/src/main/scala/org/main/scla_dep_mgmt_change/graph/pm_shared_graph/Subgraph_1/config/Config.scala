package org.main.scla_dep_mgmt_change.graph.pm_shared_graph.Subgraph_1.config

import org.apache.spark.sql._
import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

case class Config(var2: Float = 2.1f) extends ConfigBase
case class Context(spark: SparkSession, config: Config)
