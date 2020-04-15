import strOperations as strOp
import useful
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
    except Exception as error:
        useful.printExceptionVerbose(error)
        return ""


def getInitializer(elem):
    try:
        init = strOp.epurStr(elem.find("initializer").text)
        if init.startswith('= '):
            init = init[2:]
        return init
    except Exception as error:
        useful.printExceptionVerbose(error)
        return ""


def getDetailedDesc(elem):
    try:
        detailedDesc = ""
        for token in elem.find("detaileddescription").itertext():
            detailedDesc += " " + token.replace('\n', '').replace('\t', '')
        return strOp.epurStr(detailedDesc)
    except Exception as error:
        useful.printExceptionVerbose(error)
        return ""


def getLocation(elem):
    try:
        location = elem.find("location").get("file")
        if (location == ""):
            location = elem.find("includes").text
        return location
    except Exception as error:
        useful.printExceptionVerbose(error)
        return ""


def getFunctionDetailedDesc(elem):
    detailedDesc = ""
    try:
        detailedDesc += strOp.epurStr(elem.find("detaileddescription/para").text)
        if elem.find("detaileddescription/para/simplesect").get("kind") == 'note':
            for token in elem.find("detaileddescription/para/simplesect").itertext():
                detailedDesc += " " + token.replace('\n', '').replace('\t', '')
        return strOp.epurStr(detailedDesc)
    except Exception as error:
        useful.printExceptionVerbose(error)
        return detailedDesc


def getBriefDesc(elem):
    try:
        briefDesc = ""
        for token in elem.find("briefdescription").itertext():
            briefDesc += token
        return strOp.epurStr(briefDesc)
    except Exception as error:
        useful.printExceptionVerbose(error)
        return ""


def getReturnDesc(elem):
    try:
        tmp = ""
        for simplesect in elem.findall("detaileddescription/para/simplesect"):
            if simplesect.get("kind") == "return":
                for ret in simplesect.itertext():
                    tmp += " " + strOp.epurStr(ret)
        tmp = strOp.epurStr(tmp)
        return tmp
    except Exception as error:
        useful.printExceptionVerbose(error)
        return ""


def getParams(define):
    params = []
    try:
        for param in define.findall("param"):
            tmpParam = variableClass()
            try:
                tmpParam.name = strOp.epurStr(param.find("defname").text)
            except Exception as error:
                useful.printExceptionVerbose(error)
                tmpParam.name = strOp.epurStr(param.find("declname").text)
            tmpParam.type = getType(param)
            params.append(tmpParam)
        return params
    except Exception as error:
        useful.printExceptionVerbose(error)
        return params


def removeFromDetailedDescParams(desc, params):
    if len(params) > 0 and params[0].name in desc:
        index = desc.find(params[0].name)
        desc = desc[:index]
    return desc


def getParamDesc(elem, params):
    try:
        for param in elem.find("detaileddescription/para/parameterlist").findall("parameteritem"):
            name = strOp.epurStr(param.find("parameternamelist/parametername").text)
            tmp = ""
            for txt in param.find("parameterdescription").itertext():
                tmp += " " + strOp.epurStr(txt)
            for param in params:
                if param.name == name:
                    param.desc = strOp.epurStr(tmp)
                    break
        return params
    except Exception as error:
        useful.printExceptionVerbose(error)
        return params


def getRetvals(elem):
    retvals = []
    try:
        for parameterlist in elem.findall("detaileddescription/para/parameterlist"):
            if parameterlist.get("kind") == "retval":
                for retval in parameterlist.findall("parameteritem"):
                    tmp = variableClass()
                    tmpName = ""
                    for txt in retval.find("parameternamelist/parametername").itertext():
                        tmpName += " " + strOp.epurStr(txt)
                    tmpDesc = ""
                    for txt in retval.find("parameterdescription").itertext():
                        tmpDesc += " " + strOp.epurStr(txt)
                    tmp.value = strOp.epurStr(tmpName)
                    tmp.desc = strOp.epurStr(tmpDesc)
                    retvals.append(tmp)
        return retvals
    except Exception as error:
        useful.printExceptionVerbose(error)
        return retvals
