from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def Script_4(spark: SparkSession) -> DataFrame:
    #from pyspark.sql.functions import *
    from pyspark.sql.types import (
        StructField,
        ArrayType,
        StructType,
        ShortType,
        IntegerType,
        LongType,
        DecimalType,
        FloatType,
        BooleanType,
        DoubleType,
        StringType,
        DateType,
        TimestampType
    )
    from decimal import Decimal
    import datetime
    schema = StructType([
            StructField("p_short", ShortType(), True),
            StructField("p_int", IntegerType(), True),
            StructField("p_long", LongType(), True),
            StructField("p_decimal", DecimalType(20, 10), True),
            StructField("p_float", FloatType(), True),
            StructField("p_boolean", BooleanType(), True),
            StructField("p_double", DoubleType(), True),
            StructField("p_string", StringType(), True),
            StructField("p_date", DateType(), True),
            StructField("p_timestamp", TimestampType(), True),
            StructField("   c_short   -  ", ShortType(), True),
            StructField("c_int  -  ", IntegerType(), True),
            StructField("c-long", LongType(), True),
            StructField("c  decimal", DecimalType(), True),
            StructField(" - c_float ", FloatType(), True),
            StructField("  c_boolean", BooleanType(), True),
            StructField(" c_double--", DoubleType(), True),
            StructField("--c_string", StringType(), True),
            StructField(" c_date", DateType(), True),
            StructField("-- c_timestamp", TimestampType(), True),
            StructField(" c_array--int  ", ArrayType(IntegerType()), True),
            StructField("c   array_string", ArrayType(StringType()), True),
            StructField("c--array--long", ArrayType(LongType()), True),
            StructField("c-array boolean   ", ArrayType(BooleanType()), True),
            StructField("  c--array---date--", ArrayType(DateType()), True),
            StructField("- c- array- timestamp ", ArrayType(TimestampType()), True),
            StructField("-  c_array_float  -", ArrayType(FloatType()), True),
            StructField("  c-array-decimal  ", ArrayType(DecimalType(15, 2)), True),
            StructField("  c - struct  -  ", StructType([
                StructField(" - c_short  - ", ShortType(), True),
                StructField("-  c_int  -", IntegerType(), True),
                StructField("    c-long    ", LongType(), True),
                StructField("--c_--decimal--", DecimalType(22, 3), True),
                StructField("c float  -  - ", FloatType(), True),
                StructField("-   c_boolean", BooleanType(), True),
                StructField("  c_--double   -", DoubleType(), True),
                StructField("  c-   - string", StringType(), True),
                StructField("- - - c_date - -", DateType(), True),
                StructField("  - c_timestamp  - ", TimestampType(), True),
                StructField("c-array-int-only-1-2-3 4 5", ArrayType(IntegerType()), True)

        ]), True)
    ])
    data = []

    for i in range(1, 100):
        day = (i % 20) + 1
        month = (i % 8) + 1
        year = 1990 + (i % 30)
        data.append(
            (i % 10, i % 12, i % 20, Decimal(i / 10), - i / 5, i % 4 == 0, i * 3 / 7, Config.c_string + str(i * 5),
             datetime.date(year, month, day),
             datetime.datetime(year, month + 2, day + 1, i % 10 + 1, i % 20 + 1, i % 44 + 1, i % 45 + 1),
             10, 6540, 2342374324123, Decimal(12321.123121), - 3123.123, i % 4 == 0, 45734.345341,
             (
               "r#$%@#4!*&^()_=ASD~!"
               + str(i * 5)
             ),
             datetime.date(year, month, day), datetime.datetime(year, month + 2, day + 1, 10, 20, 44, 45),
             [i % 2, - i % 2, i % 6],
             ["asdsa" + str(i * 4), "23432asda" + str(i * 10), "asdsd" + str(i * 20)],
             [i * 1000, i * 34534, i * 34543], [i % 2 == 0, i % 3 == 0, i % 4 == 0],
             [datetime.date(year, month + 3, day + 4), datetime.date(year, month, day), datetime.date(year, month + 3, day + 4)],
             [datetime.datetime(year, month + 3, day + 4, i % 10 + 1, i % 20 + 1, i % 44 + 1, i % 45 + 1),
              datetime.datetime(year, month + 1, day + 1, i % 10 + 1, i % 20 + 1, i % 44 + 1, i % 45 + 1),
              datetime.datetime(year, month + 1, day + 5, i % 10 + 1, i % 20 + 1, i % 44 + 1, i % 45 + 1)],
             [i * 7 / 2, i * 11 / 5, i * 7 / 11],
             [Decimal(i * 54 / 2), Decimal(i * 4 / 33), Decimal(i * 456 / 45)],
             {
               " - c_short  - ": i % 35,
               "-  c_int  -": i % 56,
               "    c-long    ": i * 45435,
               "--c_--decimal--": Decimal(i * 45642 / 45),
               "c float  -  - ": - i * 656456 / 342,
               "-   c_boolean": i % 4 == 0,
               "  c_--double   -": i * 43543 / 4,
               "  c-   - string": (
                 "2342312dasd$%@#"
                 + str(i * 5)
               ),
               "- - - c_date - -": datetime.date(year, month + 1, day + 5),
               "  - c_timestamp  - ": datetime.datetime(year, month + 1, day + 5, i % 10 + 1, i % 20 + 1, i % 44 + 1, i % 45 + 1),
               "c-array-int-only-1-2-3 4 5": [i % 65535, i * 2, i * 3, i * 4]
             })
        );

    df = spark.createDataFrame(data = data, schema = schema)
    out0 = df

    return out0
