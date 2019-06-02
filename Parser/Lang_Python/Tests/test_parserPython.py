import unittest
from unittest.mock import patch

import xml.etree.ElementTree as ET
import Parser.classes as classes
import Parser.Lang_Python.parserPython as parserPython


class Test_ParserPython(unittest.TestCase):
    @patch('Parser.Lang_Python.parserPython.printData.printVariables')
    def test_printParsedData(self, mock_printVariables):
        variable = classes.variableClass()
        variable.name = 'RANDOM_VARIABLE'
        variable.type = 'string'
        variable.value = 'HELLO'
        variables = [variable]
        functions = []

        data = {
            'variables': variables,
            'functions': functions
        }

        parserPython.printParsedData(data)
        mock_printVariables.assert_called_once()

    @patch('Parser.Lang_Python.parserPython.os.path.isfile', return_value=True)
    @patch('Parser.Lang_Python.parserPython.ET.parse')
    @patch('Parser.Lang_Python.parserPython.getVariable')
    @patch('Parser.Lang_Python.parserPython.getFunction')
    def test_parseXMLFile_with_namespace(self,
                                         mock_getFunction,
                                         mock_getVariable,
                                         mock_parse,
                                         mock_isfile):  # be careful, patched items come in inverted order
        obj = ' \
        <root> \
            <memberdef kind="variable"> \
                <type>string</type> \
                <definition>string pythonFile.RANDOM_VARIABLE</definition> \
                <argsstring></argsstring> \
                <name>RANDOM_VARIABLE</name> \
                <initializer>=  &apos;HELLO&apos;</initializer> \
            </memberdef> \
            <memberdef kind="function"> \
                <name>pythonFunction</name> \
                <param> \
                    <type>param1</type> \
                    <defname>param1</defname> \
                </param> \
                <param> \
                    <type>param2</type> \
                    <defname>param2</defname> \
                </param> \
            </memberdef> \
        </root> \
        '
        mock_parse.return_value = ET.ElementTree(ET.fromstring(obj))
        parserPython.parseXMLFile('./xml/hello__8_.xml', 'PYTHON', 'Test lib')

        mock_getVariable.assert_called_once()
        mock_getFunction.assert_called_once()

    @patch('Parser.Lang_Python.parserPython.os.path.isfile', return_value=True)
    @patch('Parser.Lang_Python.parserPython.ET.parse')
    @patch('Parser.Lang_Python.parserPython.printParsedData')
    @patch('Parser.Lang_Python.parserPython.useful.verbose', True)  # no mock in parameter
    def test_parseXMLFile_with_verbose(self,
                                       mock_printParsedData,
                                       mock_parse,
                                       mock_isfile):  # be careful, patched items come in inverted order
        obj = '<root></root>'
        mock_parse.return_value = ET.ElementTree(ET.fromstring(obj))
        parserPython.parseXMLFile('./xml/hello__8_.xml', 'PYTHON', 'Test lib')

        mock_printParsedData.assert_called_once()
