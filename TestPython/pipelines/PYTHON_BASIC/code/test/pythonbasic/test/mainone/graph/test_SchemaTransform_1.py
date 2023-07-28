from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pythonbasic.test.mainone.graph.SchemaTransform_1 import *
from pythonbasic.test.mainone.config.ConfigStore import *


class SchemaTransform_1Test(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/SchemaTransform_1/in0/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/SchemaTransform_1/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pythonbasic/test/mainone/graph/SchemaTransform_1/out/schema.json',
            'test/resources/data/pythonbasic/test/mainone/graph/SchemaTransform_1/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = SchemaTransform_1(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("customer_id", "first_name", "last_name", "email_main", "country_code", "full_name"),
            dfOutComputed.select("customer_id", "first_name", "last_name", "email_main", "country_code", "full_name"),
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
