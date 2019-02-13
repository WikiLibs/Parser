import re
import src.strOperations as strOp
from src.classes import defineClass

def getName(define):
    return strOp.epurStr(define.find("name").text)


def getInitializer(define):
    try:
        init = strOp.epurStr(define.find("initializer").text)
    except:
        init = "none"
    return init


def getParams(define):
    params = []
    try:
        for param in define.findall("param"):
            params.append(strOp.epurStr(param.find("defname").text))
    except:
        pass
    return params


def getBriefDefinition(define):
    try:
        bd = strOp.epurStr(define.find("briefdescription").text)
        if len(bd) <= 1:
            bd = "none"
    except:
        bd = "none"
    return bd


def getDetailedDefinition(define):
    try:
        dd = strOp.epurStr(define.find("detaileddescription").find("para").text)
    except:
        dd = "none"
    return dd

def getSourceFile(define):
    return strOp.epurStr(define.find("location").get("file"))

def getSourceLine(define):
    return strOp.epurStr(define.find("location").get("line"))

def getDefine(define):
    tmpDefine = defineClass()
    
    tmpDefine.name = getName(define)
    tmpDefine.initializer = getInitializer(define)
    tmpDefine.params = getParams(define)
    tmpDefine.briefDesc = getBriefDefinition(define)
    tmpDefine.detailedDesc = getDetailedDefinition(define)
    tmpDefine.sourceFile = getSourceFile(define)
    tmpDefine.sourceLine = getSourceLine(define)
    
    return tmpDefine