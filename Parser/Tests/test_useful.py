import unittest
from unittest.mock import patch

import sys
import io

import Parser.useful as useful


class Test_Useful(unittest.TestCase):
    def test_verbose_false(self):
        '''it should not print hello as verbose isn't enabled'''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '')

    @patch('Parser.useful.verbose', True)  # modify value of global variable
    def test_verbose_true(self):
        '''it should print hello as verbose is enabled'''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), 'hello\n')

    def test_exception_verbose_false(self):
        '''it should not print the exception as exceptions is not enabled'''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printExceptionVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '')

    @patch('Parser.useful.verbose', True)
    @patch('Parser.useful.exceptions', True)
    def test_exception_verbose_true(self):
        '''it should not print the exception as exceptions is not enabled'''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        useful.printExceptionVerbose('hello')
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), 'Exception: hello\n')
