import src.strOperations as strOp
from src.classes import variableClass


def getCompoundName(elem):
    return strOp.epurStr(elem.find("compounddef/compoundname").text)

def getName(elem):
    return elem.find("name").text

def getType(elem):
    try:
        elemType = ""
        for token in elem.find("type").itertext():
            elemType += token
        elemType = strOp.epurStr(elemType)
    except:
        return ""
    return elemType


def getDetailedDesc(param):
    try:
        detailedDesc = strOp.epurStr(param.find("detaileddescription/para").text)
    except:
        try:
            detailedDesc = strOp.epurStr(param.find("detaileddescription").text)
        except:
            return ""
    return detailedDesc


def getBriefDesc(param):
    try:
        briefDesc = strOp.epurStr(param.find("briefdescription/para").text)
    except:
        try:
            briefDesc = strOp.epurStr(param.find("briefdescription").text)
        except:
            return ""
    return briefDesc

def getParams(elem):
    allVars = []
    i = 0

    for token in elem.findall("param"):
        tmpVar = variableClass()
        tmpVar.name = token.find("declname").text
        tmpVar.type = getType(token)
        try:
            tmpVar.desc = elem.findall("./detaileddescription/para/parameterlist/parameteritem")[i].find("./parameterdescription/para").text
        except:
            pass
        allVars.append(tmpVar)
        i += 1
    return allVars

def getReturnComment(elem):
    try:
        comment  = elem.find("./detaileddescription/para/simplesec/para").text
        return comment
    except:
        return ""