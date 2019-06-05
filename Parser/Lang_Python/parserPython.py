import os
import xml.etree.ElementTree as ET
from Lang_Python.getVariable import getVariable
from Lang_Python.getClass import getClass
from Lang_Python.getFunction import getFunction
import Lang_Python.printData as printData
import useful
from aiClient import AIClient
from jsonRequestCrafter import JSONRequestCrafter


def printParsedData(data):
    printData.printVariables(data['variables'])
    printData.printClasses(data['classes'])
    printData.printFunctions(data['functions'])


def getClassesFiles(filename):
    result = os.popen('find . -name class*' + filename + '*.xml -print').read().split()
    return result


def parseXMLFile(filename, lang, libname):
    variables = []
    classes = []
    functions = []

    newFilename = filename[6:-8]
    namespaceFilename = './xml/namespace' + newFilename + '.xml'

    classFilenames = getClassesFiles(newFilename)

    if os.path.isfile(namespaceFilename):
        namespaceRoot = ET.parse(namespaceFilename).getroot()

        for elem in namespaceRoot.iter('memberdef'):
            kind = elem.get('kind')
            if kind == 'variable':
                variables.append(getVariable(elem))
            if kind == 'function':
                functions.append(getFunction(elem))

    for classFile in classFilenames:
        classFileRoot = ET.parse(classFile).getroot()
        classes.append(getClass(classFileRoot))

    if useful.verbose:
        data = {
            'variables': variables,
            'classes': classes,
            'functions': functions
        }
        printParsedData(data)

    if useful.upload:
        # change this, maybe try association table
        client = AIClient()
        list = []
        list.append(('client', client))
        list.append(('variable', variables))
        list.append(('class', classes))
        list.append(('function', functions))
        JSONRequestCrafter(lang, libname, list)
