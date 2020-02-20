import Parser.getters as getters
from Parser.genericClasses import buildFunction
from Parser.genericClasses import buildPrototype
from classes import variableClass
from Parser.Lang_CPP.utility import buildFunctionPrototype

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
    for elem in tlist.iter('param'):
        v = variableClass()
        v.type = elem.get("type")
        v.name = elem.get("declname")
        v.value = elem.get("defval")
        params.append(v)
    detailedDesc = getters.removeFromDetailedDescParams(getters.getDetailedDesc(root), params)
    returnType = root.find("type").text
    func = buildFunctionPrototype(name, returnType, briefDesc, detailedDesc, params)
    return ([buildFunction("", func)])
