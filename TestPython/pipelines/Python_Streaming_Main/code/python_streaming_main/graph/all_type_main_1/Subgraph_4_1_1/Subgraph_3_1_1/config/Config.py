from python_streaming_main.graph.all_type_main_1.Subgraph_4_1_1.Subgraph_3_1_1.Subgraph_7_1_1.config.Config import (
    SubgraphConfig as Subgraph_7_1_1_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_string: str="test",
            Subgraph_7_1_1: dict={},
            c_sg3_1_1_c_long: int=12212,
            **kwargs
    ):

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.Subgraph_7_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_7_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_7_1_1, 
            Subgraph_7_1_1_Config
        )
        self.c_sg3_1_1_c_long = c_sg3_1_1_c_long
        pass

    def update(self, updated_config):
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_string = updated_config.c_string
        self.Subgraph_7_1_1 = updated_config.Subgraph_7_1_1
        self.c_sg3_1_1_c_long = updated_config.c_sg3_1_1_c_long
        pass

Config = SubgraphConfig()
