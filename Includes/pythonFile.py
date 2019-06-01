RANDOM_VARIABLE = 'HELLO'
"""
I hope this comment goes USEFUL_STRING
"""
USEFUL_STRING = 'HI I\'M A STRING'  # Is this okay


class pythonClass:
    def __init__(self, paramInit1, paramInit2):
        self.param1 = paramInit1
        self.param2 = paramInit2
        print('I\'m a test')

    def normalClassFunction(self, niceParameter):
        tmp = self.param1 + self.param2 + niceParameter
        return tmp
