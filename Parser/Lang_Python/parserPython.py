#!/usr/bin/env python3.6
import os
import xml.etree.ElementTree as ET
from Lang_Python.getVariable import getVariable
from Lang_Python.getClass import getClass
from Lang_Python.getFunction import getFunction
from languageInterface import LanguageInterface

kindTable = {
    "variable": getVariable,
    "function": getFunction,
    "class": getClass
}

#prepare to get throws
class parserPython(LanguageInterface):
    # def getSymbols(self, filename):
    #     newFilename = filename[6:-8]
    #     namespaceFilename = './xml/namespace' + newFilename + '.xml'

    #     classFilenames = getClassesFiles(newFilename)

    #     if os.path.isfile(namespaceFilename):
    #         namespaceRoot = ET.parse(namespaceFilename).getroot()

    #         for elem in namespaceRoot.iter('memberdef'):
    #             kind = elem.get('kind')
    #             if kind == 'variable':
    #                 super().appendToSymbols('variable', getVariable(elem))
    #             if kind == 'function':
    #                 super().appendToSymbols('function', getFunction(elem))

    #     for classFile in classFilenames:
    #         classFileRoot = ET.parse(classFile).getroot()
    #         super().appendToSymbols('class', getClass(classFileRoot))

    def getSymbols(self, filename):
        newFilename = filename[6:-8]
        namespaceFilename = './xml/namespace' + newFilename + '.xml'

        classFilenames = getClassesFiles(newFilename)
        syms = []
        if os.path.isfile(namespaceFilename):
            namespaceRoot = ET.parse(namespaceFilename).getroot()
            for elem in namespaceRoot.iter('memberdef'):
                kind = elem.get('kind')
                syms += kindTable[kind](elem)

        for classFile in classFilenames:
            classFileRoot = ET.parse(classFile).getroot()
            syms += kindTable['class'](classFileRoot)

        for s in syms:
            self.appendToSymbols("generic", s)

def getClassesFiles(filename):
    result = os.popen('find . -name \"class*' + filename + '*.xml\" -print').read().split()
    return result
