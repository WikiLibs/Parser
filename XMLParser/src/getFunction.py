from classes import functionClass
import getters as getters
import strOperations as strOp

def getFunction(elem):
    tmpFunction = functionClass()

    tmpFunction.name = getters.getName(elem)
    tmpFunction.returnType = getters.getType(elem)
    tmpFunction.returnComment = getters.getReturnComment(elem)
    params = getters.getParams(elem)
    tmpFunction.briefDesc = getters.getBriefDesc(elem)
    tmpFunction.detailedDesc = getters.removeFromDetailedDescParams(getters.getDetailedDesc(elem), getters.getParamsName(elem))
    
    return tmpFunction