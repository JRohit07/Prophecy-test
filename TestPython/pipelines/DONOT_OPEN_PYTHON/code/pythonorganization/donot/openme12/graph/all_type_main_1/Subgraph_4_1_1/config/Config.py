from pythonorganization.donot.openme12.graph.all_type_main_1.Subgraph_4_1_1.Subgraph_3_1_1.config.Config import (
    SubgraphConfig as Subgraph_3_1_1_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_string: str="test",
            Subgraph_3_1_1: dict={},
            **kwargs
    ):

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.Subgraph_3_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_3_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_3_1_1, 
            Subgraph_3_1_1_Config
        )
        pass

    def update(self, updated_config):
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_string = updated_config.c_string
        self.Subgraph_3_1_1 = updated_config.Subgraph_3_1_1
        pass

Config = SubgraphConfig()
