import re
import src.strOperations as strOp
from src.classes import defineClass
import src.getters as getters


def getDefine(define):
    params = []
    tmpDefine = defineClass()
    
    tmpDefine.name = getters.getName(define)
    tmpDefine.initializer = getters.getInitializer(define)
    tmpDefine.briefDesc = getters.getBriefDesc(define)
    tmpDefine.detailedDesc = getters.removeFromDetailedDescParams(getters.getDetailedDesc(define), getters.getParamsName(define))
    tmpDefine.params = getters.getParamsName(define)
    #tmpDefine.params = getParams(define, getParamsName(define))
    return tmpDefine