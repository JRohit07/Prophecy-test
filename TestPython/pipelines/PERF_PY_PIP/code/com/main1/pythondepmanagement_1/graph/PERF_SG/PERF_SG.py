from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def PERF_SG(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    Config.update(config)
    df_Source_1_1_1_1 = Source_1_1_1_1(spark)
    df_Source_1_1_1_1 = collectMetrics(
        spark, 
        df_Source_1_1_1_1, 
        "PERF_SG", 
        "m8WouEve-n6lqpAkBphlf$$8GKjZDCDrFR3UeHTGQJ2f", 
        "zSU_5lMgy5pPkCuHBjaUu$$uhYpeHTVZi3ewV-TPQZtp"
    )
    df_Limit_1 = Limit_1(spark, df_Source_1_1_1_1)
    df_Limit_1 = collectMetrics(
        spark, 
        df_Limit_1, 
        "PERF_SG", 
        "9t9uBAVzKDb-tSNNpWI0d$$YYMun3nyz_bviDahQKNNw", 
        "oh91qUECznAyrQeFO6DmR$$0oqb5NKxb4IonbUZHaZUF"
    )
    df_Limit_2 = Limit_2(spark, in0)
    df_Limit_2 = collectMetrics(
        spark, 
        df_Limit_2, 
        "PERF_SG", 
        "2WXD7I_vY2oNSIPC47xJC$$3CGx8zYIAXUuCMY_DB_1N", 
        "Xt8hM5Le46iybvle0JU5B$$6kbr-iMYGFNGdE8yManKk"
    )
    df_Join_1 = Join_1(spark, df_Limit_1, df_Limit_2)
    df_Join_1 = collectMetrics(
        spark, 
        df_Join_1, 
        "PERF_SG", 
        "7SjF_bwe-oeO2e_dDOyFN$$iICNu5mFd7pzjtz_No_K3", 
        "lHMTh3JIu52n_EWbNUnqy$$6CT796REyyqO5hXF0hWOS"
    )
    df_Limit_1_1_1_1 = Limit_1_1_1_1(spark, df_Join_1)
    df_Limit_1_1_1_1 = collectMetrics(
        spark, 
        df_Limit_1_1_1_1, 
        "PERF_SG", 
        "bNS1jT6xxMQsp5Ei9Jl00$$QSdQUJCVDpk3cK5A_mdrg", 
        "kHMIQG-RHPwK6i6EY0mL4$$Cb_NMnhJ1wBn1PcZeEo-g"
    )
    df_Filter_1_1_1_1 = Filter_1_1_1_1(spark, df_Limit_1_1_1_1)
    df_Filter_1_1_1_1 = collectMetrics(
        spark, 
        df_Filter_1_1_1_1, 
        "PERF_SG", 
        "Ce-5OjZ40TeLYTcll_Brx$$CkBpSCfGaLmbkZ5ugIAQy", 
        "9S1f72FcXKLu4Yz0CvnrU$$gjviW8hJUxwVgdaNPkpcz"
    )
    df_OrderBy_1_1_1_1 = OrderBy_1_1_1_1(spark, df_Filter_1_1_1_1)
    df_OrderBy_1_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_1_1_1_1, 
        "PERF_SG", 
        "E8ocUqW_L-LZRJKDolarl$$fUGlJQhdG_P7udEjMaqvS", 
        "6y8v6up-aLCcDvwwn9MtV$$uR8R-H_dOplS2oSVC0RnD"
    )
    df_Aggregate_1 = Aggregate_1(spark, df_OrderBy_1_1_1_1)
    df_Aggregate_1 = collectMetrics(
        spark, 
        df_Aggregate_1, 
        "PERF_SG", 
        "76BhqrxKFkiKoPk-hZH5A$$iAmZM2LVMrcrMunDMJI-l", 
        "01NxgFBrURzyagZMZU2Xh$$U5vZVEKeb1zGcPNBXbE6p"
    )
    df_SchemaTransform_1_1_1_1 = SchemaTransform_1_1_1_1(spark, df_Aggregate_1)
    df_SchemaTransform_1_1_1_1 = collectMetrics(
        spark, 
        df_SchemaTransform_1_1_1_1, 
        "PERF_SG", 
        "J8h-zvV8WynAuJs9CsDl6$$SxLVKv_oOjNbd59AZD2jf", 
        "9p9-cMioqTc7Y6nHeKyz6$$PmbzvXlvf9hwnJqqaRqRo"
    )
    df_Deduplicate_1_1_1_1 = Deduplicate_1_1_1_1(spark, df_SchemaTransform_1_1_1_1)
    df_Deduplicate_1_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_1_1_1_1, 
        "PERF_SG", 
        "xKV6T398OK6KLVBTX0-mJ$$nieWqiRb4MudE8XLh9BHh", 
        "EG88iH1ETYOLjvMc6yaoH$$fvgFEf_Ct7qPfKiDedDUh"
    )
    df_Deduplicate_2_1_1_1 = Deduplicate_2_1_1_1(spark, df_SchemaTransform_1_1_1_1)
    df_Deduplicate_2_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_2_1_1_1, 
        "PERF_SG", 
        "T3IR-nGV6zlHntF4nAYze$$in4vvLU_CBxq1sDqKU8s_", 
        "HWEFJQqBtocabXK5rAZBf$$0DSVJ_CGvkFF2gyzFdHm1"
    )
    df_SetOperation_1_1_1_1 = SetOperation_1_1_1_1(spark, df_Deduplicate_1_1_1_1, df_Deduplicate_2_1_1_1)
    df_SetOperation_1_1_1_1 = collectMetrics(
        spark, 
        df_SetOperation_1_1_1_1, 
        "PERF_SG", 
        "RMpBTtc4OQvIQ1m8yPoOm$$2kFeOK7h-LoVP9IA1xtK_", 
        "gsnmUAyxOzqTMj_uHd7i2$$aEXEGh_MbEbIoFxRPJAPx"
    )
    df_WindowFunction_1 = WindowFunction_1(spark, df_SetOperation_1_1_1_1)
    df_WindowFunction_1 = collectMetrics(
        spark, 
        df_WindowFunction_1, 
        "PERF_SG", 
        "SzGMlhyH-D-ClupoYSuZK$$Anj9YtZcezZf6zHa7zVfK", 
        "9dC2HNUsBy5rfE-af-R4O$$_5xprrHz9aPvn7PuHGufD"
    )
    df_Repartition_1_1_1_1 = Repartition_1_1_1_1(spark, df_Limit_1_1_1_1)
    df_Repartition_1_1_1_1 = collectMetrics(
        spark, 
        df_Repartition_1_1_1_1, 
        "PERF_SG", 
        "hvh6iIjk6zGZgXAute5j_$$pGS_-4fwWzWtXetaT0j8s", 
        "8sI_IyUQBYhf8dDMsUoRw$$VxRnmpV8mBP-CyufUITBU"
    )
    df_RowDistributor_1_1_1_1_out0, df_RowDistributor_1_1_1_1_out1 = RowDistributor_1_1_1_1(
        spark, 
        df_Repartition_1_1_1_1
    )
    df_RowDistributor_1_1_1_1_out0 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_1_out0, 
        "PERF_SG", 
        "nXQabxsNzXyGx8PXdf2SG$$bJMLUEzpfNyloUGcrks-D", 
        "7Kq6AndFgiVLRdbFCMqKI$$0aWUbb0ENArE52e_QKJjP"
    )
    df_RowDistributor_1_1_1_1_out1 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_1_out1, 
        "PERF_SG", 
        "nXQabxsNzXyGx8PXdf2SG$$bJMLUEzpfNyloUGcrks-D", 
        "3OS9j6PuYO3pmRjgbyvKe$$QrII0P4qdgD_Dsy3IsBmS"
    )
    df_PERF_SG_REFORMAT = PERF_SG_REFORMAT(spark, in1)
    df_PERF_SG_REFORMAT = collectMetrics(
        spark, 
        df_PERF_SG_REFORMAT, 
        "PERF_SG", 
        "bg4A214VFrlwp6WMWy6MN$$o0pf5GNgFQBL6VCFDl0jd", 
        "BKZ13uQEpVglB6nKDxJqy$$7GG-L9tlcZ7JBvxPg1TIt"
    )
    df_Limit_3_1_1_1 = Limit_3_1_1_1(spark, df_PERF_SG_REFORMAT)
    df_Limit_3_1_1_1 = collectMetrics(
        spark, 
        df_Limit_3_1_1_1, 
        "PERF_SG", 
        "XfpUWAMN_e43io1QnRIkN$$sDeJAD904RUJ6UvmBvuPn", 
        "b74t6GxTqgdE0dK2_13P4$$d4TP11SKh4GOe8c3Ymo1d"
    )
    df_Subgraph_4_1_1_1 = Subgraph_4_1_1_1(
        spark, 
        config.Subgraph_4_1_1_1, 
        df_RowDistributor_1_1_1_1_out0, 
        df_RowDistributor_1_1_1_1_out1, 
        df_Limit_3_1_1_1
    )
    df_Script_1_1_1_1 = Script_1_1_1_1(spark, df_WindowFunction_1)
    df_Script_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_1_1_1_1, 
        "PERF_SG", 
        "tT3hEVBSutvBwJCS5HvMR$$fLBqzP_9R9n6zG8uBKA8q", 
        "BFHu_2vEu-YZyPEyYSShP$$1cMAvczmADh2eMRC1VsbL"
    )
    df_Script_1_1_1_1.cache().count()
    df_Script_1_1_1_1.unpersist()
    df_OrderBy_3_1_1_1 = OrderBy_3_1_1_1(spark, in2)
    df_OrderBy_3_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_3_1_1_1, 
        "PERF_SG", 
        "mOMQl_-GfuQoqVlMPl6_a$$3ctmRZyqUsUTI1Iy9ctPi", 
        "xLtEx1DsPfG0cpI0KOpd-$$5SMZjwwiJTZ2_0qSBxseJ"
    )
    df_Deduplicate_3_1_1_1 = Deduplicate_3_1_1_1(spark, df_OrderBy_3_1_1_1)
    df_Deduplicate_3_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_3_1_1_1, 
        "PERF_SG", 
        "IYXl13dFEPTPYeMJ4S9vt$$YMTntVomJ400U2izq-UdM", 
        "X9vnqgtG0dZfZ6jzWbuG5$$hEvIlIVygGkPfFgAM3DuX"
    )

    return df_Subgraph_4_1_1_1, df_Limit_3_1_1_1, df_Deduplicate_3_1_1_1
