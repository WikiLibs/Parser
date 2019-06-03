import os
import xml.etree.ElementTree as ET
from Lang_Python.getVariable import getVariable
from Lang_Python.getFunction import getFunction
import Lang_Python.printData as printData
import useful


def printParsedData(data):
    printData.printVariables(data['variables'])
    printData.printFunctions(data['functions'])


def parseXMLFile(filename, lang, libname):
    variables = []
    functions = []

    newFilename = filename[6:-8]
    namespaceFilename = './xml/namespace' + newFilename + '.xml'

    useful.logInfo('Started parsing \'' + newFilename + '\'.py')

    if os.path.isfile(namespaceFilename):
        namespaceRoot = ET.parse(namespaceFilename).getroot()

        for elem in namespaceRoot.iter('memberdef'):
            kind = elem.get('kind')
            if kind == 'variable':
                variables.append(getVariable(elem))
            if kind == 'function':
                functions.append(getFunction(elem))

    if useful.verbose:
        data = {
            'variables': variables,
            'functions': functions
        }
        printParsedData(data)
