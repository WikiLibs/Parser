from classes import defineClass
from genericClasses import buildPrototype
from genericClasses import buildDefine
import getters as getters


# def getDefineOld(define):
#     tmpDefine = defineClass()

#     tmpDefine.name = getters.getName(define)
#     tmpDefine.include = getters.getLocation(define)
#     tmpDefine.initializer = getters.getInitializer(define)
#     tmpDefine.params = getters.getParamDesc(define, getters.getParams(define))
#     tmpDefine.briefDesc = getters.getBriefDesc(define)
#     tmpDefine.detailedDesc = getters.getDetailedDesc(define)
#     return tmpDefine

def getDefine(define):
    syms = []
    name = getters.getName(define)
    include = getters.getLocation(define)
    initializer = getters.getInitializer(define)
    params = getters.getParamDesc(define, getters.getParams(define))
    briefDesc = getters.getBriefDesc(define)
    detailedDesc = getters.getDetailedDesc(define)

    defineProto = buildPrototype("#define " + name + " " + initializer, briefDesc)
    syms.append(buildDefine(path=name, prototypeObj=defineProto, importString=include))
    return syms
