from genericClasses import GenericPrototype
from genericClasses import buildParameter
from genericClasses import buildException
import getters as getters

def buildFunctionPrototype(protoPrefix, protoSuffix, name, returnType, briefDesc, detailedDesc, parameters, returnDesc, exceptions):
    pObj = GenericPrototype()
    funcProto = returnType + " " + name + "("
    if (len(parameters) > 0):
        for par in parameters:
            proto = par.type + " " + par.name
            if (par.value != None and len(par.value) > 0):
                proto = proto + " = " + par.value
            funcProto = funcProto + proto + ", "
            symref = resolveReference(par.ref)
            if (symref != None):
                pObj.addParameter(buildParameter(prototype=proto, description=par.desc, linkedSymbol=symref.path))
            else:
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
    if (len(exceptions) > 0):
        for ex in exceptions:
            e = None
            if (ex.reference != None):
                e = buildException(linkedSymbol=resolveReference(ex.reference).path, description=ex.description)
            else:
                e = buildException(linkedSymbol="AUTOGEN:" + ex.typename, description=ex.description)
            pObj.addException(e)
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
        self.path = self.name.replace("::", "/")

def resolveReference(refid):
    name = getters.getRefName(refid)
    if (name == None):
        return (None)
    return (Reference(name))
