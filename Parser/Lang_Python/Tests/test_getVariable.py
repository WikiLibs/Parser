import unittest
import xml.etree.ElementTree as ET

import Parser.Lang_Python.getVariable as getVariable
import Parser.classes as classes


class Test_GetVariable(unittest.TestCase):
    def test_getVariable(self):
        '''
        it should get the variable
        '''
        obj = ET.ElementTree(ET.fromstring(
            '<root> \
                <type>string</type> \
                <definition>string pythonFile.RANDOM_VARIABLE</definition> \
                <argsstring></argsstring> \
                <name>RANDOM_VARIABLE</name> \
                <initializer>=  HELLO</initializer> \
            </root>'
        )).getroot()

        expected = classes.variableClass()
        expected.name = 'RANDOM_VARIABLE'
        expected.type = 'string'
        expected.value = 'HELLO'

        received = getVariable.getVariable(obj)
        self.assertEqual(expected.name, received.name, 'Should be equal')
        self.assertEqual(expected.type, received.type, 'Should be equal')
        self.assertEqual(expected.value, received.value, 'Should be equal')
