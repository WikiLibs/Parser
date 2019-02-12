#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from sys import argv as av

from src.getDefine import getDefine
from src.getStruct import getStruct

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
    root = ET.parse(av[1]).getroot()

    path = getFilePath(root)
    print(path)
    for elem in root.iter('memberdef'):
        if elem.get('kind') == 'define':
            defines = getDefine(elem, defines)
    for elem in root.iter('innerclass'):
        refid = elem.get("refid")
        if "struct" in refid:
            structs = getStruct("xml/" + refid + ".xml", structs)
        if "union" in elem.get('refid'):
            print("union found, should check ", refid, ".xml", sep="")
        

if __name__ == '__main__':
    main()