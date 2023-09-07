from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonorganization.donot.openme12.graph.Reformat_16 import *
from pythonorganization.donot.openme12.config.ConfigStore import *


class Reformat_16Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Reformat_16(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "account_flags",
              "account_open_date",
              "country_code",
              "customer_id",
              "email",
              "first_name",
              "last_name",
              "phone"
            ),
            dfOutComputed.select(
              "account_flags",
              "account_open_date",
              "country_code",
              "customer_id",
              "email",
              "first_name",
              "last_name",
              "phone"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/in0/data/test_unit_test_1.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/out/data/test_unit_test_1.json',
            'out'
        )
        dfOutComputed = Reformat_16(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "account_flags",
              "account_open_date",
              "country_code",
              "customer_id",
              "email",
              "first_name",
              "last_name",
              "phone"
            ),
            dfOutComputed.select(
              "account_flags",
              "account_open_date",
              "country_code",
              "customer_id",
              "email",
              "first_name",
              "last_name",
              "phone"
            ),
            self.maxUnequalRowsToShow
        )

    def test_unit_test_2(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/in0/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/in0/data/test_unit_test_2.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/out/schema.json',
            'test/resources/data/pythonorganization/donot/openme12/graph/Reformat_16/out/data/test_unit_test_2.json',
            'out'
        )
        dfOutComputed = Reformat_16(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "account_flags",
              "account_open_date",
              "country_code",
              "customer_id",
              "email",
              "first_name",
              "last_name",
              "phone"
            ),
            dfOutComputed.select(
              "account_flags",
              "account_open_date",
              "country_code",
              "customer_id",
              "email",
              "first_name",
              "last_name",
              "phone"
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
