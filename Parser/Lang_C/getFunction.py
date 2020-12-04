import useful
from classes import functionClass
import PyQt.inputsWindow as inputsWindow
from genericClasses import buildFunction
from genericClasses import buildPrototype
from genericClasses import buildParameter
import getters as getters


# def getFunctionOld(elem):
#     tmpFunction = functionClass()

#     tmpFunction.name = getters.getName(elem)
#     tmpFunction.include = getters.getLocation(elem)
#     tmpFunction.params = getters.getParamDesc(elem, getters.getParams(elem))
#     tmpFunction.briefDesc = getters.getBriefDesc(elem)
#     tmpFunction.detailedDesc = getters.getFunctionDetailedDesc(elem)
#     tmpFunction.returnType = getters.getType(elem)
#     tmpFunction.returnDesc = getters.getReturnDesc(elem)
#     tmpFunction.returnValues = getters.getRetvals(elem)
#     return tmpFunction

def getFunction(elem):
    syms = []
    prefix = useful.prefix
    if prefix == "":
        prefix = inputsWindow.prefix
    name = getters.getName(elem)
    include = getters.getLocation(elem)
    params = getters.getParamDesc(elem, getters.getParams(elem))
    briefDesc = getters.getBriefDesc(elem)
    detailedDesc = getters.getFunctionDetailedDesc(elem)
    returnType = getters.getType(elem)
    returnDesc = getters.getReturnDesc(elem)
    returnValues = getters.getRetvals(elem)

    funcProto = buildPrototype(returnType + " " + name + "(", briefDesc)
    for param in params:
        proto = param.type + " " + param.name
        funcProto.prototype += proto + ", "
        funcProto.addParameter(buildParameter(prototype=proto, description=param.desc))
    if len(params) != 0:
        funcProto.prototype = funcProto.prototype[:-2]
    funcProto.prototype += ")"
    funcProto.addParameter(buildParameter(prototype="return", description=returnDesc))
    syms.append(buildFunction(path=prefix + name, prototypeObj=funcProto, importString=include))
    return syms
