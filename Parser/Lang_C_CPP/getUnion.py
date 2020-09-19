import xml.etree.ElementTree as ET
import useful
import PyQt.inputsWindow as inputsWindow

from classes import unionClass
from classes import variableClass
from genericClasses import buildUnion
from genericClasses import buildPrototype
from genericClasses import buildVariable
import getters as getters


# def getUnionOld(fileName):
#     tmpUnion = unionClass()
#     root = ET.parse(fileName).getroot()

#     tmpUnion.name = getters.getCompoundName(root)
#     tmpUnion.include = getters.getLocation(root.find("compounddef"))
#     tmpUnion.briefDesc = getters.getBriefDesc(root.find("compounddef"))
#     tmpUnion.detailedDesc = getters.getDetailedDesc(root.find("compounddef"))

#     for elem in root.iter("memberdef"):
#         tmpVar = variableClass()
#         tmpVar.name = getters.getName(elem)
#         tmpVar.type = getters.getType(elem)
#         tmpVar.briefDesc = getters.getBriefDesc(elem)
#         tmpVar.detailedDesc = getters.getDetailedDesc(elem)
#         tmpUnion.members.append(tmpVar)
#     return tmpUnion

def getUnion(fileName):
    root = ET.parse(fileName).getroot()

    syms = []
    prefix = useful.prefix
    if prefix == "":
        prefix = inputsWindow.prefix
    name = getters.getCompoundName(root)
    include = getters.getLocation(root.find("compounddef"))
    briefDesc = getters.getBriefDesc(root.find("compounddef"))
    detailedDesc = getters.getDetailedDesc(root.find("compounddef"))

    unionProto = buildPrototype("struct " + name, briefDesc)
    unionSym = buildUnion(path=prefix + name, prototypeObj=unionProto, importString=include)
    for elem in root.iter("memberdef"):
        ename = getters.getName(elem)
        etype = getters.getType(elem)
        edesc = getters.getDetailedDesc(elem)
        proto = buildPrototype(etype + " " + ename, edesc)
        syms.append(buildVariable(path=(prefix + name + "/" + ename), prototypeObj=proto))
        unionSym.addMember(name + "/" + ename)
    syms.append(unionSym)
    return syms
