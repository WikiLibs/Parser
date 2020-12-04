import useful
from classes import functionClass
from genericClasses import buildFunction
from genericClasses import buildPrototype
from genericClasses import buildParameter
from genericClasses import buildException
import getters as getters


# def getFunctionOld(elem):
#     tmpFunction = functionClass()

#     tmpFunction.name = getters.getName(elem)
#     tmpFunction.include = getters.getLocation(elem)
#     tmpFunction.params = getters.getParams(elem)
#     tmpFunction.value = getters.getRetvals(elem)
#     return tmpFunction

def getFunction(elem):
    syms = []
    name = getters.getName(elem)
    include = getters.getLocation(elem)
    params = getters.getParamDesc(elem, getters.getParams(elem))
    briefDesc = getters.getBriefDesc(elem)
    detailedDesc = getters.getFunctionDetailedDesc(elem)
    returnType = getters.getType(elem)
    exceptions = getters.getExceptions(elem)
    returnDesc = getters.getReturnDesc(elem)
    returnValues = getters.getRetvals(elem)

    funcProto = buildPrototype(returnType + " " + name + "(", briefDesc)
    for param in params:
        proto = param.name
        funcProto.prototype += proto + ", "
        funcProto.addParameter(buildParameter(prototype=proto, description=param.desc))
    for ex in exceptions:
        funcProto.addException(buildException(linkedSymbol=ex.typename, description=ex.description))
    if len(params) != 0:
        funcProto.prototype = funcProto.prototype[:-2]
    funcProto.prototype += ")"
    funcProto.addParameter(buildParameter(prototype="return", description=returnDesc))
    syms.append(buildFunction(path=name, prototypeObj=funcProto, importString=include))
    return syms
