from classes import classClass
import useful
import PyQt.inputsWindow as inputsWindow
from Lang_Java.getFunction import getFunction
from Lang_Java.getVariable import getVariable
from genericClasses import buildClass
from genericClasses import buildPrototype
from genericClasses import buildVariable
from genericClasses import buildFunction
from genericClasses import buildParameter
from genericClasses import buildException
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

def getClass(classRoot):
    syms = []
    prefix = useful.prefix
    if prefix == "":
        prefix = inputsWindow.prefix
    name = getters.getCompoundName(classRoot)
    name = name[name.find('::') + 1:]
    include = getters.getLocation(classRoot.find("compounddef"))
    briefDesc = getters.getBriefDesc(classRoot.find("compounddef"))

    classProto = buildPrototype("class " + name, briefDesc)
    classSym = buildClass(path=name, prototypeObj=classProto, importString=include)
    for elem in classRoot.iter('memberdef'):
        kind = elem.get('kind')

        if kind == 'variable':
            varSyms = getVariable(elem)
            for varSym in varSyms:
                classSym.addMember(prefix + name + "/" + varSym.path[len(useful.prefix):])
                syms.append(varSym)

        if kind == 'function':
            funcSyms = getFunction(elem)
            for funcSym in funcSyms:
                classSym.addMember(prefix + name + "/" + funcSym.path[len(useful.prefix):])
                syms.append(funcSym)
    syms.append(classSym)
    return syms
