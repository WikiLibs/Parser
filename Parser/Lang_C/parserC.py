#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from Lang_C.getDefine import getDefine
from Lang_C.getStruct import getStruct
from Lang_C.getUnion import getUnion
from Lang_C.getFunction import getFunction
from Lang_C.getTypedef import getTypedef
from Lang_C.getEnum import getEnum
from languageInterface import LanguageInterface
import getters as getters

kindTable = {
    "define": getDefine,
    "function": getFunction,
    "typedef": getTypedef,
    "union": getUnion,
    "struct": getStruct,
    "enum": getEnum
}

class parserC(LanguageInterface):
    # def getSymbolsOld(self, filename):
    #     root = ET.parse(filename).getroot()

    #     for elem in root.iter('memberdef'):
    #         kind = elem.get('kind')
    #         if kind == 'define':
    #             super().appendToSymbols('define', getDefine(elem))
    #         if kind == 'function':
    #             super().appendToSymbols('function', getFunction(elem))
    #         if kind == 'typedef':
    #             super().appendToSymbols('typedef', getTypedef(elem))

    #     for elem in root.iter('innerclass'):
    #         refid = elem.get('refid')
    #         if 'struct' in refid:
    #             super().appendToSymbols('struct', getStruct("xml/" + refid + ".xml"))
    #         if 'union' in refid:
    #             super().appendToSymbols('union', getUnion("xml/" + refid + ".xml"))

    def getSymbols(self, filename):
        root = ET.parse(filename).getroot()

        syms = []
        for elem in root.iter('memberdef'):
            kind = elem.get('kind')
            syms += kindTable[kind](elem)

        for elem in root.iter('innerclass'):
            refid = elem.get('refid')
            if 'struct' in refid:
                syms += kindTable['struct']("xml/" + refid + ".xml")
            if 'union' in refid:
                syms += kindTable['union']("xml/" + refid + ".xml")

        for s in syms:
            self.appendToSymbols("generic", s)
