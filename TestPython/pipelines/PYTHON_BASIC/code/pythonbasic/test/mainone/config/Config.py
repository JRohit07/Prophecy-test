from pythonbasic.test.mainone.graph.Subgraph_1.config.Config import SubgraphConfig as Subgraph_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, c_string: str=None, Subgraph_1: dict=None, c_int: int=None, **kwargs):
        self.spark = None
        self.update(c_string, Subgraph_1, c_int)

    def update(self, c_string: str="PYTHON_BASIC - DEFAULT", Subgraph_1: dict={}, c_int: int=1, **kwargs):
        prophecy_spark = self.spark
        self.c_string = c_string
        self.Subgraph_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1, 
            Subgraph_1_Config
        )
        self.c_int = self.get_int_value(c_int)
        pass
