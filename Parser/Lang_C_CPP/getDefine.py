from classes import defineClass
from Lang_C_CPP.utility import buildDefinePrototype
from genericClasses import buildPrototype
from genericClasses import buildDefine
import getters as getters


def getDefineOld(define):
    tmpDefine = defineClass()

    tmpDefine.name = getters.getName(define)
    tmpDefine.include = getters.getLocation(define)
    tmpDefine.initializer = getters.getInitializer(define)
    tmpDefine.params = getters.getParamDesc(define, getters.getParams(define))
    tmpDefine.briefDesc = getters.getBriefDesc(define)
    tmpDefine.detailedDesc = getters.getDetailedDesc(define)
    return tmpDefine

def getDefine(define):
    name = getters.getName(define)
    include = getters.getLocation(define)
    params = getters.getParamDesc(define, getters.getParams(define))
    briefDesc = getters.getBriefDesc(define)
    detailedDesc = getters.getDetailedDesc(define)

    # buildDefinePrototype(name, briefDesc, detailedDesc, params)
    defineProto = buildPrototype("#define " + name, briefDesc)
    return buildDefine(path=name, prototypeObj=defineProto, importString=include)
