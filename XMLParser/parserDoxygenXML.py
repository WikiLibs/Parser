#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from sys import argv as av

from src.getDefine import getDefine
from src.getStruct import getStruct
from src.getUnion import getUnion
from src.getFunction import getFunction
from src.getTypedef import getTypedef
import src.printData as printData


dicoLang = {
    "C" : [ '.h', '.c' ],
    "Python" : [ '.py' ]
}


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
    

def getAllFiles(langage):
    global dicoLang
    files = []
    root = ET.parse("./xml/index.xml").getroot()
    extentions = dicoLang.get(langage)

    for child in root:
        if child.get('kind') == 'file':
            filename = child.find('name').text
            for extension in extentions:
                if filename.endswith(extension):
                    files.append("./xml/" + child.get('refid') + ".xml")
    return files


def main():
    files = getAllFiles("C")

    for filename in files:
        parseXMLFile(filename)

if __name__ == '__main__':
    main()