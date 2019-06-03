import unittest
import xml.etree.ElementTree as ET

import Parser.Lang_Python.getFunction as getFunction
import Parser.classes as classes


class Test_getFunction(unittest.TestCase):
    def test_getFunction(self):
        '''
        It should get the function
        '''
        obj = ET.ElementTree(ET.fromstring(
            '<root> \
                <name>pythonFunction</name> \
                <param> \
                    <type>param1</type> \
                    <defname>param1</defname> \
                </param> \
                <param> \
                    <type>param2</type> \
                    <defname>param2</defname> \
                </param> \
            </root>'
        )).getroot()

        expected = classes.functionClass()
        expected.name = 'pythonFunction'
        variable = classes.variableClass()
        variable.name = "param1"
        variable.type = "param1"
        variable2 = classes.variableClass()
        variable2.name = "param2"
        variable2.type = "param2"
        expected.params = [variable, variable2]
        expected.returnValues = []

        received = getFunction.getFunction(obj)
        self.assertEqual(expected.name, received.name, 'Should be equal')
        self.assertEqual(expected.params[0].name, received.params[0].name, 'Should be equal')
        self.assertEqual(expected.params[0].type, received.params[0].type, 'Should be equal')
        self.assertEqual(expected.params[1].name, received.params[1].name, 'Should be equal')
        self.assertEqual(expected.params[1].type, received.params[1].type, 'Should be equal')
        self.assertEqual(expected.returnValues, received.returnValues, 'Should be equal')