import getters as getters
from genericClasses import buildFunction
from genericClasses import buildPrototype
from classes import variableClass
from Lang_CPP.utility import buildFunctionPrototype
from useful import logError
from useful import logInfo
from useful import logWarning

def parseFunction(root):
    protoPrefix = root.get("prot")
    if (root.get("static") == "yes"):
        protoPrefix = protoPrefix + " static"
    if (root.get("explicit") == "yes"):
        protoPrefix = protoPrefix + " explicit"
    if (root.get("inline") == "yes"):
        protoPrefix = protoPrefix + " inline"
    virt = root.get("virt")
    protoSuffix = ""
    if (root.get("const") == "yes"):
        protoSuffix = protoSuffix + " const"
    if (virt == "virtual"):
        protoPrefix = protoPrefix + " virtual"
    elif (virt == "pure-virtual"):
        protoPrefix = protoPrefix + " virtual"
        protoSuffix = protoSuffix + " = 0"
    name = getters.getName(root)
    params = getters.getParamDesc(root, getters.getParams(root))
    briefDesc = getters.getBriefDesc(root)
    tlist = root.find("templateparamlist")
    if (tlist != None):
        for elem in tlist.iter('param'):
            v = variableClass()
            v.type = elem.find("type")
            if (elem.find("declname") == None): #Found bug in Doxygen
                logWarning("A terrible error has occured in Doxygen: template is corrupted, attempting restore...")
                txt = v.type.text
                vals = txt.split(" ")
                if (len(vals) < 2):
                    logError("Unable to restore corrupted template!")
                    continue
                v.type = vals[0]
                v.name = vals[1]
                logInfo("Successfully restored corrupted template!")
            else:
                if (v.type.find("ref") != None):
                    v.ref = v.type.find("ref").get("refid")
                    v.type = v.type.find("ref").text
                    #TODO: Demangler
                else:
                    v.type = v.type.text
                v.name = elem.find("declname").text
                if (elem.find("defval") != None):
                    v.value = elem.find("defval").text
            params.append(v)
    detailedDesc = getters.removeFromDetailedDescParams(getters.getDetailedDesc(root), params)
    returnType = root.find("type")
    if (returnType.find("ref") != None):
        returnType = returnType.find("ref").text
    else:
        returnType = returnType.text
    if (returnType == None): #XML lib of python is bugged
        logError("A terrible error in Python XML has been detected: XML lib returned None when the node exists")
        returnType = ""
    func = buildFunctionPrototype(name, returnType, briefDesc, detailedDesc, params)
    func = buildFunction("", func)
    if (returnType == ""):
        func.typename = "constructor"
    return ([func])
