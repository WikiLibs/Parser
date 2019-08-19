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

    def test_get_token_connection_error(self):
        with self.assertRaises(ConnectionError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient("what", "", "")
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
            client = aiClient.AIClient("what", "", "")
            client.PushSymbol(sym)

    @patch('requests.post', return_value=res2)
    def test_get_token_no_error(self,
                                mock_request_post):
        client = aiClient.AIClient("what", "", "")
        client.GetToken()
        mock_request_post.assert_called()

    def test_refresh_token_refreshing_no_error(self):
        client = aiClient.AIClient("what", "", "")
        client._time = -3000
        client.CheckIfRefresh()

    def test_push_symbol_res_error(self):
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
            client = aiClient.AIClient(aiClient.APP_KEY, aiClient.APP_ID, aiClient.SEC)
            client.GetToken()
            client.PushSymbol(sym)

    @patch('Parser.aiClient.AIClient.GetToken', return_value="test")
    def test_optimize_no_token(self,
                               mock_get_token):
        with self.assertRaises(OSError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient("what", "", "")
            client.CallOptimizer()
            mock_get_token.assert_called()
        
    def test_optimizer_optimize_error(self):
        with self.assertRaises(IOError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient(aiClient.APP_KEY, aiClient.APP_ID, aiClient.SEC)
            client._token = "what"
            client.CallOptimizer()

    def test_optimize_ext_connection_error(self):
        with self.assertRaises(OSError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient("what", "", "")
            client.CallOptimizer_ext("")

    @patch('requests.post', return_value=res2)
    def test_optimize_ext_optimize_error(self,
                                         req_post):
        with self.assertRaises(IOError) as cm:
            capturedOutput = io.StringIO()  # setup an io
            sys.stdout = capturedOutput  # redirect stdout
            client = aiClient.AIClient("what", "", "")
            client.CallOptimizer_ext("what???")
            req_post.assert_called()
