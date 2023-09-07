from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0\
        .withColumn("c_array--long", explode_outer("c_array--long"))\
        .withColumn("c_array-int  _ int", explode_outer("c_array-int  _ int"))\
        .withColumn("-- c_array_timestamp -- ", explode_outer("-- c_array_timestamp -- "))\
        .withColumn("c_array -- float", explode_outer("c_array -- float"))\
        .withColumn("c_struct -- _  -c_array_int - of a struct ", explode_outer("c_struct -- _  .c_array_int - of a struct "))\
        .columns
    selectCols = [col(
                    "c_struct -- _  -c_string - of a struct -- _"
                  ) if "c_struct -- _  -c_string - of a struct -- _" in flt_col else col("c_struct -- _  .c_string - of a struct -- _")\
                    .alias("c_struct -- _  -c_string - of a struct -- _"),                   col(
                    "c_struct -- _  -c_array_int - of a struct "
                  ) if "c_struct -- _  -c_array_int - of a struct " in flt_col else col("c_struct -- _  .c_array_int - of a struct ")\
                    .alias("c_struct -- _  -c_array_int - of a struct "),                   col("c_array--long") if "c_array--long" in flt_col else col("c_array--long"),                   col("c_array-int  _ int") if "c_array-int  _ int" in flt_col else col("c_array-int  _ int"),                   col("-- c_array_timestamp -- ") if "-- c_array_timestamp -- " in flt_col else col("-- c_array_timestamp -- "),                   col("c_array -- float") if "c_array -- float" in flt_col else col("c_array -- float")]

    return in0\
        .withColumn("c_array--long", explode_outer("c_array--long"))\
        .withColumn("c_array-int  _ int", explode_outer("c_array-int  _ int"))\
        .withColumn("-- c_array_timestamp -- ", explode_outer("-- c_array_timestamp -- "))\
        .withColumn("c_array -- float", explode_outer("c_array -- float"))\
        .withColumn("c_struct -- _  -c_array_int - of a struct ", explode_outer("c_struct -- _  .c_array_int - of a struct "))\
        .select(*selectCols)
