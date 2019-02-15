#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from getDefine import getDefine
from getStruct import getStruct
from getUnion import getUnion
from getFunction import getFunction
from getTypedef import getTypedef
import printData as printData


def parseXMLFile(filename):
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
        if kind == 'function':
            functions.append(getFunction(elem))
        if kind == 'typedef':
            typedefs.append(getTypedef(elem))

    for elem in root.iter('innerclass'):
        refid = elem.get("refid")
        if "struct" in refid:
            structs.append(getStruct("xml/" + refid + ".xml"))
        if "union" in refid:
            unions.append(getUnion("xml/" + refid + ".xml"))
    
    #printData.printStructures(structs)
    #printData.printDefines(defines)
    printData.printFunctions(functions)
