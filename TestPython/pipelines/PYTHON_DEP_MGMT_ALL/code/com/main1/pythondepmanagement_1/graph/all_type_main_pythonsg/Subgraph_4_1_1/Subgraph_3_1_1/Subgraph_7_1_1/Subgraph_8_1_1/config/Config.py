from com.main1.pythondepmanagement_1.graph.all_type_main_pythonsg.Subgraph_4_1_1.Subgraph_3_1_1.Subgraph_7_1_1\
    .Subgraph_8_1_1\
    .Subgraph_9_1_1\
    .config\
    .Config import SubgraphConfig as Subgraph_9_1_1_Config
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            c_dbsecrets: str="qasecrets_mysql:username",
            c_string: str="test",
            Subgraph_9_1_1: dict={},
            c_orderby: str="`c-string`",
            **kwargs
    ):

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.Subgraph_9_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_9_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_9_1_1, 
            Subgraph_9_1_1_Config
        )
        self.c_orderby = c_orderby
        pass

    def update(self, updated_config):
        self.c_dbsecrets = updated_config.c_dbsecrets
        self.c_string = updated_config.c_string
        self.Subgraph_9_1_1 = updated_config.Subgraph_9_1_1
        self.c_orderby = updated_config.c_orderby
        pass

Config = SubgraphConfig()
