#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from Lang_C_CPP.getDefine import getDefine
from Lang_C_CPP.getStruct import getStruct
from Lang_C_CPP.getUnion import getUnion
from Lang_C_CPP.getFunction import getFunction
from Lang_C_CPP.getTypedef import getTypedef
from languageInterface import LanguageInterface

import getters as getters


class parserC(LanguageInterface):
    def getSymbols(self, filename):
        root = ET.parse(filename).getroot()

        for elem in root.iter('memberdef'):
            kind = elem.get('kind')
            if kind == 'define':
                super().appendToSymbols('define', getDefine(elem))
            if kind == 'function':
                super().appendToSymbols('function', getFunction(elem))
            if kind == 'typedef':
                super().appendToSymbols('typedef', getTypedef(elem))

        for elem in root.iter('innerclass'):
            refid = elem.get('refid')
            if 'struct' in refid:
                super().appendToSymbols('struct', getStruct("xml/" + refid + ".xml"))
            if 'union' in refid:
                super().appendToSymbols('union', getUnion("xml/" + refid + ".xml"))