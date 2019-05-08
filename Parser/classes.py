class variableClass:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.value = ""
        self.desc = ""


class defineClass:
    def __init__(self):
        self.name = ""
        self.initializer = ""
        self.params = []
        self.briefDesc = ""
        self.detailedDesc = ""


class structClass:
    def __init__(self):
        self.name = ""
        self.members = []
        self.briefDesc = ""
        self.detailedDesc = ""


class unionClass:
    def __init__(self):
        self.name = ""
        self.members = []
        self.briefDesc = ""
        self.detailedDesc = ""


class functionClass:
    def __init__(self):
        self.name = ""
        self.briefDesc = ""
        self.detailedDesc = ""
        self.params = []
        self.returnType = ""
        self.returnDesc = ""
        self.returnValues = []


class typedefClass:
    def __init__(self):
        self.tdType = ""
        self.tdName = ""
        self.briefDesc = ""
        self.detailedDesc = ""