import sys

from PyQt.welcomeWindow import WelcomeWindow
from PyQt.inputsWindow import InputsWindow
from PyQt.summaryWindow import SummaryWindow
from PyQt.processingWindow import ProcessingWindow
from PyQt.endWindow import EndWindow

from PyQt5 import QtWidgets

WIDTH = 640
HEIGHT = 480


class Controller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    def show_WelcomeWindow(self, param_arg):
        self.welcome = WelcomeWindow(param_arg, self.width, self.height)
        self.welcome.switch_window.connect(self.show_InputInfoWindow)
        self.welcome.show()

    def show_InputInfoWindow(self, param_arg):
        self.input = InputsWindow(param_arg)
        self.input.switch_window.connect(self.show_SummaryWindow)
        self.welcome.close()
        self.input.show()

    def show_SummaryWindow(self, param_arg, libname, liblang, libpath, apiKey):
        self.param_arg = param_arg
        self.summary = SummaryWindow(param_arg, libname, liblang, libpath, apiKey, self.width, self.height)
        self.summary.switch_window.connect(self.show_ProcessingWindow)
        self.input.close()
        self.summary.show()

    def show_ProcessingWindow(self, param_arg, libname, liblang, libpath, apiKey):
        self.summary.close()
        self.process = ProcessingWindow()
        self.process.setParamArg(param_arg)
        self.process.setLibName(libname)
        self.process.setLibLang(liblang)
        self.process.setLibPath(libpath)
        self.process.setApiKey(apiKey)
        self.process.show()

        self.process.startProcessing()
        self.process.switch_window.connect(self.show_EndWindow)

    def show_EndWindow(self):
        self.end = EndWindow(self.width, self.height)
        self.process.close()
        self.end.show()


def graphicalClient(program_args):
    # Create Qt application
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller(WIDTH, HEIGHT)
    controller.show_WelcomeWindow(program_args)
    return_val = app.exec_()
    return return_val
