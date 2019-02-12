import src.strOperations as strOp


def getCompoundName(elem):
    return strOp.epurStr(elem.find("compounddef").find("compoundname").text)

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
        detailedDesc = strOp.epurStr(param.find("detaileddescription").find("para").text)
    except:
        try:
            detailedDesc = strOp.epurStr(param.find("detaileddescription").text)
        except:
            return ""
    return detailedDesc


def getBriefDesc(param):
    try:
        briefDesc = strOp.epurStr(param.find("briefdescription").find("para").text)
    except:
        try:
            briefDesc = strOp.epurStr(param.find("briefdescription").text)
        except:
            return ""
    return briefDesc