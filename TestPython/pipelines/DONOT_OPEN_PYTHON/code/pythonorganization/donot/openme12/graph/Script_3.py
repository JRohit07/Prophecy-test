from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Script_3(
        spark: SparkSession, 
        in0: DataFrame, 
        in1: DataFrame, 
        in2: DataFrame, 
        in3: DataFrame, 
        in4: DataFrame, 
        in5: DataFrame, 
        in6: DataFrame
) -> DataFrame:
    """
This is a comment
"""
    '''
This is another comment
'''
    ## FINAL SINGLE LINE COMMENT ####
    from pyspark.sql.types import DoubleType
    import requests
    URL = "https://www.geeksforgeeks.org/data-structures/"
    r = requests.get(URL)
    print(r.content)
    import matplotlib.pyplot as plt
    import numpy as np
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])
    plt.plot(xpoints, ypoints)
    import pandas as pd
    data = {
"calories" : [420, 380, 390], "duration" : [50, 40, 45]}
    df = pd.DataFrame(data)
    print(df)
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    from scipy.special import cbrt
    cb = cbrt([27, 64])
    print(cb[0])
    import torch
    import math
    dtype = torch.float
    device = torch.device("cpu")
    x = torch.linspace(- math.pi, math.pi, 2000, device = device, dtype = dtype)
    y = torch.sin(x)
    a = torch.randn((), device = device, dtype = dtype)
    print(a)
    out00 = in0.select("c_int").withColumnRenamed("c_int", "c_int_new")
    out1 = in1.select("c_int").withColumnRenamed("c_int", "c_int_new")
    out2 = in2.select("c_int").withColumnRenamed("c_int", "c_int_new")
    out3 = in3.select("c_int").withColumnRenamed("c_int", "c_int_new")
    out4 = in4\
             .select("customer_id")\
             .withColumn("customer_id", in4["customer_id"].cast(IntegerType()))\
             .withColumnRenamed("customer_id", "c_int_new")
    out5 = in5.select("_c0").withColumnRenamed("_c0", "c_int_new")
    out6 = in6.select("c-int-column type").withColumnRenamed("c-int-column type", "c_int_new")
    out0 = out00.union(out1).union(out2).union(out3).union(out4).union(out5).union(out6)

    return out0
