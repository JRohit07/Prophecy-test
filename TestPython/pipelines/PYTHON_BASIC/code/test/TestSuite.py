import unittest

from test.pythonbasic.test.mainone.graph.test_UL_Join_1 import *
from test.pythonbasic.test.mainone.graph.test_UL_OrderBy_1 import *
from test.pythonbasic.test.mainone.graph.test_SchemaTransform_1 import *
from test.pythonbasic.test.mainone.graph.test_UL_Aggregate_1 import *
from test.pythonbasic.test.mainone.graph.Subgraph_1.test_UL_Reformat_4_1 import *
from test.pythonbasic.test.mainone.graph.Subgraph_1.test_UL_Join_1_1 import *
from test.pythonbasic.test.mainone.graph.Subgraph_1.test_UL_OrderBy_1_1 import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
