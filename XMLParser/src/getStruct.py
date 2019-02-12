import xml.etree.ElementTree as ET
from src.classes import structClass
from src.classes import variableClass
import src.strOperations as strOp
import src.getters as getters


def getStruct(fileName, structs):
    tmpStruct = structClass()
    root = ET.parse(fileName).getroot()

    tmpStruct.name = getters.getCompoundName(root)
    tmpStruct.briefDesc = getters.getBriefDesc(root.find("compounddef"))
    tmpStruct.detailedDesc = getters.getDetailedDesc(root.find("compounddef"))

    for elem in root.iter("memberdef"):
        tmpVar = variableClass()
        tmpVar.name = getters.getName(elem)
        tmpVar.type = getters.getType(elem)
        tmpVar.briefDesc = getters.getBriefDesc(elem)
        tmpVar.detailedDesc = getters.getDetailedDesc(elem)
        tmpStruct.members.append(tmpVar)

    structs.append(tmpStruct)
    return structs