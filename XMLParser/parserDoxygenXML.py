#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from sys import argv as av

from src.getDefine import getDefine
from src.getStruct import getStruct
from src.getUnion import getUnion
from src.getFunction import getFunction
from src.getTypedef import getTypedef
import src.printData as printData

def getFilePath(root):
    try:
        path = root.find("compounddef").find("incdepgraph").find("node").find("label").text
    except:
        try:
            path = root.find("compounddef").find("compoundname").text
        except:
            path = "none"
    return path


def main():
    defines = []
    structs = []
    unions = []
    functions = []
    typedefs = []
    root = ET.parse(av[1]).getroot()

    path = getFilePath(root)

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
    #printData.printFunctions(functions)
    

if __name__ == '__main__':
    main()