from Lang_CPP.getDefine import getDefine

def parseFile(root):
    syms = []
    for elem in root.iter('memberdef'):
        kind = elem.get('kind')
        if (kind == "define"):
            syms.append(getDefine(elem))
    return (syms)
