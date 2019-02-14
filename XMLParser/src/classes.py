class variableClass:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.value = ""
        self.desc = ""

    def __str__(self):
        return "name = " + self.name + ", type = " + self.type + ", value = " + self.value

class defineClass:
    def __init__(self):
        self.name = ""
        self.initializer = ""
        self.params = []
        self.briefDesc = ""
        self.detailedDesc = ""
        self.sourceFile = ""
        self.sourceLine = ""

    def __str__(self):
        return "name = " + self.name + ", initializer = " + self.initializer + ", params = " + " ".join(self.params) + ", brief_description = " + self.briefDesc + ", detailed_description = " + self.detailedDesc + ", source_file = " + self.sourceFile + ", line = " + self.sourceLine

class structClass:
    def __init__(self):
        self.name = ""
        self.members = []
        self.briefDesc = ""
        self.detailedDesc = ""

    def __str__(self):
        return "name = " + self.name + ", brief_desc = " + self.briefDesc + ", detailed_brief = " + self.detailedDesc

class unionClass:
    def __init__(self):
        self.name = ""
        self.members = []
        self.briefDesc = ""
        self.detailedDesc = ""

class functionClass:
    def __init__(self):
        self.name = ""
        self.returnType = ""
        self.returnComment = ""
        self.params = []
        self.briefDesc = ""
        self.detailedDesc = ""

class typedefClass:
    def __init__(self):
        self.tdType = ""
        self.tdName = ""
        self.briefDesc = ""
        self.detailedDesc = ""