import unittest

import requests
from unittest.mock import patch

import Parser.jsonClasses as jsClass
import Parser.aiClient as aiClient


class Test_aiClient(unittest.TestCase):
    res = requests
    res.status_code = 200
    res.text = "test"

    @patch('requests.post', return_value=res)
    def test_push_symbol_error_auth(self,
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
    @patch('requests.patch', return_value=res)
    def test_optimize_error_push(self,
                                 mock_request_patch,
                                 mock_request_post):
        client = aiClient.AIClient()
        client.CallOptimizer()