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


'''def getParams(elem):
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
    return allVars'''


def getReturnDesc(elem):
    try:
        tmp = ""
        for simplesect in elem.findall("detaileddescription/para/simplesect"):
            if simplesect.get("kind") == "return":
                for ret in simplesect.itertext():
                    tmp += " " + strOp.epurStr(ret)
        tmp = strOp.epurStr(tmp)
        return tmp
    except:
        return ""


def getParams(define):
    params = []
    try:
        for param in define.findall("param"):
            tmpParam = variableClass()
            try:
                tmpParam.name = strOp.epurStr(param.find("defname").text)
            except:
                tmpParam.name = strOp.epurStr(param.find("declname").text)
            try:
                tmpParam.type = getType(param)
            except:
                pass
            params.append(tmpParam)
        return params
    except:
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
    except:
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
    except:
        return retvals