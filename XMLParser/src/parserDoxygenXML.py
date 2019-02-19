#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from getDefine import getDefine
from getStruct import getStruct
from getUnion import getUnion
from getFunction import getFunction
from getTypedef import getTypedef
import printData
import useful
from JSONRequestCrafter import JSONRequestCrafter

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

    list = []
    list.append(defines)
    list.append(structs)
    list.append(unions)
    list.append(functions)
    list.append(typedefs)
    JSONRequestCrafter(lang, libname, list)

    #printData.printStructures(structs)
    #printData.printDefines(defines)
    #printData.printFunctions(functions)
    #printData.printTypedefs(typedefs)
    #printData.printUnions(unions)
