import xml.etree.ElementTree as ET
from classes import unionClass
from classes import variableClass
import strOperations as strOp
import getters as getters


def getUnion(fileName):
    tmpUnion = unionClass()
    root = ET.parse(fileName).getroot()

    tmpUnion.name = getters.getCompoundName(root)
    tmpUnion.briefDesc = getters.getBriefDesc(root.find("compounddef"))
    tmpUnion.detailedDesc = getters.getDetailedDesc(root.find("compounddef"))

    for elem in root.iter("memberdef"):
        tmpVar = variableClass()
        tmpVar.name = getters.getName(elem)
        tmpVar.type = getters.getType(elem)
        tmpVar.briefDesc = getters.getBriefDesc(elem)
        tmpVar.detailedDesc = getters.getDetailedDesc(elem)
        tmpUnion.members.append(tmpVar)

    return tmpUnion