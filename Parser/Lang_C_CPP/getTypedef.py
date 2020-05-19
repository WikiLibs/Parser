from classes import typedefClass
import getters as getters
import strOperations as strOp
from genericClasses import buildTypedef
from genericClasses import buildPrototype
from genericClasses import buildParameter
import useful


def getTypedefOld(elem):
    tmpTypedef = typedefClass()

    tmpTypedef.tdType = getters.getType(elem)
    tmpTypedef.include = getters.getLocation(elem)
    try:
        tmp = strOp.epurStr(elem.find("argsstring").text)
        tmpTypedef.tdType = strOp.epurStr(tmpTypedef.tdType + tmp)
    except Exception as error:
        useful.printExceptionVerbose(error)
        pass
    tmpTypedef.tdName = getters.getName(elem)
    tmpTypedef.briefDesc = getters.getBriefDesc(elem)
    tmpTypedef.detailedDesc = getters.getDetailedDesc(elem)
    return tmpTypedef

def getTypedef(elem):
    tdType = getters.getType(elem)
    include = getters.getLocation(elem)
    try:
        tmp = strOp.epurStr(elem.find("argsstring").text)
        tdType = strOp.epurStr(tdType + tmp)
    except Exception as error:
        useful.printExceptionVerbose(error)
        pass
    tdName = getters.getName(elem)
    briefDesc = getters.getBriefDesc(elem)
    detailedDesc = getters.getDetailedDesc(elem)
    typedefProto = buildPrototype("typedef " + tdName + " " + tdType, briefDesc)
    return [buildTypedef(path=tdName, prototypeObj=typedefProto, importString=include)]
