#!/usr/bin/python3.6

from jsonClasses import SymbolUpdate, SymbolPrototype, SymbolParam
import useful

g_lang = ""
g_lib = ""


def craftStructRequest(client, structs):
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Struct Request  ****/")
    for struct in structs:
        useful.printVerbose("Crafting " + struct.name)
        sym = SymbolUpdate(struct.name)
        sym.setLang(g_lang)
        sym.setType("struct")
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


def craftDefineRequest(client, defines):
    global g_lang
    global g_lib

    # enlever le define de protextion
    useful.printVerbose("\n\n/****  Beginning crafting Define Request  ****/")
    for define in defines:
        useful.printVerbose("Crafting " + define.name)
        sym = SymbolUpdate(define.name)
        sym.setLang(g_lang)
        sym.setType("macro")
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


def craftUnionRequest(client, unions):
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Union Request  ****/")
    for union in unions:
        sym = SymbolUpdate(union.name)
        sym.setLang(g_lang)
        sym.setType("union")
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


def craftFunctionRequest(client, functions):
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Function Request  ****/")
    for function in functions:
        useful.printVerbose("Setting " + function.name)
        sym = SymbolUpdate(function.name)
        sym.setLang(g_lang)
        sym.setType("function")
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


def craftTypedefRequest(client, typedefs):
    global g_lang
    global g_lib

    useful.printVerbose("\n\n/****  Beginning crafting Typedef Request  ****/")
    for typedef in typedefs:
        useful.printVerbose("Setting " + typedef.tdname)
        sym = SymbolUpdate(typedef.tdName)
        sym.setLang(g_lang)
        sym.setType("typedef")
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


def craftVariableRequest():
    return


def craftClassRequest():
    return


def printWIP(client, list):
    print("This feature is in WIP")


def initDicoFunction():
    dict = {}
    dict['struct'] = craftStructRequest
    dict['define'] = craftDefineRequest
    dict['union'] = craftUnionRequest
    dict['function'] = craftFunctionRequest
    dict['typedef'] = craftTypedefRequest
    dict['variable'] = printWIP
    dict['class'] = printWIP
    dict['client'] = printWIP
    return dict


def JSONRequestCrafter(lang, lib, rawData):
    global g_lang
    global g_lib

    g_lang = lang
    g_lib = lib
    dict = initDicoFunction()
    for key, val in rawData:
        if key == 'client':
            client = val
            rawData.remove((key, val))
    useful.printVerbose("Beginning crafting Requests")
    for key, lists in rawData:
        if key in dict:
            dict[key](client, lists)
        else:
            useful.logError('key ' + key + ' not found in JSONRequestCrafter (line:220)', 1)
    useful.printVerbose("Finished crafting Requests")
    useful.printVerbose("Calling optimizer")
    client.CallOptimizer()
    useful.printVerbose("Called optimizer")
