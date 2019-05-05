import unittest

import sys
sys.path.append('Parser/Src')

import Parser.Src.Tests.test_useful as test_useful
import Parser.Src.Tests.test_strOperations as test_strOperations

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_useful))
suite.addTests(loader.loadTestsFromModule(test_strOperations))

runner = unittest.TextTestRunner()
result = runner.run(suite)
