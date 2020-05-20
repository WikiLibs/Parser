from classes import classClass
import useful
import PyQt.inputsWindow as inputsWindow
from Lang_Python.getVariable import getVariable
from Lang_Python.getFunction import getFunction
from genericClasses import buildClass
from genericClasses import buildPrototype
from genericClasses import buildVariable
from genericClasses import buildFunction
from genericClasses import buildParameter
import getters as getters


# def getClassOld(classRoot):
#     tmpClass = classClass()

#     tmpClass.name = getters.getCompoundName(classRoot)
#     tmpClass.name = tmpClass.name[tmpClass.name.find('::') + 2:]
#     tmpClass.include = getters.getLocation(classRoot.find("compounddef"))

#     for elem in classRoot.iter('memberdef'):
#         kind = elem.get('kind')
#         if kind == 'variable':
#             tmpClass.variables.append(getVariable(elem))
#         if kind == 'function':
#             tmpClass.functions.append(getFunction(elem))

#     return tmpClass

def getClass(classRoot):
    syms = []
    prefix = useful.prefix
    if prefix == "":
        prefix = inputsWindow.prefix
    name = getters.getCompoundName(classRoot)
    name = name[name.find('::') + 2:]
    include = getters.getLocation(classRoot.find("compounddef"))
    briefDesc = getters.getBriefDesc(classRoot.find("compounddef"))

    classProto = buildPrototype("class " + name, briefDesc)
    classSym = buildClass(path=name, prototypeObj=classProto, importString=include)
    for elem in classRoot.iter('memberdef'):
        kind = elem.get('kind')

        if kind == 'variable':
            varName = getters.getName(elem)
            varInclude = getters.getLocation(elem)
            varType = getters.getType(elem)
            varBriefDesc = getters.getBriefDesc(elem)
            varProto = buildPrototype(varType + " " + varName, varBriefDesc)
            syms.append(buildVariable(path=(name + "/" + varName), prototypeObj=varProto, importString=varInclude))
            classSym.addMember(prefix + name + "/" + varName)

        if kind == 'function':
            funcName = getters.getName(elem)
            funcInclude = getters.getLocation(elem)
            funcParams = getters.getParamDesc(elem, getters.getParams(elem))
            funcBriefDesc = getters.getBriefDesc(elem)
            funcReturnType = getters.getType(elem)
            funcReturnDesc = getters.getReturnDesc(elem)
            funcProto = buildPrototype(funcReturnType + " " + funcName + "(", funcBriefDesc)
            for param in funcParams:
                paramProto = param.type + " " + param.name
                funcProto.prototype += paramProto + ", "
                funcProto.addParameter(buildParameter(prototype=paramProto, description=param.desc))
            funcProto.prototype = funcProto.prototype[:-2]
            funcProto.prototype += ")"
            funcProto.addParameter(buildParameter(prototype="return", description=funcReturnDesc))
            syms.append(buildFunction(path=(name + "/" + funcName), prototypeObj=funcProto, importString=funcInclude))
            classSym.addMember(prefix + name + "/" + funcName)
    syms.append(classSym)
    return syms
