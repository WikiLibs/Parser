#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from Lang_C_CPP.getDefine import getDefine
from Lang_C_CPP.getStruct import getStruct
from Lang_C_CPP.getUnion import getUnion
from Lang_C_CPP.getFunction import getFunction
from Lang_C_CPP.getTypedef import getTypedef
import Lang_C_CPP.printData as printData
import useful
from aiClient import AIClient
from jsonRequestCrafter import JSONRequestCrafter


def printParsedData(data):
    printData.printStructures(data['structs'])
    printData.printDefines(data['defines'])
    printData.printFunctions(data['functions'])
    printData.printTypedefs(data['typedefs'])
    printData.printUnions(data['unions'])


def parseXMLFile(filename, lang, libname):
    defines = []
    structs = []
    unions = []
    functions = []
    typedefs = []
    root = ET.parse(filename).getroot()

    for elem in root.iter('memberdef'):
        kind = elem.get('kind')
        if kind == 'define':
            defines.append(getDefine(elem))
            useful.printVerbose("\tFound macro \'" + defines[-1].name + "\'")
        if kind == 'function':
            functions.append(getFunction(elem))
            useful.printVerbose("\tFound function \'" + functions[-1].name + "\'")
        if kind == 'typedef':
            typedefs.append(getTypedef(elem))
            useful.printVerbose("\tFound typedef \'" + typedefs[-1].tdType + "\'")

    for elem in root.iter('innerclass'):
        refid = elem.get("refid")
        if "struct" in refid:
            structs.append(getStruct("xml/" + refid + ".xml"))
            useful.printVerbose("\tFound struct \'" + structs[-1].name + "\'")
        if "union" in refid:
            unions.append(getUnion("xml/" + refid + ".xml"))
            useful.printVerbose("\tFound union \'" + unions[-1].name + "\'")

    if useful.verbose:
        data = {
            'structs': structs,
            'defines': defines,
            'functions': functions,
            'typedefs': typedefs,
            'unions': unions
        }
        printParsedData(data)

    if useful.upload:
        client = AIClient("root@root.com", "12Poissons2hOt4U")
        list = []
        list.append(client)
        list.append(defines)
        list.append(structs)
        list.append(unions)
        list.append(functions)
        list.append(typedefs)
        JSONRequestCrafter(lang, libname, list)
