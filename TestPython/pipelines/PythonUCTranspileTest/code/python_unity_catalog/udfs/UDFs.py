from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)
initial = 10

def registerUDFs(spark: SparkSession):
    spark.udf.register("squared", squared)
    spark.udf.register("factorial", factorial)
    spark.udf.register("random_string", random_string)

@udf(returnType = IntegerType())
def squared(input):
    input = int(input) if input is not None else 2

    return int(input) * int(input) * initial if input is not None else initial

@udf(returnType = IntegerType())
def factorial(input):
    input = int(input) if input is not None else 2

    return int(input) * int(input) if input is not None else initial

@udf(returnType = StringType())
def random_string(length, extra_characters=""):
    import string, random
    length = int(length) if length is not None else 2

    return "".join(
        [
          random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + extra_characters)
          for _ in range(length)
        ]
    )
