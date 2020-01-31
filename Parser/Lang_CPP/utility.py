import GenericPrototype from genericClasses

def buildFunctionPrototype(name, namespace, returnType, description, parameters):
    pObj = GenericPrototype()
    pObj.path = namespace.replace("::", "/") + "/" + name
    funcProto = returnType + " " + name + "("
    for par in parameters:
        proto = par.type + " " + par.name
        funcProto = funcProto + proto + ", "
        pObj.addParameter(buildParameter(prototype=proto, description=par.desc))
    funcProto = funcProto[:2]
    funcProto = funcProto + ")"
    pObj.prototype = funcProto
    return (obj)
