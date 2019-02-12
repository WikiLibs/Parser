import xml.etree.ElementTree as ET
from src.classes import structClass
from src.classes import variableClass
import src.strOperations as strOp

def getName(root):
    return strOp.epurStr(root.find("compounddef").find("compoundname").text)


def getBriefDesc(root):
    try:
        briefDesc = strOp.epurStr(root.find("compounddef").find("briefdescription").text)
    except:
        return ""
    return briefDesc


def getDetailedDesc(root):
    try:
        detailedDesc = strOp.epurStr(root.find("compounddef").find("detaileddescription").find("para").text)
    except:
        try:
            detailedDesc = strOp.epurStr(root.find("compounddef").find("detaileddescription").text)
        except:
            return ""
    return detailedDesc


def getParamName(param):
    return param.find("name").text


def getParamType(param):
    try:
        paramType = ""
        for elem in param.find("type").itertext():
            paramType += elem
        paramType = strOp.epurStr(paramType)
    except:
        return ""
    return paramType

def getParamBriefDesc(param):
    try:
        briefDesc = strOp.epurStr(param.find("briefdescription").find("para").text)
    except:
        try:
            briefDesc = strOp.epurStr(param.find("briefdescription").text)
        except:
            return ""
    return briefDesc

def getParamDetailedDesc(param):
    try:
        detailedDesc = strOp.epurStr(param.find("detaileddescription").find("para").text)
    except:
        try:
            detailedDesc = strOp.epurStr(param.find("detaileddescription").text)
        except:
            return ""
    return detailedDesc


def getStruct(fileName, structs):
    tmpStruct = structClass()
    root = ET.parse(fileName).getroot()

    tmpStruct.name = getName(root)
    tmpStruct.briefDesc = getBriefDesc(root)
    tmpStruct.detailedDesc = getDetailedDesc(root)
    for elem in root.iter("memberdef"):
        tmpVar = variableClass()
        tmpVar.name = getParamName(elem)
        tmpVar.type = getParamType(elem)
        tmpVar.briefDesc = getParamBriefDesc(elem)
        tmpVar.detailedDesc = getParamDetailedDesc(elem)
        tmpStruct.members.append(tmpVar)

    structs.append(tmpStruct)
    return structs