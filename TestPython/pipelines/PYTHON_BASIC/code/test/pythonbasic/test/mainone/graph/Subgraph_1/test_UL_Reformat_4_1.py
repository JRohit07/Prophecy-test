from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonbasic.test.mainone.graph.Subgraph_1.UL_Reformat_4_1 import *
from pythonbasic.test.mainone.config.ConfigStore import *


class UL_Reformat_4_1Test(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Subgraph_1/UL_Reformat_4_1/in0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Subgraph_1/UL_Reformat_4_1/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Subgraph_1/UL_Reformat_4_1/out/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Subgraph_1/UL_Reformat_4_1/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = UL_Reformat_4_1(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "c_lookup_first_name",
              "c_lookup_last_name",
              "customer_id",
              "first_name",
              "last_name",
              "phone",
              "email",
              "country_code",
              "account_open_date",
              "account_flags"
            ),
            dfOutComputed.select(
              "c_lookup_first_name",
              "c_lookup_last_name",
              "customer_id",
              "first_name",
              "last_name",
              "phone",
              "email",
              "country_code",
              "account_open_date",
              "account_flags"
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
              file = f"configs/resources/pythonbasic/test/configs/configall/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
        dftest_mainone_graph_Lookup_1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/Lookup_1/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/Lookup_1/data.json',
            "in0"
        )
        from pythonbasic.test.mainone.graph.Lookup_1 import Lookup_1
        Lookup_1(self.spark, dftest_mainone_graph_Lookup_1)
