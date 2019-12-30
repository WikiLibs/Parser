#!/usr/bin/env python3.6
import os
import xml.etree.ElementTree as ET
from Lang_Python.getFunction import getFunction
from Lang_Java.getClass import getClass
from Lang_Java.getVariable import getVariable
from languageInterface import LanguageInterface


class parserJava(LanguageInterface):
    def getSymbols(self, filename):
        newFilename = filename[6:-8]
        namespaceFilename = './xml/namespace' + newFilename + '.xml'

        classFilenames = getClassesFiles(newFilename)

        if os.path.isfile(namespaceFilename):
            namespaceRoot = ET.parse(namespaceFilename).getroot()

            for elem in namespaceRoot.iter('membderdef'):
                kind = elem.get('kind')
                if kind == 'variable':
                    super().appendToSymbols('variable', getVariable(elem))
                if kind == 'function':
                    super().appendToSymbols('function', getFunction(elem))

        for classFile in classFilenames:
            classFileRoot = ET.parse(classFile).getroot()
            super().appendToSymbols('class', getClass(classFileRoot))


def getClassesFiles(filename):
    result = os.popen('find . -name class*' + filename + '*.xml -print').read().split()
    return result