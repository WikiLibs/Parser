import os
import xml.etree.ElementTree as ET
from Lang_Python.getVariable import getVariable
from Lang_Python.getClass import getClass
import Lang_Python.printData as printData
import useful


def printParsedData(data):
    printData.printVariables(data['variables'])
    printData.printClasses(data['classes'])


def getClassesFiles(filename):
    result = os.popen('find . -name class' + filename + '*.xml -print').read().split()
    return result


def parseXMLFile(filename, lang, libname):
    variables = []
    classes = []

    newFilename = filename[6:-8]
    namespaceFilename = './xml/namespace' + newFilename + '.xml'

    classFilenames = getClassesFiles(newFilename)

    if os.path.isfile(namespaceFilename):
        namespaceRoot = ET.parse(namespaceFilename).getroot()

        for elem in namespaceRoot.iter('memberdef'):
            kind = elem.get('kind')
            if kind == 'variable':
                variables.append(getVariable(elem))

    for classFile in classFilenames:
        classFileRoot = ET.parse(classFile).getroot()
        classes.append(getClass(classFileRoot))

    if useful.verbose:
        data = {
            'variables': variables,
            'classes': classes
        }
        printParsedData(data)
