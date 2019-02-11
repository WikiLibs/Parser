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