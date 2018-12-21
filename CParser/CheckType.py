TYPE_PUNC   = "TokenKind.PUNCTUATION"
TYPE_ID     = "TokenKind.IDENTIFIER"
TYPE_COMM   = "TokenKind.COMMENT"
TYPE_KEYW   = "TokenKind.KEYWORD"

PUNC_HASH   = "#"

ID_DEFINE   = "define"

def isMacro(content, index):
    if (content[index].tokType == TYPE_PUNC and content[index].tokContent == PUNC_HASH) and (content[index + 1].tokType == TYPE_ID and content[index + 1].tokContent == ID_DEFINE):
        if content[index + 3].tokContent == "(":
            return True

    return False

def isFunction(content, index):
    try:
        if (content[index].tokType == TYPE_ID or content[index].tokType == TYPE_KEYW) and content[index - 1].tokContent != PUNC_HASH: 
            while content[index + 1].tokType == TYPE_PUNC and (content[index + 1].tokContent == "*" or content[index + 1].tokContent == "&"):
                index += 1
            if content[index + 1].tokType == TYPE_ID and content[index + 2].tokContent == '(':
                return True
    except:
        return False
    return False
