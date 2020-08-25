from genericClasses import GenericPrototype
from genericClasses import buildParameter
import getters as getters

def buildFunctionPrototype(protoPrefix, protoSuffix, name, returnType, briefDesc, detailedDesc, parameters, returnDesc):
    pObj = GenericPrototype()
    funcProto = returnType + " " + name + "("
    if (len(parameters) > 0):
        for par in parameters:
            proto = par.type + " " + par.name
            if (par.value != None and len(par.value) > 0):
                proto = proto + " = " + par.value
            funcProto = funcProto + proto + ", "
            pObj.addParameter(buildParameter(prototype=proto, description=par.desc))
        funcProto = funcProto[:-2]
    if (len(returnDesc) > 0):
        pObj.addParameter(buildParameter(prototype="return", description=returnDesc))
    funcProto = funcProto + ")"
    funcProto = protoPrefix + " " + funcProto + protoSuffix
    pObj.prototype = funcProto
    pObj.description = briefDesc
    if (len(detailedDesc) > 0):
        pObj.description = detailedDesc
    return (pObj)

def buildDefinePrototype(name, briefDesc, detailedDesc, parameters):
    pObj = GenericPrototype()
    funcProto = "#define " + name + "("
    if (len(parameters) > 0):
        for par in parameters:
            funcProto = funcProto + par.name + ", "
            pObj.addParameter(buildParameter(prototype=par.name, description=par.desc))
        funcProto = funcProto[:-2]
    funcProto = funcProto + ")"
    pObj.prototype = funcProto
    pObj.description = briefDesc
    if (len(detailedDesc) > 0):
        pObj.description = detailedDesc
    return (pObj)

class Reference:
    def __init__(self, name):
        self.name = name
        self.path = self.Name.replace("::", "/")

def resolveReference(refid):
    name = getters.getRefName(refid)
    if (name == None):
        return (None)
    return (Reference(name))
