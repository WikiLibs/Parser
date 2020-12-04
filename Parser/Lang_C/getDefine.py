import useful
from classes import defineClass
import PyQt.inputsWindow as inputsWindow
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
    prefix = useful.prefix
    if prefix == "":
        prefix = inputsWindow.prefix
    name = getters.getName(define)
    include = getters.getLocation(define)
    initializer = getters.getInitializer(define)
    params = getters.getParamDesc(define, getters.getParams(define))
    briefDesc = getters.getBriefDesc(define)
    detailedDesc = getters.getDetailedDesc(define)

    defineProto = buildPrototype("#define " + name + " " + initializer, briefDesc)
    syms.append(buildDefine(path=prefix + name, prototypeObj=defineProto, importString=include))
    return syms
