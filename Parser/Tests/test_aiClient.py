import unittest

import sys
import io

import requests
import Parser.useful as useful
from unittest.mock import patch

import Parser.jsonClasses as jsClass
import Parser.aiClient as aiClient


class Test_aiClient(unittest.TestCase):
    res = requests
    res.status_code = 600
    res.text = "test"

    res2 = requests
    res2.status_code = 200
    res2.text = "test"

    def test_get_token_error(self):
        with self.assertRaises(ConnectionError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient()
            client.GetToken()

    @patch('Parser.aiClient.AIClient.GetToken', return_value="test")
    def test_push_symbol_error(self,
                               mock_get_token):
        sym = jsClass.SymbolUpdate("test")
        sym.setLang("test2")
        sym.setPath("test")
        sym.setType("test")
        proto = jsClass.SymbolPrototype("test")
        proto.setPrototype("test")
        proto.setDescription("")
        param = jsClass.SymbolParam("test")
        param.setPath("")
        param.setDescription("")
        param.setPrototype("test")
        proto.appendParameters(param)
        proto.appendParameters(param)
        sym.appendPrototypes(proto)
        sym.appendPrototypes(proto)
        sym.appendSymbols("test")
        with self.assertRaises(OSError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient()
            client.PushSymbol(sym)

    @patch('Parser.aiClient.AIClient.GetToken', return_value="test")
    def test_optimize_error_patch(self,
                                  mock_get_token):
        with self.assertRaises(OSError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient()
            client.CallOptimizer()

    @patch('requests.post', return_value=res2)
    def test_get_token_no_error(self,
                                mock_request_post):
        client = aiClient.AIClient()
        client.GetToken()
