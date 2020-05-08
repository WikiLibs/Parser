from classes import defineClass
import getters as getters


def getDefine(define):
    tmpDefine = defineClass()

    tmpDefine.name = getters.getName(define)
    tmpDefine.initializer = getters.getInitializer(define)
    tmpDefine.params = getters.getParamDesc(define, getters.getParams(define))
    tmpDefine.briefDesc = getters.getBriefDesc(define)
    tmpDefine.detailedDesc = getters.getDetailedDesc(define)
    return tmpDefine
