import unittest
import xml.etree.ElementTree as ET

import Parser.Lang_Python.getClass as getClass
import Parser.classes as classes


class Test_GetClass(unittest.TestCase):
    def test_getClass(self):
        '''
        it should get the class
        '''
        obj = ET.ElementTree(ET.fromstring(
            '<root> \
                <compounddef> \
                    <compoundname>pythonFile::pythonClass</compoundname> \
                    <memberdef kind="variable"> \
                        <type></type> \
                        <definition>pythonFile.pythonClass::param1</definition> \
                        <argsstring></argsstring> \
                        <name>param1</name> \
                    </memberdef> \
                    <memberdef kind="function"> \
                        <type>def</type> \
                        <definition>def pythonFile.pythonClass.__init__</definition> \
                        <argsstring>(self, paramInit1, paramInit2)</argsstring> \
                        <name>__init__</name> \
                        <param> \
                            <type>self</type> \
                            <defname>self</defname> \
                        </param> \
                        <param> \
                            <type>paramInit1</type> \
                            <defname>paramInit1</defname> \
                        </param> \
                    </memberdef> \
                </compounddef> \
            </root>'
        )).getroot()

        expectedVar = classes.variableClass()
        expectedVar.name = 'param1'
        expectedVar.type = 'variable'

        expected = classes.classClass()
        expected.name = 'pythonClass'
        expected.description = ''
        expected.variables = [expectedVar]

        received = getClass.getClass(obj)
        self.assertEqual(expected.name, received[-1].path, 'Should be equal')
        self.assertEqual(expected.description, received[-1].prototypes[0].description, 'Should be equal')
        self.assertEqual(expected.variables[0].name, received[0].path, 'Should be equal')
        self.assertEqual(expected.variables[0].type, received[0].typename, 'Should be equal')
