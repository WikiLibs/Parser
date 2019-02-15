import strOperations as strOp
from classes import variableClass


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


def getInitializer(define):
    try:
        init = strOp.epurStr(define.find("initializer").text)
        return init
    except:
        return ""


def getDetailedDesc(elem):
    try:
        detailedDesc = ""
        for token in elem.find("detaileddescription").itertext():
            detailedDesc += " " + token.replace('\n', '').replace('\t', '')
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
        try:
            tmpVar = variableClass()
            tmpVar.name = strOp.epurStr(token.find("declname").text)
            tmpVar.type = strOp.epurStr(token.find("type").text)
            try:
                tmpVar.desc = elem.findall("./detaileddescription/para/parameterlist/parameteritem")[i].find("./parameterdescription/para").text
            except:
                pass
            allVars.append(tmpVar)
            i += 1
        except:
            pass
    return allVars


def getReturnComment(elem):
    try:
        comment  = elem.find("./detaileddescription/para/simplesec/para").text
        return comment
    except:
        return ""


def getParamsName(define):
    params = []
    try:
        for param in define.findall("param"):
            try:
                params.append(strOp.epurStr(param.find("defname").text))
            except:
                params.append(strOp.epurStr(param.find("declname").text))
    except:
        pass
    return params


def removeFromDetailedDescParams(desc, params):
    if len(params) > 0 and params[0] in desc:
        index = desc.find(params[0])
        desc = desc[:index]
    return desc