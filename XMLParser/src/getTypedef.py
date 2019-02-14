from src.classes import typedefClass
import src.getters as getters

def getTypedef(elem):
    tmpTypedef = typedefClass()

    tmpTypedef.tdType = getters.getType(elem)
    tmpTypedef.tdName = getters.getName(elem)
    tmpTypedef.briefDesc = getters.getBriefDesc(elem)
    tmpTypedef.detailedDesc = getters.getDetailedDesc(elem)

    return tmpTypedef