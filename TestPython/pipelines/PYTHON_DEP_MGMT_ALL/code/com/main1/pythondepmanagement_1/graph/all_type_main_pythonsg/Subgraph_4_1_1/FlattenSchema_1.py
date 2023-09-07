from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0\
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
        .withColumn("c_complex-array-Asthma-medications-medicationsClasses-className_1-associated-Drug", explode_outer("c_complex-array-Asthma-medications-medicationsClasses-className_1.associated-Drug"))\
        .columns
    selectCols = [col("c_int.test.value1") if "c_int.test.value1" in flt_col else col("c_int").alias("c_int.test.value1"),                   col("c_int.test.value1.complex-array1.diabetes") if "c_int.test.value1.complex-array1.diabetes" in flt_col else col("c_complex-array-Diabetes-medications-medicationsClasses-className_1-associated-Drug.name")\
                    .alias("c_int.test.value1.complex-array1.diabetes"),                   col(
                    "c_int.test.value1.complex-struct1.diabetes.medication"
                  ) if "c_int.test.value1.complex-struct1.diabetes.medication" in flt_col else col("c_complex-array-Diabetes.medications")\
                    .alias("c_int.test.value1.complex-struct1.diabetes.medication"),                   col(
                    "c_int.test.value1.complex-struct1.diabetes.medication.cfuse"
                  ) if "c_int.test.value1.complex-struct1.diabetes.medication.cfuse" in flt_col else col("c_complex-array-Asthma-medications-medicationsClasses-className_1-associated-Drug.cf-use")\
                    .alias("c_int.test.value1.complex-struct1.diabetes.medication.cfuse")]

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
        .select(*selectCols)
