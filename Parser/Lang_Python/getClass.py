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
    classSym = buildClass(path=prefix + name, prototypeObj=classProto, importString=include)
    for elem in classRoot.iter('memberdef'):
        kind = elem.get('kind')

        if kind == 'variable':
            varSyms = getVariable(elem)
            for varSym in varSyms:
                classSym.addMember(prefix + name + "/" + varSym.path[len(prefix):])
                syms.append(varSym)

        if kind == 'function':
            funcSyms = getFunction(elem)
            for funcSym in funcSyms:
                classSym.addMember(prefix + name + "/" + funcSym.path[len(prefix):])
                syms.append(funcSym)
    syms.append(classSym)
    return syms
