from com.sg_src.main.graph.Subgraph_1.config.Config import SubgraphConfig as Subgraph_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, c_dbsecrets: str=None, c_string: str=None, Subgraph_1: dict=None, **kwargs):
        self.spark = None
        self.update(c_dbsecrets, c_string, Subgraph_1)

    def update(self, c_dbsecrets: str="qasecrets_mysql:username", c_string: str="test", Subgraph_1: dict={}, **kwargs):
        prophecy_spark = self.spark

        if c_dbsecrets is not None:
            self.c_dbsecrets = self.get_dbutils(prophecy_spark).secrets.get(*c_dbsecrets.split(":"))

        self.c_string = c_string
        self.Subgraph_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1, 
            Subgraph_1_Config
        )
        pass
