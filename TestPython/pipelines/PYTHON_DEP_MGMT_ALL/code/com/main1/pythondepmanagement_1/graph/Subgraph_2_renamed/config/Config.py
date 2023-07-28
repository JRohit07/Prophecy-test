from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, c_sg2_config1: str="terasdasdasd ", **kwargs):
        self.c_sg2_config1 = c_sg2_config1
        pass

    def update(self, updated_config):
        self.c_sg2_config1 = updated_config.c_sg2_config1
        pass

Config = SubgraphConfig()
