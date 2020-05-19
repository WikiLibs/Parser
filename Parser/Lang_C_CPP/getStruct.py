import xml.etree.ElementTree as ET
import useful
import PyQt.inputsWindow as inputsWindow
from classes import structClass
from classes import variableClass
from genericClasses import buildStruct
from genericClasses import buildPrototype
from genericClasses import buildVariable
from genericClasses import buildParameter
import getters as getters


def getStructOld(fileName):
    tmpStruct = structClass()
    root = ET.parse(fileName).getroot()

    tmpStruct.name = getters.getCompoundName(root)
    tmpStruct.include = getters.getLocation(root.find("compounddef"))
    tmpStruct.briefDesc = getters.getBriefDesc(root.find("compounddef"))
    tmpStruct.detailedDesc = getters.getDetailedDesc(root.find("compounddef"))

    for elem in root.iter("memberdef"):
        tmpVar = variableClass()
        tmpVar.name = getters.getName(elem)
        tmpVar.type = getters.getType(elem)
        tmpVar.desc = getters.getDetailedDesc(elem)
        tmpStruct.members.append(tmpVar)
    return tmpStruct

def getStruct(fileName):
    root = ET.parse(fileName).getroot()

    syms = []
    prefix = useful.prefix
    if prefix == "":
        prefix = inputsWindow.prefix
    name = getters.getCompoundName(root)
    include = getters.getLocation(root.find("compounddef"))
    briefDesc = getters.getBriefDesc(root.find("compounddef"))
    detailedDesc = getters.getDetailedDesc(root.find("compounddef"))

    structProto = buildPrototype("struct " + name, briefDesc)
    structSym = buildStruct(path=name, prototypeObj=structProto, importString=include)
    for elem in root.iter("memberdef"):
        ename = getters.getName(elem)
        etype = getters.getType(elem)
        edesc = getters.getDetailedDesc(elem)
        proto = buildParameter(etype + " " + ename, edesc)
        syms.append(buildVariable(path=(name + "/" + ename), prototypeObj=proto)
        structSym.addMember(prefix + name + "/" + ename)
    syms.append(structSym)
    return syms
