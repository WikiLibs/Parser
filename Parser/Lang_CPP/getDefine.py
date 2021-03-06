from Lang_CPP.utility import buildDefinePrototype
from genericClasses import buildDefine
import getters as getters

def getDefine(define):
    name = getters.getName(define)
    params = getters.getParamDesc(define, getters.getParams(define))
    briefDesc = getters.getBriefDesc(define)
    detailedDesc = getters.getDetailedDesc(define)
    return buildDefine(path=name, prototypeObj=buildDefinePrototype(name, briefDesc, detailedDesc, params), importString=define.find("location").get("file"))
