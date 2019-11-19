import unittest

import sys
import io

from unittest.mock import patch
import Parser.useful as useful
import Parser.jsonRequestCrafter as jsonRequestCrafter
import Parser.classes as classParser
import Parser.aiClient as aiClient


class Test_JsonRequestCrafter(unittest.TestCase):
    @patch('Parser.aiClient.AIClient.CallOptimizer')
    @patch('Parser.aiClient.AIClient.GetToken')
    def test_distinc_wip(self,
                         mock_call_get_token,
                         mock_call_optimizer):
        '''
        it should print WIP
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        list = ['crash']
        list2 = [('client', aiClient.AIClient(aiClient.APP_KEY, aiClient.APP_ID, aiClient.SEC)), ('client', list)]
        jsonRequestCrafter.JSONRequestCrafter('C', 'Test', list2)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), 'This feature is in WIP\n', 'Should print \'This feature is in WIP\'')

    @patch('Parser.aiClient.AIClient.GetToken')
    def test_distinc_error(self, mock_get_token):
        '''
        it should print WIP
        '''
        with self.assertRaises(SystemExit) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            list = ['test']
            list2 = [('client', aiClient.AIClient(aiClient.APP_KEY, aiClient.APP_ID, aiClient.SEC)), ('error', list)]
            jsonRequestCrafter.JSONRequestCrafter('C', 'Test', list2)
            sys.stdout = sys.__stdout__  # reset stdout

        self.assertEqual(cm.exception.code, 1)  # assert exit code
        self.assertEqual(capturedOutput.getvalue(),
        (useful.RED + useful.BOLD + "[ERROR]" + useful.RESET + " - key error not found in JSONRequestCrafter (line:220)\n" + useful.BOLD + "[---Exiting program---]" + useful.RESET + "\n"), "Should print the expected")

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_struct_request(self,
                                  mock_push_symbol):
        '''
        like it should be
        '''

        struct = classParser.structClass()
        mem = classParser.variableClass()
        struct.members.append(mem)
        structs = [struct]

        jsonRequestCrafter.craftStructRequest(aiClient.AIClient, structs)
        mock_push_symbol.assert_called()

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_union_request(self,
                                  mock_push_symbol):
        '''
        like it should be
        '''

        union = classParser.unionClass()
        mem = classParser.variableClass()
        union.members.append(mem)
        unions = [union]

        jsonRequestCrafter.craftUnionRequest(aiClient.AIClient, unions)
        mock_push_symbol.assert_called()

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_define_request(self,
                                  mock_push_symbol):
        '''
        like it should be
        '''

        define = classParser.defineClass()
        param = classParser.variableClass()
        define.params.append(param)
        define.params.append(param)
        defines = [define]

        jsonRequestCrafter.craftDefineRequest(aiClient.AIClient, defines)
        mock_push_symbol.assert_called()

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_function_request(self,
                                    mock_push_symbol):
        '''
        like it should be
        '''

        function = classParser.functionClass()
        param = classParser.variableClass()
        function.params.append(param)
        function.params.append(param)
        functions = [function]

        jsonRequestCrafter.craftFunctionRequest(aiClient.AIClient, functions)
        mock_push_symbol.assert_called()

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_typedef_request(self,
                                   mock_push_symbol):
        '''
        like it should be
        '''

        typedef = classParser.typedefClass()
        typedefs = [typedef]

        jsonRequestCrafter.craftTypedefRequest(aiClient.AIClient, typedefs)
        mock_push_symbol.assert_called()

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_class_request(self,
                                 mock_push_symbol):
        '''
        like it should be
        '''
        function = classParser.functionClass()
        param = classParser.variableClass()
        function.params.append(param)
        function.params.append(param)
        classe = classParser. classClass()
        classe.functions.append(function)
        classe.functions.append(function)
        classe.variables.append(param)
        classe.variables.append(param)
        classes = [classe]

        jsonRequestCrafter.craftClassRequest(aiClient.AIClient,  classes)
        mock_push_symbol.assert_called()

    @patch('Parser.aiClient.AIClient.PushSymbol')
    def test_craft_variable_request(self,
                                    mock_push_symbol):
        '''
        like it should be
        '''

        variable = classParser. variableClass()
        variables = [variable]

        jsonRequestCrafter.craftVariableRequest(aiClient.AIClient,  variables)
        mock_push_symbol.assert_called()
