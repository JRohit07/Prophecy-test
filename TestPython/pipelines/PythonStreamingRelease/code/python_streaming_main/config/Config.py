from python_streaming_main.graph.all_type_main_1.config.Config import SubgraphConfig as all_type_main_1_Config
from python_streaming_main.graph.Subgraph_1.config.Config import SubgraphConfig as Subgraph_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, all_type_main_1: dict=None, Subgraph_1: dict=None, **kwargs):
        self.spark = None
        self.update(all_type_main_1, Subgraph_1)

    def update(self, all_type_main_1: dict={}, Subgraph_1: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.all_type_main_1 = self.get_config_object(
            prophecy_spark, 
            all_type_main_1_Config(prophecy_spark = prophecy_spark), 
            all_type_main_1, 
            all_type_main_1_Config
        )
        self.Subgraph_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1, 
            Subgraph_1_Config
        )
        pass
