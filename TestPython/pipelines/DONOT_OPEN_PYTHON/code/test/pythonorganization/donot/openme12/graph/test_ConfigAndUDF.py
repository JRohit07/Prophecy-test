from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonorganization.donot.openme12.graph.ConfigAndUDF import *
from pythonorganization.donot.openme12.config.ConfigStore import *


class ConfigAndUDFTest(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = ConfigAndUDF(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("c   short  --", "c-int-column type", "-- c-long", "c-decimal", "c  float", "c--boolean"),
            dfOutComputed.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOutComputed = ConfigAndUDF(self.spark, dfIn0)
        assertPredicates(
            "out",
            dfOutComputed,
            list(
              zip([~ col("`c   short  --`").like("%a%"), ~ col("`c-int-column type`").like("%GH123%")], ["p1", "p2"])
            )
        )

    def test_unit_test_2(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/data/test_unit_test_2.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/data/test_unit_test_2.json',
            'out'
        )
        dfOutComputed = ConfigAndUDF(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c  date",
              "c_timestamp",
              "squared_short",
              "factorial_short",
              "random_string_value",
              "config_values"
            ),
            dfOutComputed.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c  date",
              "c_timestamp",
              "squared_short",
              "factorial_short",
              "random_string_value",
              "config_values"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_3(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/data/test_unit_test_3.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/data/test_unit_test_3.json',
            'out'
        )
        dfOutComputed = ConfigAndUDF(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c  date",
              "c_timestamp",
              "squared_short",
              "factorial_short",
              "random_string_value",
              "config_values"
            ),
            dfOutComputed.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c  date",
              "c_timestamp",
              "squared_short",
              "factorial_short",
              "random_string_value",
              "config_values"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_4(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/in0/data/test_unit_test_4.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/ConfigAndUDF/out/data/test_unit_test_4.json',
            'out'
        )
        dfOutComputed = ConfigAndUDF(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c  date",
              "c_timestamp",
              "squared_short",
              "factorial_short",
              "random_string_value",
              "config_values"
            ),
            dfOutComputed.select(
              "c   short  --",
              "c-int-column type",
              "-- c-long",
              "c-decimal",
              "c  float",
              "c--boolean",
              "c- - -double",
              "c___-- string",
              "c  date",
              "c_timestamp",
              "squared_short",
              "factorial_short",
              "random_string_value",
              "config_values"
            ),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
