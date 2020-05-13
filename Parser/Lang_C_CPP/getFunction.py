from classes import functionClass
import getters as getters


def getFunction(elem):
    tmpFunction = functionClass()

    tmpFunction.name = getters.getName(elem)
    tmpFunction.include = getters.getLocation(elem)
    tmpFunction.params = getters.getParamDesc(elem, getters.getParams(elem))
    tmpFunction.briefDesc = getters.getBriefDesc(elem)
    tmpFunction.detailedDesc = getters.getFunctionDetailedDesc(elem)
    tmpFunction.returnType = getters.getType(elem)
    tmpFunction.returnDesc = getters.getReturnDesc(elem)
    tmpFunction.returnValues = getters.getRetvals(elem)

    return tmpFunction
