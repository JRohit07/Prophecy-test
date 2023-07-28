from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Script_5(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from scipy.special import cbrt
    cb = cbrt([27, 64])
    print(cb)
    import torch
    import math
    dtype = torch.float
    device = torch.device("cpu")
    x = torch.linspace(- math.pi, math.pi, 2000, device = device, dtype = dtype)
    y = torch.sin(x)
    a = torch.randn((), device = device, dtype = dtype)
    print(a)
    out0 = in0

    return out0
