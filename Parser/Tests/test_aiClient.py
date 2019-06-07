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
    res.status_code = 201
    res.text = "test"

    res2 = requests
    res2.status_code = 200
    res2.text = "test"

    @patch('requests.post', return_value=res)
    def test_push_symbol_error(self,
                               mock_request_post):
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
        client = aiClient.AIClient()
        client.PushSymbol(sym)

    @patch('requests.post', return_value=res)
    def test_get_token_error(self,
                             mock_request_post):
        client = aiClient.AIClient()
        client.GetToken()

    @patch('requests.patch', return_value=res)
    def test_optimize_error_patch(self,
                                  mock_request_patch):
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
