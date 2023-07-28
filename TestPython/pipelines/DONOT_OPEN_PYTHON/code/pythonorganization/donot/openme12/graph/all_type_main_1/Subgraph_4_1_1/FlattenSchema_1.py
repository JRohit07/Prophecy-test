from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("c_complex-array", explode_outer("c_complex-array"))\
        .withColumn("c_complex-array-Diabetes", explode_outer("c_complex-array.Diabetes"))\
        .withColumn("c_complex-array-Asthma", explode_outer("c_complex-array.Asthma"))\
        .withColumn("c_complex-array-Diabetes-medications", explode_outer("c_complex-array-Diabetes.medications"))\
        .withColumn("c_complex-array-Asthma-medications", explode_outer("c_complex-array-Asthma.medications"))\
        .withColumn(
          "c_complex-array-Diabetes-medications-medicationsClasses",
          explode_outer("c_complex-array-Diabetes-medications.medicationsClasses")
        )\
        .withColumn(
          "c_complex-array-Asthma-medications-medicationsClasses",
          explode_outer("c_complex-array-Asthma-medications.medicationsClasses")
        )\
        .withColumn(
          "c_complex-array-Diabetes-medications-medicationsClasses-className_1",
          explode_outer("c_complex-array-Diabetes-medications-medicationsClasses.className_1")
        )\
        .withColumn(
          "c_complex-array-Asthma-medications-medicationsClasses-className_1",
          explode_outer("c_complex-array-Asthma-medications-medicationsClasses.className_1")
        )\
        .withColumn(
          "c_complex-array-Diabetes-medications-medicationsClasses-className_1-associated-Drug",
          explode_outer("c_complex-array-Diabetes-medications-medicationsClasses-className_1.associated-Drug")
        )\
        .withColumn(
          "c_complex-array-Asthma-medications-medicationsClasses-className_1-associated-Drug",
          explode_outer("c_complex-array-Asthma-medications-medicationsClasses-className_1.associated-Drug")
        )\
        .select(col("c_int").alias("c_int.test.value1"), col("c_complex-array-Diabetes-medications-medicationsClasses-className_1-associated-Drug.name")\
        .alias("c_int.test.value1.complex-array1.diabetes"), col("c_complex-array-Diabetes.medications").alias("c_int.test.value1.complex-struct1.diabetes.medication"), col("c_complex-array-Asthma-medications-medicationsClasses-className_1-associated-Drug.cf-use")\
        .alias("c_int.test.value1.complex-struct1.diabetes.medication.cfuse"))
