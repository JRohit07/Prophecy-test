from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, _config_check: str=None, **kwargs):
        self.spark = None
        self.update(_config_check)

    def update(self, _config_check: str="old_value", **kwargs):
        prophecy_spark = self.spark
        self._config_check = _config_check
        pass
