from classes import typedefClass
import getters as getters
import strOperations as strOp
import useful
from genericClasses import buildTypedef
from genericClasses import buildPrototype
from genericClasses import buildParameter


# def getTypedefOld(elem):
#     tmpTypedef = typedefClass()

#     tmpTypedef.tdType = getters.getType(elem)
#     tmpTypedef.include = getters.getLocation(elem)
#     try:
#         tmp = strOp.epurStr(elem.find("argsstring").text)
#         tmpTypedef.tdType = strOp.epurStr(tmpTypedef.tdType + tmp)
#     except Exception as error:
#         useful.printExceptionVerbose(error)
#         pass
#     tmpTypedef.tdName = getters.getName(elem)
#     tmpTypedef.briefDesc = getters.getBriefDesc(elem)
#     tmpTypedef.detailedDesc = getters.getDetailedDesc(elem)
#     return tmpTypedef

def getTypedef(elem):
    syms = []
    tdType = getters.getType(elem)
    include = getters.getLocation(elem)
    try:
        if elem.find("argsstring").text:
            tmp = strOp.epurStr(elem.find("argsstring").text)
        else:
            return syms
        tdType = strOp.epurStr(tdType + tmp)
    except Exception as error:
        useful.printExceptionVerbose(error)
        pass
    tdName = getters.getName(elem)
    briefDesc = getters.getBriefDesc(elem)
    detailedDesc = getters.getDetailedDesc(elem)
    typedefProto = buildPrototype("typedef " + tdName + " " + tdType, briefDesc)
    syms.append(buildTypedef(path=tdName, prototypeObj=typedefProto, importString=include))
    return syms
