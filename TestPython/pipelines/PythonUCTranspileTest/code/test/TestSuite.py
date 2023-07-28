import unittest

from test.python_unity_catalog.graph.test_Deduplicate_1 import *
from test.python_unity_catalog.graph.test_SQLStatement_1_1 import *
from test.python_unity_catalog.graph.test_OrderBy_1 import *
from test.python_unity_catalog.graph.test_WindowFunction_1 import *
from test.python_unity_catalog.graph.test_Reformat_1 import *
from test.python_unity_catalog.graph.test_Aggregate_1 import *
from test.python_unity_catalog.graph.Subgraph_1.test_Filter_2 import *
from test.python_unity_catalog.graph.Subgraph_1.Subgraph_2.test_Reformat_4 import *
from test.python_unity_catalog.graph.Subgraph_1.test_Reformat_3 import *
from test.python_unity_catalog.graph.test_Join_1 import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
