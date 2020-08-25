#!/usr/bin/python3.6

from jsonClasses import SymbolUpdate, SymbolPrototype, SymbolParam, SymbolException
import useful

g_lang = ""
g_lib = ""


def craftStructRequest(client, structs): #import
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Struct Request  ****/")
    for struct in structs:
        useful.printVerbose("Crafting " + struct.name)
        sym = SymbolUpdate(struct.name)
        sym.setLang(g_lang)
        sym.setType("struct")
        sym.setImport(struct.include)
        sym_proto = SymbolPrototype(struct.name)
        sym_proto.setDescription(struct.detailedDesc)
        sym_proto.setPrototype("struct " + struct.name)
        sym.appendPrototypes(sym_proto)
        useful.printVerbose("Crafting " + struct.name + " is done")
        useful.printVerbose("Now Getting " + struct.name + " members")
        for member in struct.members:
            useful.printVerbose("Setting " + member.name)
            mem = SymbolUpdate(member.name)
            mem.setLang(g_lang)
            mem.setType("attribute")
            sym.appendSymbols(g_lang + "/" + g_lib + "/" + struct.name + "/" + member.name)
            mem_proto = SymbolPrototype(member.name)
            mem_proto.setDescription(member.desc)
            mem_proto.setPrototype(member.type + " " + member.name)
            mem.appendPrototypes(mem_proto)
            path = g_lang + "/" + g_lib + "/" + struct.name + "/" + member.name
            mem.setPath(path)
            useful.printVerbose("Path is " + path)
            client.PushSymbol(mem)
        useful.printVerbose("Finished getting " + struct.name + " members")
        path = g_lang + "/" + g_lib + "/" + struct.name
        sym.setPath(path)
        useful.printVerbose("Pushing " + struct.name + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Struct Request")


def craftDefineRequest(client, defines): #import
    global g_lang
    global g_lib

    # enlever le define de protextion
    useful.printVerbose("\n\n/****  Beginning crafting Define Request  ****/")
    for define in defines:
        useful.printVerbose("Crafting " + define.name)
        sym = SymbolUpdate(define.name)
        sym.setLang(g_lang)
        sym.setType("macro")
        sym.setImport(define.include)
        sym_proto = SymbolPrototype(define.name)
        sym_proto.setDescription(define.detailedDesc)
        sym_proto.setPrototype("#define " + define.name + " " + define.initializer)
        useful.printVerbose("Crafting " + define.name + " is done")
        useful.printVerbose("Now Getting " + define.name + " parametters")
        for param in define.params:
            useful.printVerbose("Setting " + param.name)
            sym_param = SymbolParam(param.name)
            sym_param.setPrototype(param.name)
            sym_param.setDescription(param.desc)
            sym_proto.appendParameters(sym_param)
        useful.printVerbose("Finished getting " + define.name + " members")
        sym.appendPrototypes(sym_proto)
        path = g_lang + "/" + g_lib + "/" + define.name
        sym.setPath(path)
        useful.printVerbose("Pushing " + define.name + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Define Request")


def craftUnionRequest(client, unions): #import
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Union Request  ****/")
    for union in unions:
        sym = SymbolUpdate(union.name)
        sym.setLang(g_lang)
        sym.setType("union")
        sym.setImport(union.include)
        sym_proto = SymbolPrototype(union.name)
        sym_proto.setDescription(union.detailedDesc)
        sym_proto.setPrototype("union " + union.name)
        sym.appendPrototypes(sym_proto)
        useful.printVerbose("Crafting " + union.name + " is done")
        useful.printVerbose("Now Getting " + union.name + " members")
        for member in union.members:
            useful.printVerbose("Setting " + member.name)
            mem = SymbolUpdate(member.name)
            mem.setLang(g_lang)
            mem.setType("attribute")
            sym.appendSymbols(g_lang + "/" + g_lib + "/" + union.name + "/" + member.name)
            mem_proto = SymbolPrototype(member.name)
            mem_proto.setDescription(member.desc)
            mem_proto.setPrototype(member.type + " " + member.name)
            mem.appendPrototypes(mem_proto)
            path = g_lang + "/" + g_lib + "/" + union.name + "/" + member.name
            mem.setPath(path)
            client.PushSymbol(mem)
        useful.printVerbose("Finished getting " + union.name + " members")
        path = g_lang + "/" + g_lib + "/" + union.name
        sym.setPath(path)
        useful.printVerbose("Pushing " + union.name + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Union Request")


def craftFunctionRequest(client, functions): #import
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Function Request  ****/")
    for function in functions:
        useful.printVerbose("Setting " + function.name)
        sym = SymbolUpdate(function.name)
        sym.setLang(g_lang)
        sym.setType("function")
        sym.setImport(function.include)
        sym_proto = SymbolPrototype(function.name)
        sym_proto.setDescription(function.detailedDesc)
        buf = function.returnType + " " + function.name + "("
        for i in range(0, len(function.params)):
            if i != 0:
                buf += ", "
            buf += function.params[i].type + " " + function.params[i].name
        buf += ")"
        sym_proto.setPrototype(buf)
        par_proto = SymbolParam("return")
        par_proto.setDescription(function.returnDesc)
        par_proto.setPrototype("return")
        sym_proto.appendParameters(par_proto)
        for param in function.params:
            useful.printVerbose("Found param " + param.name)
            par_proto = SymbolParam(param.name)
            par_proto.setDescription(param.desc)
            par_proto.setPrototype(param.type + " " + param.name)
            sym_proto.appendParameters(par_proto)
        sym.appendPrototypes(sym_proto)
        path = g_lang + "/" + g_lib + "/" + function.name
        sym.setPath(path)
        useful.printVerbose("Pushing " + function.name + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Function Request")


def craftTypedefRequest(client, typedefs): #import
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Typedef Request  ****/")
    for typedef in typedefs:
        useful.printVerbose("Setting " + typedef.tdName)
        sym = SymbolUpdate(typedef.tdName)
        sym.setLang(g_lang)
        sym.setType("typedef")
        sym.setImport(typedef.include)
        sym_proto = SymbolPrototype(typedef.tdName)
        sym_proto.setDescription(typedef.detailedDesc)
        sym_proto.setPrototype("typedef " + typedef.tdName + " " + typedef.tdType)
        sym.appendPrototypes(sym_proto)
        path = g_lang + "/" + g_lib + "/" + typedef.tdName
        sym.setPath(path)
        useful.printVerbose("Pushing " + typedef.tdName + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Typedef Request")


def craftClassRequest(client, classes): #import
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Class Request  ****/")
    for classe in classes:
        useful.printVerbose("Setting " + classe.name)
        sym = SymbolUpdate(classe.name)
        sym.setLang(g_lang)
        sym.setType("class")
        sym.setImport(classe.include)
        sym_proto = SymbolPrototype(classe.name)
        sym_proto.setDescription(classe.description)
        sym_proto.setPrototype("class " + classe.name)
        sym.appendPrototypes(sym_proto)
        useful.printVerbose("Crafting " + classe.name + " is done")
        useful.printVerbose("Now Getting " + classe.name + " variables")
        for variable in classe.variables:
            useful.printVerbose("Setting " + variable.name)
            mem = SymbolUpdate(variable.name)
            mem.setLang(g_lang)
            mem.setType("member attribute")
            sym.appendSymbols(g_lang + "/" + g_lib + "/" + classe.name + "/" + variable.name)
            mem_proto = SymbolPrototype(variable.name)
            mem_proto.setDescription(variable.desc)
            mem_proto.setPrototype(variable.type + " " + variable.name)
            mem.appendPrototypes(mem_proto)
            path = g_lang + "/" + g_lib + "/" + classe.name + "/" + variable.name
            mem.setPath(path)
            useful.printVerbose("Path is " + path)
            client.PushSymbol(mem)
        useful.printVerbose("Finished getting " + classe.name + " variables")
        useful.printVerbose("Now Getting " + classe.name + " functions")
        for function in classe.functions:
            useful.printVerbose("Setting " + function.name)
            func = SymbolUpdate(function.name)
            func.setLang(g_lang)
            func.setType("member function")
            func_proto = SymbolPrototype(function.name)
            func_proto.setDescription(function.detailedDesc)
            buf = function.returnType + " " + function.name + "("
            for i in range(0, len(function.params)):
                if i != 0:
                    buf += ", "
                buf += function.params[i].type + " " + function.params[i].name
            buf += ")"
            func_proto.setPrototype(buf)
            par_proto = SymbolParam("return")
            par_proto.setDescription(function.returnDesc)
            par_proto.setPrototype("return")
            func_proto.appendParameters(par_proto)
            for param in function.params:
                useful.printVerbose("Found param " + param.name)
                par_proto = SymbolParam(param.name)
                par_proto.setDescription(param.desc)
                par_proto.setPrototype(param.type + " " + param.name)
                func_proto.appendParameters(par_proto)
            func.appendPrototypes(func_proto)
            path = g_lang + "/" + g_lib + "/" + classe.name + "/" + function.name
            func.setPath(path)
            useful.printVerbose("Path is " + path)
            client.PushSymbol(func)
        useful.printVerbose("Finished getting " + classe.name + " functions")
        path = g_lang + "/" + g_lib + "/" + classe.name
        sym.setPath(path)
        useful.printVerbose("Pushing " + classe.name + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Class Request")


def craftVariableRequest(client, variables):
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Variable Request  ****/")
    for variable in variables:
        useful.printVerbose("Setting " + variable.name)
        sym = SymbolUpdate(variable.name)
        sym.setLang(g_lang)
        sym.setType("variable")
        sym_proto = SymbolPrototype(variable.name)
        sym_proto.setDescription(variable.desc)
        sym_proto.setPrototype("variable " + variable.name + " " + variable.type)
        sym.appendPrototypes(sym_proto)
        path = g_lang + "/" + g_lib + "/" + variable.name
        sym.setPath(path)
        useful.printVerbose("Pushing " + variable.name + " on the Database")
        useful.printVerbose("Path is " + path)
        client.PushSymbol(sym)
        useful.printVerbose("Push done")
    useful.printVerbose("Ended crafting Typedef Request")


def printWIP(client, list):
    print("This feature is in WIP")


def craftGenericRequest(client, list):
    useful.printVerbose("\n\n/****  Begin crafting of generic symbol requests  ****/")
    map = {}
    pathPrefix = g_lang + "/" + g_lib + "/"
    useful.printVerbose("> Building and uploading JSON...")
    for ss in list: # Third pass: build and send JSON data
        sym = SymbolUpdate("")
        sym.setPath(pathPrefix + ss.path)
        sym.setLang(g_lang)
        sym.setType(ss.typename)
        sym.setImport(ss.importString)
        for proto in ss.prototypes:
            p = SymbolPrototype("")
            p.setPrototype(proto.prototype)
            p.setDescription(proto.description)
            for par in proto.parameters:
                parpar = SymbolParam("")
                parpar.setPrototype(par.prototype)
                parpar.setDescription(par.description)
                parpar.setPath(par.linkedSymbol)
                p.appendParameters(parpar)
            for ex in proto.exceptions:
                exex = SymbolException("")
                exex.setPath(ex.linkedSymbol)
                exex.setDescription(ex.description)
                p.appendExceptions(exex)
            sym.appendPrototypes(p)
        for path in ss.linkedSymbols:
            sym.appendSymbols(pathPrefix + path)
        client.PushSymbol(sym)
    useful.printVerbose("End crafting of generic symbol requests")

def initDicoFunction():
    dict = {}
    dict['struct'] = craftStructRequest
    dict['define'] = craftDefineRequest
    dict['union'] = craftUnionRequest
    dict['function'] = craftFunctionRequest
    dict['typedef'] = craftTypedefRequest
    dict['variable'] = craftVariableRequest
    dict['class'] = craftClassRequest
    dict['client'] = printWIP
    dict['generic'] = craftGenericRequest
    return dict


def JSONRequestCrafter(lang, lib, rawData):
    global g_lang
    global g_lib

    g_lang = lang
    g_lib = lib
    # remove rawData with a better thing
    client = ""
    dict = initDicoFunction()
    for key, val in rawData:
        if key == 'client':
            client = val
            rawData.remove((key, val))
    client.GetToken()
    useful.printVerbose("Beginning crafting Requests")
    for key, lists in rawData:
        if key in dict:
            dict[key](client, lists)
        else:
            useful.logFatal('key ' + key + ' not found in JSONRequestCrafter (line:220)', 1)
    useful.printVerbose("Finished crafting Requests")
