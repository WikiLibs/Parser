import useful
from classes import variableClass
from genericClasses import buildVariable
from genericClasses import buildPrototype
import getters as getters


# def getVariableOld(elem):
#     tmpVariable = variableClass()

#     tmpVariable.name = getters.getName(elem)
#     tmpVariable.type = getters.getType(elem)
#     tmpVariable.value = getters.getInitializer(elem)
#     return tmpVariable

def getVariable(elem):
    syms = []
    name = getters.getName(elem)
    include = getters.getLocation(elem)
    vtype = getters.getType(elem)
    value = getters.getInitializer(elem)
    briefDesc = getters.getBriefDesc(elem)

    varProto = buildPrototype(vtype + " " + name, briefDesc)
    syms.append(buildVariable(path=useful.prefix + name, prototypeObj=varProto, importString=include))
    return syms
