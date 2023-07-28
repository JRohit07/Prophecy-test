from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def CompareColumns_2(spark: SparkSession, in0: DataFrame, in1: DataFrame) -> DataFrame:
    from pyspark.sql.functions import lit, sum, first, explode_outer, create_map, when, coalesce, col, row_number
    from pyspark.sql.window import Window
    from functools import reduce
    valueColumnsMap = []

    for vColumn in set(in0.columns).difference({"c_short"}):
        valueColumnsMap.extend([lit(vColumn), col(vColumn).cast("string")])

    selectCols = [col("c_short"),                   explode_outer(create_map(*valueColumnsMap))\
                    .alias(
                    "column_name",
                    "##value##"
                  )]
    df1 = in0.select(*selectCols)
    exploded1 = df1.alias("exploded1")
    df2 = in1.select(*selectCols)
    exploded2 = df2.alias("exploded2")
    joined = exploded1\
                 .join(
                   exploded2,
                   reduce(
                     lambda a, c: a & c,
                     [col(f"exploded1.column_name") == col(f"exploded2.column_name"),                       col(f"exploded1.c_short") == col(f"exploded2.c_short")],
                     lit(True)
                   ),
                   "full_outer"
                 )\
                 .select(
                   coalesce(col(f"exploded1.column_name"), col(f"exploded2.column_name")).alias("column_name"), 
                   coalesce(col(f"exploded1.c_short"), col(f"exploded2.c_short")).alias("c_short"), 
                   col(
                       f"exploded1.##value##"
                     )\
                     .alias(
                     "##left_value##"
                   ), 
                   col(
                       f"exploded2.##value##"
                     )\
                     .alias(
                     "##right_value##"
                   )
                 )\
                 .withColumn(
                   "match_count",
                   when(
                       coalesce(
                         (
                           col("##left_value##")
                           == col(
                             "##right_value##"
                           )
                         ),
                         (
                           col(
                               "##left_value##"
                             )\
                             .isNull()
                           & col(
                               "##right_value##"
                             )\
                             .isNull()
                         )
                       ),
                       lit(1)
                     )\
                     .otherwise(lit(0))
                 )\
                 .withColumn(
        "mismatch_count",
        when(
            coalesce(
              (
                col("##left_value##")
                != col(
                  "##right_value##"
                )
              ),
              ~ (
                col(
                    "##left_value##"
                  )\
                  .isNull()
                & col(
                    "##right_value##"
                  )\
                  .isNull()
              )
            ),
            lit(1)
          )\
          .otherwise(lit(0))
                 )
    mismatchExamples = joined\
                           .filter(col("mismatch_count").__gt__(lit(0)))\
                           .withColumn(
                             "##row_number###",
                             row_number()\
                               .over(Window.partitionBy(col("column_name"), col("c_short")).orderBy(col("c_short")))
                           )\
                           .filter(
                             (
                               col("##row_number###")
                               == lit(1)
                             )
                           )\
                           .select(
                             col("column_name"), 
                             col("c_short"), 
                             lit(0).alias("match_count"), 
                             lit(0).alias("mismatch_count"), 
                             col(
                                 "##left_value##"
                               )\
                               .alias("mismatch_example_left"), 
                             col(
                                 "##right_value##"
                               )\
                               .alias("mismatch_example_right")
                           )\
                           .dropDuplicates(["column_name"])

    return joined\
        .drop(
          "##left_value##"
        )\
        .drop(
          "##right_value##"
        )\
        .withColumn("mismatch_example_left", lit(None))\
        .withColumn("mismatch_example_right", lit(None))\
        .union(mismatchExamples)\
        .groupBy("column_name")\
        .agg(
          sum("match_count").alias("match_count"), 
          sum("mismatch_count").alias("mismatch_count"), 
          first(col("mismatch_example_left"), ignorenulls = True).alias("mismatch_example_left"), 
          first(col("mismatch_example_right"), ignorenulls = True).alias("mismatch_example_right"), 
          first(
              when(coalesce(col("mismatch_example_left"), col("mismatch_example_right")).isNotNull(), col("c_short"))\
                .otherwise(lit(None)),
              ignorenulls = True
            )\
            .alias("mismatch_example_c_short")
        )\
        .orderBy(col("mismatch_count").desc(), col("column_name"))
