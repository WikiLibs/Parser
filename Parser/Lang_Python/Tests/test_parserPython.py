import unittest
from unittest.mock import patch

import xml.etree.ElementTree as ET
import Parser.Lang_Python.parserPython as parserPython


class Test_ParserPython(unittest.TestCase):
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
        parserObj = parserPython.parserPython('PYTHON', 'Test lib')
        parserObj.getSymbols('./xml/hello__8_.xml')

        mock_getVariable.assert_called_once()
        mock_getFunction.assert_called_once()

    @patch('Parser.Lang_Python.parserPython.getClassesFiles')
    @patch('Parser.Lang_Python.parserPython.ET.parse')
    @patch('Parser.Lang_Python.parserPython.getClass')
    def test_parseXMLFile_with_class(self,
                                     mock_getClasses,
                                     mock_parse,
                                     mock_getClassesFiles):  # be careful, patched items come in inverted order
        obj = '<root></root>'
        mock_getClassesFiles.return_value = ['./xml/classpython_file_1_1python_class.xml']
        mock_parse.return_value = ET.ElementTree(ET.fromstring(obj))
        parserObj = parserPython.parserPython('PYTHON', 'Test lib')
        parserObj.getSymbols('./xml/hello__8_.xml')

        mock_getClasses.assert_called_once()
