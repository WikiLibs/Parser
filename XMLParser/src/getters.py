import src.strOperations as strOp
from src.classes import variableClass


def getCompoundName(elem):
    return strOp.epurStr(elem.find("compounddef/compoundname").text)

def getName(elem):
    return strOp.epurStr(elem.find("name").text)

def getType(elem):
    try:
        elemType = ""
        for token in elem.find("type").itertext():
            elemType += token
        elemType = strOp.removePointerSpace(strOp.epurStr(elemType))
        return elemType
    except:
        return ""


def getDetailedDesc(elem):
    try:
        detailedDesc = ""
        for token in elem.find("detaileddescription").itertext():
            detailedDesc += token
        return strOp.epurStr(detailedDesc)
    except:
        return ""


def getBriefDesc(elem):
    try:
        briefDesc = ""
        for token in elem.find("briefdescription").itertext():
            briefDesc += token
        return strOp.epurStr(briefDesc)
    except:
        return ""

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