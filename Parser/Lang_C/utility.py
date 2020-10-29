from genericClasses import GenericPrototype
from genericClasses import buildParameter

def buildDefinePrototype(name, briefDesc, detailedDesc, parameters):
    pObj = GenericPrototype()
    pObj.prototype = "#define " + name
    pObj.description = briefDesc
    if (len(detailedDesc) > 0):
        pObj.description = detailedDesc
    return pObj

