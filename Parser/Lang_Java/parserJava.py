#!/usr/bin/env python3.6
import os
import xml.etree.ElementTree as ET
from useful import filesClass
from Lang_Java.getFunction import getFunction
from Lang_Java.getClass import getClass
from Lang_Java.getVariable import getVariable
from languageInterface import LanguageInterface

kindTable = {
    "variable": getVariable,
    "function": getFunction,
    "class": getClass
}

#prepare to get throws
class parserJava(LanguageInterface):
    # def getSymbolsOld(self, filename):
    #     newFilename = filename[6:-8]
    #     namespaceFilename = './xml/namespace' + newFilename + '.xml'

    #     classFilenames = getClassesFiles(newFilename)

    #     if os.path.isfile(namespaceFilename):
    #         namespaceRoot = ET.parse(namespaceFilename).getroot()

    #         for elem in namespaceRoot.iter('membderdef'):
    #             kind = elem.get('kind')
    #             if kind == 'variable':
    #                 super().appendToSymbols('variable', getVariable(elem))
    #             if kind == 'function':
    #                 super().appendToSymbols('function', getFunction(elem))

    #     for classFile in classFilenames:
    #         classFileRoot = ET.parse(classFile).getroot()
    #         super().appendToSymbols('class', getClass(classFileRoot))

    def getAllParseableFiles(self):
        files = []
        root = ET.parse("./xml/index.xml").getroot()

        for child in root.iter("compound"):
            if (child.get('kind') != 'dir'):
                tmp = filesClass()
                tmp.ogFilename = child.find('name').text
                tmp.xmlFilename = "./xml/" + child.get('refid') + ".xml"
                files.append(tmp)
        return (files)

    def getSymbols(self, filename):
        newFilename = filename[6:]
        namespaceFilename = './xml/' + newFilename

        # classFilenames = getClassesFiles(newFilename)
        # for i in classFilenames:
        #     print("class found: " + i)
        syms = []
        if os.path.isfile(namespaceFilename):
            root = ET.parse(namespaceFilename).getroot()

            cpdef = root.find("compounddef")
            kind = cpdef.get("kind")

            syms = []
            if (kind in kindTable):
                syms = kindTable[kind](root)
            # namespaceRoot = ET.parse(namespaceFilename).getroot()
            # print("here1")
            # for elem in namespaceRoot.iter('compounddef'):
            #     print("kind " + elem.tag)
            #     kind = elem.get('kind')
            #     syms += kindTable[kind](elem)

        # for classFile in classFilenames:
        #     classFileRoot = ET.parse(classFile).getroot()
        #     syms += kindTable['class'](classFileRoot)

        for s in syms:
            self.appendToSymbols("generic", s)

# def getClassesFiles(filename):
#     result = os.popen('find . -name \"class*' + filename + '*.xml\" -print').read().split()
#     return result
