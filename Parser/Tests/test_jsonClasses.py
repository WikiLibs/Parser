import unittest

import Parser.jsonClasses as jsClass


class Test_jsonClasses(unittest.TestCase):
    def test_symbol_path(self):
        sym = jsClass.SymbolPath("test")
        sym.setPath("test")

    def test_symbol_param(self):
        sym = jsClass.SymbolParam("test")
        sym.setPath("")
        sym.setDescription("")
        sym.setPrototype("test")
        sym.get_JSON()

    def test_symbo_proto(self):
        sym = jsClass.SymbolPrototype("test")
        sym.setPrototype("test")
        sym.setDescription("")
        param = jsClass.SymbolParam("test")
        param.setPath("")
        param.setDescription("")
        param.setPrototype("test")
        sym.appendParameters(param)
        sym.appendParameters(param)
        sym.get_JSON()

    def test_symbol_update(self):
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
        sym.get_JSON()
    