from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, c_sg2_c_string: str="sdasdasdasd", **kwargs):
        self.c_sg2_c_string = c_sg2_c_string
        pass

    def update(self, updated_config):
        self.c_sg2_c_string = updated_config.c_sg2_c_string
        pass

Config = SubgraphConfig()
