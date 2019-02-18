#!/usr/bin/python3.6

import sys
from JSONClasses import SymbolUpdate, SymbolPrototype, SymbolParam, SymbolPath

g_lang = ""
g_lib = ""

def pushSymbol(path, json) :
    print(json)

def craftStructRequest(structs) :
    global g_lang
    global g_lib

    for struct in structs :
        sym = SymbolUpdate(struct.name)
        sym.setLang(g_lang)
        sym.setType("struct")
        sym_proto = SymbolPrototype(struct.name)
        sym_proto.setDescription(struct.detailedDesc)
        sym_proto.setPrototype("struct " + struct.name)
        sym.appendPrototypes(sym_proto)
        for member in struct.members :
            mem = SymbolUpdate(member.name)
            mem.setLang(g_lang)
            mem.setType("attribute")
            sym.appendSymbols(g_lang + "/" + g_lib + "/" + struct.name + "/" + member.name)
            mem_proto = SymbolPrototype(member.name)
            mem_proto.setDescription(member.desc)
            mem_proto.setPrototype(member.type + " " + member.name)
            mem.appendPrototypes(mem_proto)
            print(g_lang + "/" + g_lib + "/" + struct.name + "/" + member.name)
            print(mem.get_JSON() + "\n")
        print(g_lang + "/" + g_lib + "/" + struct.name)
        print(sym.get_JSON() + "\n")

def craftDefineRequest(defines) :
    global g_lang
    global g_lib

    for define in defines :
        sym = SymbolUpdate(define.name)
        sym.setLang(g_lang)
        sym.setType("macro")
        sym_proto = SymbolPrototype(define.name)
        sym_proto.setDescription(define.detailedDesc)
        sym_proto.setPrototype("define " + define.name)
        for param in define.params :
            sym_param = SymbolParam(param.name)
            sym_param.setPrototype(param.name)
            sym_param.setDescription(param.desc)
            sym_proto.appendParameters(sym_param)
        sym.appendPrototypes(sym_proto)
        print(g_lang + "/" + g_lib + "/" + define.name)
        print(sym.get_JSON() + "\n")

def craftUnionRequest(unions) :
    global g_lang
    global g_lib

    for union in unions :
        sym = SymbolUpdate(union.name)
        sym.setLang(g_lang)
        sym.setType("union")
        sym_proto = SymbolPrototype(union.name)
        sym_proto.setDescription(union.detailedDesc)
        sym_proto.setPrototype("union " + union.name)
        sym.appendPrototypes(sym_proto)
        for member in union.members :
            mem = SymbolUpdate(member.name)
            mem.setLang(g_lang)
            mem.setType("attribute")
            sym.appendSymbols(g_lang + "/" + g_lib + "/" + union.name + "/" + member.name)
            mem_proto = SymbolPrototype(member.name)
            mem_proto.setDescription(member.desc)
            mem_proto.setPrototype(member.type + " " + member.name)
            mem.appendPrototypes(mem_proto)
            print(g_lang + "/" + g_lib + "/" + union.name + "/" + member.name)
            print(mem.get_JSON() + "\n")
        print(g_lang + "/" + g_lib + "/" + union.name)
        print(sym.get_JSON() + "\n")

def craftFunctionRequest(functions) :
    global g_lang
    global g_lib

    for function in functions :
        sym = SymbolUpdate(function.name)
        sym.setLang(g_lang)
        sym.setType("function")
        sym_proto = SymbolPrototype(function.name)
        sym_proto.setDescription(function.detailedDesc)
        buf = function.returnType + " " + function.name + "("
        for i in range(0, len(function.params)) :
                if i != 0 :
                        buf += ", "
                buf += function.params[i].type + " " + function.params[i].name
        buf += ")"
        sym_proto.setPrototype(buf)
        par_proto = SymbolParam("return")
        par_proto.setDescription(function.returnDesc)
        par_proto.setPrototype("return")
        sym_proto.appendParameters(par_proto)
        for param in function.params :
                par_proto = SymbolParam(param.name)
                par_proto.setDescription(param.desc)
                par_proto.setPrototype(param.type + " " + param.name)
                # par_proto.setPath(g_lang + "/" + g_lib + "/" + function.name + "/" + param.name)
                sym_proto.appendParameters(par_proto)
        sym.appendPrototypes(sym_proto)
        print(g_lang + "/" + g_lib + "/" + function.name)
        print(sym.get_JSON() + "\n")

def craftTypedefRequest(typedefs) :
    global g_lang
    global g_lib

    for typedef in typedefs :
        sym = SymbolUpdate(typedef.tdName)
        sym.setLang(g_lang)
        sym.setType("typedef")
        sym_proto = SymbolPrototype(typedef.tdName)
        sym_proto.setDescription(typedef.detailedDesc)
        sym_proto.setPrototype("typedef " + typedef.tdName + " " + typedef.tdType)
        sym.appendPrototypes(sym_proto)
        print(g_lang + "/" + g_lib + "/" + typedef.tdName)
        print(sym.get_JSON() + "\n")

def JSONRequestCrafter(lang, lib, rawData) :
    global g_lang
    global g_lib

    g_lang = lang
    g_lib = lib
    craftDefineRequest(rawData[0])
    craftStructRequest(rawData[1])
    craftUnionRequest(rawData[2])
    craftFunctionRequest(rawData[3])
    craftTypedefRequest(rawData[4])
