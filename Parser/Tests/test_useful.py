import unittest
from unittest.mock import patch

import sys
import io

import xml.etree.ElementTree as ET
import Parser.useful as useful


class Test_Useful(unittest.TestCase):
    def test_verbose_false(self):
        '''
        it should not print hello as verbose isn't enabled
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '')

    @patch('Parser.useful.verbose', True)  # modify value of global variable
    def test_verbose_true(self):
        '''
        it should print hello as verbose is enabled
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), 'hello\n')

    def test_exception_verbose_false(self):
        '''
        it should not print the exception as exceptions is not enabled
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printExceptionVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '')

    @patch('Parser.useful.verbose', True)
    @patch('Parser.useful.exceptions', True)
    def test_exception_verbose_true(self):
        '''
        it should print the exception as exceptions is enabled by both variables
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printExceptionVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), 'Exception: hello\n')

    def test_log_info_minimal(self):
        '''
        it should print the log info without context
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.logInfo('This is a minimal info')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), (useful.GREEN +
                                                     useful.BOLD +
                                                     "[INFO]" +
                                                     useful.RESET +
                                                     " - This is a minimal info\n"))

    def test_log_info_full(self):
        '''
        it should print the log info with context
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.logInfo('This is a full info', 'file', 4)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), (useful.GREEN +
                                                     useful.BOLD +
                                                     "[INFO]" +
                                                     useful.RESET +
                                                     " - This is a full info (file: 4)\n"))

    def test_log_warning_minimal(self):
        '''
        it should print the log warning without context
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.logWarning('This is a minimal warning')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), (useful.YELLOW +
                                                     useful.BOLD +
                                                     "[WARNING]" +
                                                     useful.RESET +
                                                     " - This is a minimal warning\n"))

    def test_log_warning_full(self):
        '''
        it should print the log warning with context
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.logWarning('This is a full warning', 'file', 4)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), (useful.YELLOW +
                                                     useful.BOLD +
                                                     "[WARNING]" +
                                                     useful.RESET +
                                                     " - This is a full warning (file: 4)\n"))

    def test_log_error_minimal(self):
        '''
        it should print the log error without context
        '''
        with self.assertRaises(SystemExit) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            useful.logError('This is a minimal error', 34)
            sys.stdout = sys.__stdout__  # reset stdout

        self.assertEqual(cm.exception.code, 34)  # assert exit code
        self.assertEqual(capturedOutput.getvalue(), (useful.RED +
                                                     useful.BOLD +
                                                     "[ERROR]" +
                                                     useful.RESET +
                                                     " - This is a minimal error\n" +
                                                     useful.BOLD +
                                                     "[---Exiting program---]" +
                                                     useful.RESET +
                                                     "\n"))

    def test_log_error_full(self):
        '''
        it should print the log error with context
        '''
        with self.assertRaises(SystemExit) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            useful.logError('This is a full error', 34, 'file', 4)
            sys.stdout = sys.__stdout__  # reset stdout

        self.assertEqual(cm.exception.code, 34)  # assert exit code
        self.assertEqual(capturedOutput.getvalue(), (useful.RED +
                                                     useful.BOLD +
                                                     "[ERROR]" +
                                                     useful.RESET +
                                                     " - This is a full error (file: 4)\n" +
                                                     useful.BOLD +
                                                     "[---Exiting program---]" +
                                                     useful.RESET +
                                                     "\n"))
