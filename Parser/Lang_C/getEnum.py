from classes import classClass
from Lang_Java.getFunction import getFunction
from Lang_Java.getVariable import getVariable
from genericClasses import buildPrototype
from genericClasses import buildVariable
from genericClasses import buildParameter
import getters as getters


# def getClassOld(classRoot):
#     tmpClass = classClass()

#     tmpClass.name = getters.getCompoundName(classRoot)
#     tmpClass.name = tmpClass.name[tmpClass.name.find('::') + 2]

#     for elem in classRoot.iter('memberdef'):
#         kind = elem.get('kind')
#         if kind == 'variable':
#             tmpClass.variables.append(getVariable(elem))
#         if kind == 'variable':
#             tmpClass.variables.append(getVariable(elem))
#         if kind == 'function':
#             tmpClass.functions.append(getFunction(elem))

#     return tmpClass

def getEnum(elem):
    syms = []
    name = getters.getName(elem)
    include = getters.getLocation(elem)
    params = getters.getEnumParams(elem)
    briefDesc = getters.getBriefDesc(elem)
    detailedDesc = getters.getDetailedDesc(elem)

    enumProto = buildPrototype("enum " + name + " { ", briefDesc)
    for param in params:
        if param.initializer != "":
            proto = param.name + param.initializer
        else:
            proto = param.name
        enumProto.prototype += proto + ", "
        enumProto.addParameter(buildParameter(prototype=proto, description=param.desc))
    if len(params) != 0:
        enumProto.prototype = enumProto.prototype[:-2]
    enumProto.prototype += " }"
    enumSym = buildVariable(path=name, prototypeObj=enumProto, importString=include)
    syms.append(enumSym)
    return syms