from src.classes import functionClass
import src.getters as getters

def getFunction(elem):
    tmpFunction = functionClass()

    tmpFunction.name = getters.getName(elem)
    tmpFunction.returnType = getters.getType(elem)
    tmpFunction.returnComment = getters.getReturnComment(elem)
    tmpFunction.params = getters.getParams(elem)
    tmpFunction.briefDesc = getters.getBriefDesc(elem)
    tmpFunction.detailedDesc = getters.getDetailedDesc(elem)
    
    return tmpFunction