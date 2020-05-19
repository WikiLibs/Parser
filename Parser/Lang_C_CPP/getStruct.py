import xml.etree.ElementTree as ET
from classes import structClass
from classes import variableClass
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
