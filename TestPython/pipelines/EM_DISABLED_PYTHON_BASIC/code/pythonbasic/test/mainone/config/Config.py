from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, c_string: str=None, c_int: int=None, **kwargs):
        self.spark = None
        self.update(c_string, c_int)

    def update(self, c_string: str="test string", c_int: int=1, **kwargs):
        prophecy_spark = self.spark
        self.c_string = c_string
        self.c_int = self.get_int_value(c_int)
        pass
