#!/usr/bin/python3.6

from jsonClasses import SymbolUpdate, SymbolPrototype, SymbolParam, SymbolException
import useful

g_lang = ""
g_lib = ""

def autoBuildSymbol(client, path, type, prototype):
    sym = SymbolUpdate("")
    sym.setPath(path)
    sym.setLang(g_lang)
    sym.setType(type)
    p = SymbolPrototype("")
    p.setPrototype(prototype)
    p.setDescription("Auto-generated symbol")
    sym.appendPrototypes(p)
    client.PushSymbol(sym)


def craftGenericRequest(lang, lib, client, list):
    useful.printVerbose("\n\n/****  Begin crafting of generic symbol requests  ****/")
    map = {}
    pathPrefix = lang + "/" + lib + "/"
    useful.printVerbose("> Building and uploading JSON...")
    for ss in list:
        sym = SymbolUpdate("")
        sym.setPath(pathPrefix + ss.path)
        sym.setLang(lang)
        sym.setType(ss.typename)
        sym.setImport(ss.importString)
        for proto in ss.prototypes:
            p = SymbolPrototype("")
            p.setPrototype(proto.prototype)
            p.setDescription(proto.description)
            for par in proto.parameters:
                if (par.linkedSymbol != None and par.linkedSymbol.startswith("AUTOGEN:")):
                    par.linkedSymbol = par.linkedSymbol[8:]
                    autoBuildSymbol(client, pathPrefix + par.linkedSymbol, "class", "class " + par.linkedSymbol)
                parpar = SymbolParam("")
                parpar.setPrototype(par.prototype)
                parpar.setDescription(par.description)
                if (par.linkedSymbol != None):
                    parpar.setPath(pathPrefix + par.linkedSymbol)
                p.appendParameters(parpar)
            for ex in proto.exceptions:
                if (ex.linkedSymbol != None and ex.linkedSymbol.startswith("AUTOGEN:")):
                    ex.linkedSymbol = ex.linkedSymbol[8:]
                    autoBuildSymbol(client, pathPrefix + ex.linkedSymbol, "class", "class " + ex.linkedSymbol)
                exex = SymbolException("")
                if (ex.linkedSymbol != None):
                    exex.setPath(pathPrefix + ex.linkedSymbol)
                exex.setDescription(ex.description)
                p.appendExceptions(exex)
            sym.appendPrototypes(p)
        for path in ss.linkedSymbols:
            sym.appendSymbols(pathPrefix + path)
        client.PushSymbol(sym)
    useful.printVerbose("End crafting of generic symbol requests")
    client.Optimize()
