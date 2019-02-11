import re

def epurStr(string):
    return re.sub(' +', ' ', string).strip()