from classes import functionClass
import getters as getters


def getFunction(elem):
    tmpFunction = functionClass()

    tmpFunction.name = getters.getName(elem)
    tmpFunction.params = getters.getParams(elem)
    tmpFunction.value = getters.getRetvals(elem)
    return tmpFunction
