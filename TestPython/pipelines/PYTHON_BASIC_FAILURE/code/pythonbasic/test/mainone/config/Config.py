from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, c_string: str=None, **kwargs):
        self.spark = None
        self.update(c_string)

    def update(self, c_string: str="test string", **kwargs):
        prophecy_spark = self.spark
        self.c_string = c_string
        pass
