import unittest

import Parser.strOperations as strOperations


class Test_StrOperations(unittest.TestCase):
    def test_epurStr(self):
        '''it should print hello world'''
        result = strOperations.epurStr('  he\nll\to      wor\rld     ')
        self.assertEqual(result, 'hello world')

    def test_removePointerSpace(self):
        '''it should print \'int*\''''
        result = strOperations.removePointerSpace('int *')
        self.assertEqual(result, 'int*')
