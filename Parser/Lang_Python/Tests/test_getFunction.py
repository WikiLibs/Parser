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
        variable2 = classes.variableClass()
        variable2.name = "param2"
        expected.params = [variable, variable2]
        expected.returnValues = [] # not handled

        received = getFunction.getFunction(obj)
        self.assertEqual(expected.name, received[0].path, 'Should be equal')
        self.assertEqual(expected.params[0].name, received[0].prototypes[0].parameters[0].prototype, 'Should be equal')
        self.assertEqual(expected.params[1].name, received[0].prototypes[0].parameters[1].prototype, 'Should be equal')
        # self.assertEqual(expected.returnValues, received[0].prototypes[1].prototype, 'Should be equal')
