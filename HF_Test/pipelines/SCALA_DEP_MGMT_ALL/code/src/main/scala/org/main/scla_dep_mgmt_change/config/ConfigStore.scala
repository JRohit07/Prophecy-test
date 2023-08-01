package org.main.scla_dep_mgmt_change.config

import org.apache.spark.sql._
import org.main.scla_dep_mgmt_change.config.Context
import pureconfig.ConfigReader.Result
import pureconfig._
import pureconfig.generic.ProductHint
import pureconfig.generic.auto._
import io.prophecy.libs._

object ConfigStore {
  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

object ConfigurationFactoryImpl extends ConfigurationFactory[Config] {

  override protected def load(
    fileConfig: ConfigObjectSource
  ): Result[Config] = {
    implicit val confHint: ProductHint[Config] =
      ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))
    fileConfig.load[Config]
  }

  def getConfig(args: Array[String]) =
    fromCLI(args,
            "rel_sc_pip_dep_mgmt_all.conf",
            "org/main/configsall/scla_dep_mgmt_change/configs_main"
    )

}
