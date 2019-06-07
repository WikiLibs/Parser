#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

import sys
import io

import Parser.useful as useful
import Parser.jsonRequestCrafter as jsonRequestCrafter
import Parser.aiClient as aiClient


class Test_JSONRequestCrafter(unittest.TestCase):
    def test_distinc_wip(self):
        '''
        it should print WIP
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        client = aiClient
        list = ['crash']
        list2 = [('client', client), ('client', list)]
        jsonRequestCrafter.JSONRequestCrafter('C', 'noOptimize', list2)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), 'This feature is in WIP\n', 'Should print \'This feature is in WIP\'')

    def test_distinc_error(self):
        '''
        it should print WIP
        '''
        with self.assertRaises(SystemExit) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            list = ['test']
            list2 = [('client', list), ('error', list)]
            jsonRequestCrafter.JSONRequestCrafter('C', 'Test', list2)
            sys.stdout = sys.__stdout__  # reset stdout

        self.assertEqual(cm.exception.code, 1)  # assert exit code
        self.assertEqual(capturedOutput.getvalue(), 
        (useful.RED + useful.BOLD + "[ERROR]" + useful.RESET + " - key error not found in JSONRequestCrafter (line:220)\n" + useful.BOLD + "[---Exiting program---]" + useful.RESET + "\n"), "Should print the expected")
