from classes import variableClass
import getters as getters


def getVariable(elem):
    tmpVariable = variableClass()

    tmpVariable.name = getters.getName(elem)
    tmpVariable.type = getters.getType(elem)
    tmpVariable.value = getters.getInitializer(elem)
    return tmpVariable
