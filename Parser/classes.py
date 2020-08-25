class variableClass:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.value = ""
        self.desc = ""
        self.ref = ""


class defineClass:
    def __init__(self):
        self.name = ""
        self.include = ""
        self.initializer = ""
        self.params = []
        self.briefDesc = ""
        self.detailedDesc = ""


class structClass:
    def __init__(self):
        self.name = ""
        self.include = ""
        self.members = []
        self.briefDesc = ""
        self.detailedDesc = ""


class unionClass:
    def __init__(self):
        self.name = ""
        self.include = ""
        self.members = []
        self.briefDesc = ""
        self.detailedDesc = ""


class functionClass:
    def __init__(self):
        self.name = ""
        self.include = ""
        self.briefDesc = ""
        self.detailedDesc = ""
        self.params = []
        self.returnType = ""
        self.returnDesc = ""
        self.returnValues = []


class typedefClass:
    def __init__(self):
        self.tdType = ""
        self.include = ""
        self.tdName = ""
        self.briefDesc = ""
        self.detailedDesc = ""


class classClass:
    def __init__(self):
        self.name = ""
        self.include = ""
        self.description = ""
        self.variables = []
        self.functions = []

class exceptionClass:
    def __init__(self):
        self.description = ""
        self.reference = ""
        self.typename = ""
