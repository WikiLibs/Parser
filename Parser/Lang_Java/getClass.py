from classes import classClass
from Lang_Java.getFunction import getFunction
from Lang_Java.getVariable import getVariable
import getters as getters


def getClass(classRoot):
    tmpClass = classClass()

    tmpClass.name = getters.getCompoundName(classRoot)
    tmpClass.name = tmpClass.name[tmpClass.name.find('::') + 2]

    for elem in classRoot.iter('memberdef'):
        kind = elem.get('kind')
        if kind == 'variable':
            tmpClass.variables.append(getVariable(elem))
        if kind == 'variable':
            tmpClass.variables.append(getVariable(elem))
        if kind == 'function':
            tmpClass.functions.append(getFunction(elem))

    return tmpClass