import graphicalClient as gc
import useful
import Lang_C_CPP.parserC as parserC
import Lang_Python.parserPython as parserPython
import Lang_Java.parserJava as parserJava


from urllib.request import urlopen
import os

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton


def getFunctionsLang():
    dispatch = {
        'C': parserC.parserC,
        'PYTHON3': parserPython.parserPython,
        'JAVA': parserJava.parserJava
    }
    return dispatch


class ProcessingWindow(QWidget):
    switch_window = QtCore.pyqtSignal(QLabel)

    def __init__(self, param_arg, libname, liblang, libpath):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.libname = libname
        self.liblang = liblang
        self.libpath = libpath
        self.resize(gc.WIDTH, gc.HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        self.stylesheet = """
            QWidget{
                background-color: #FFFFFF
            }

            QLabel{
                color: #202020;
            }

            QPushButton{
                background-color: #7B68EE;
                color: #FFFFFF;
                border-radius: 4px;
                padding: 10px;
            }

            QPushButton#ButtonDisabled{
                background-color: #808080;
                color: #FFFFFF;
                border-radius: 4px;
                padding: 10px;
            }
        """
        self.setStyleSheet(self.stylesheet)

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        self.buttonUp = QPushButton("Upload")
        self.buttonUp.clicked.connect(self.processUpload)
        self.buttonUp.setFixedSize(QtCore.QSize(100, 40))

        self.label1 = QLabel("Please click on the upload button.")

        self.title = QLabel("Processing...", self)
        self.title.setAlignment(QtCore.Qt.AlignHCenter)
        self.title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(self.title, 0, 0)
        self.gridLayout.addWidget(self.label1, 2, 0)
        self.gridLayout.addWidget(self.buttonUp, 2, 2)

    def processUpload(self):
        # Ne update pas
        # self.buttonUp.setStyleSheet(BUTTON_DEACTIVED)
        self.buttonUp.setObjectName('ButtonDisabled')
        self.buttonUp.clicked.connect(self.doNothing)
        self.gridLayout.addWidget(self.buttonUp, 2, 2)
        self.gridLayout.update()
        # Ne update pas

        # Process Everything to Parse
        self.runDoxyfile(self.liblang)

        files = useful.getAllFiles(self.liblang)
        dispatch = getFunctionsLang()
        for filename in files:
            useful.logInfo('Starting parsing \'' + filename.ogFilename + '\'')
            obj = dispatch[self.liblang](self.liblang, self.libname)
            obj.parseXMLFile(filename.xmlFilename)
        useful.callOptimizer()
        useful.deleteFiles()
        self.switch()

    def runDoxyfile(self, language):
        base_url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/'
        doxyfileBuffer = []
        url = base_url + useful.dicoLangDoxy[language] + '/Doxyfile'

        if language == "PYTHON3" and os.name == 'nt':
            url += 'Windows'

        with open('./Doxyfile', 'wb') as fd:
            fd.write(urlopen(url).read())
        with open('./Doxyfile', 'r') as fd:
            for line in fd.readlines():
                doxyfileBuffer.append(line)
        with open('./Doxyfile', 'w') as fd:
            for index, line in enumerate(doxyfileBuffer):
                if line[-1:] == "\n":
                    doxyfileBuffer[index] = line[0:-1]
                if line[0:6] == "INPUT ":
                    doxyfileBuffer[index] = doxyfileBuffer[index] + self.libpath
            fd.write('\n'.join(map(str, doxyfileBuffer)))

        if language == 'PYTHON3':
            fileName = 'py_filter'
            if os.name == 'nt':
                fileName += 'Windows'
            url = base_url + useful.dicoLangDoxy[language] + '/' + fileName

            if os.name != 'nt':
                with open('./py_filter', 'wb') as fd:
                    fd.write(urlopen(url).read())
                os.system('chmod +x py_filter')
            else:
                with open('./py_filter.bat', 'wb') as fd:
                    fd.write(urlopen(url).read())

        if os.name == 'nt':
            os.system('doxygen Doxyfile')
        else:
            os.system('doxygen Doxyfile > /dev/null')

    def doNothing(self):
        pass

    def switch(self):
        self.switch_window.emit(self.title)
