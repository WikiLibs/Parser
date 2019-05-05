import re
import strOperations as strOp
from classes import defineClass
import getters as getters


def getDefine(define):
    params = []
    tmpDefine = defineClass()
    
    tmpDefine.name = getters.getName(define)
    tmpDefine.initializer = getters.getInitializer(define)
    tmpDefine.params = getters.getParamDesc(define, getters.getParams(define))
    tmpDefine.briefDesc = getters.getBriefDesc(define)
    tmpDefine.detailedDesc = getters.removeFromDetailedDescParams(getters.getDetailedDesc(define), tmpDefine.params)
    #tmpDefine.params = getters.getParamsName(define)
    #tmpDefine.params = getParams(define, getParamsName(define))
    return tmpDefine