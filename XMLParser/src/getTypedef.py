from classes import typedefClass
import getters as getters
import strOperations as strOp

def getTypedef(elem):
    tmpTypedef = typedefClass()

    tmpTypedef.tdType = getters.getType(elem)
    try:
        tmp = strOp.epurStr(elem.find("argsstring").text)
        tmpTypedef.tdType = strOp.epurStr(tmpTypedef.tdType + tmp)
    except:
        pass
    tmpTypedef.tdName = getters.getName(elem)
    tmpTypedef.briefDesc = getters.getBriefDesc(elem)
    tmpTypedef.detailedDesc = getters.getDetailedDesc(elem)

    return tmpTypedef