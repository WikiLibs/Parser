import sys
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import os
import argparse
import useful
import aiClient

import Lang_C_CPP.parserC as parserC
import Lang_Python.parserPython as parserPython
import Lang_Java.parserJava as parserJava
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QComboBox, QFileDialog

WIDTH = 640
HEIGHT = 480

BUTTON_STYLE = """
    .QPushButton {
        border-radius: 4px;
        color: rgb(255, 255, 255);
        background-color: rgb(123, 104, 238);

        padding: 10px;
    }
"""

BUTTON_DEACTIVED = """
    .QPushButton {
        border-radius: 4px;
        color: rgb(255, 255, 255);
        background-color: rgb(100, 100, 100);

        padding: 10px;
    }
"""

def getFunctionsLang():
    dispatch = {
        'C': parserC.parserC,
        'PYTHON3': parserPython.parserPython,
        'JAVA': parserJava.parserJava
    }
    return dispatch


class WelcomeWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(object)

    def __init__(self, param_arg):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Create Layout grid
        self.gridLayout = QGridLayout(self)
        centralWidget.setLayout(self.gridLayout)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)

        title = QLabel("Welcome to the Wikilibs parser GUI interface !", self)
        title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)
        button.move(270, 270)

        imageWrapper = QLabel()
        image = QtGui.QPixmap('Assets/Images/WikiLibs_Logo')
        imageWrapper.setPixmap(image.scaled(100, 100, QtCore.Qt.KeepAspectRatio))

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(imageWrapper, 1, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(button, 2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def switch(self):
        self.switch_window.emit(self.param_arg)


class InputInfoWindow(QWidget):
    switch_window = QtCore.pyqtSignal(object, str, str, str)

    def __init__(self, param_arg):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.lib_path_txt = "Path not found - Please input a path"
        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)
        buttton2 = QPushButton('Browse Folder', self)
        buttton2.setFixedSize(QtCore.QSize(100, 40))
        buttton2.clicked.connect(self.browseLibPathFolder)

        label1 = QLabel("Library language")
        self.line_edit = QLineEdit()
        label2 = QLabel("Library name")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["C", "PYTHON3"])
        label3 = QLabel("Library path")
        self.lib_path_label = QLabel(self.lib_path_txt)

        title = QLabel("Please input the following information", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(label1, 1, 0)
        self.gridLayout.addWidget(self.line_edit, 1, 1)
        self.gridLayout.addWidget(label2, 2, 0)
        self.gridLayout.addWidget(self.combo_box, 2, 1)
        self.gridLayout.addWidget(label3, 3, 0)
        self.gridLayout.addWidget(self.lib_path_label, 3, 1)
        self.gridLayout.addWidget(buttton2, 3, 3)
        self.gridLayout.addWidget(button, 4, 3)

    def browseLibPathFolder(self):
        self.lib_path_txt = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.gridLayout.removeWidget(self.lib_path_label)
        self.lib_path_label.close()
        self.lib_path_label = QLabel(self.lib_path_txt)
        self.gridLayout.addWidget(self.lib_path_label, 3, 1)
        self.gridLayout.update()

    def switch(self):
        self.switch_window.emit(self.param_arg, self.line_edit.text(), self.combo_box.currentText(), self.lib_path_txt)


class SummaryWindow(QWidget):
    switch_window = QtCore.pyqtSignal(object, str, str, str)

    def __init__(self, param_arg, libname, liblang, libpath):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.libname = libname
        self.liblang = liblang
        self.libpath = libpath

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        button = QPushButton("Start")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)

        label1 = QLabel("Library name: " + self.libname)
        label2 = QLabel("Selected language: " + self.liblang)
        label3 = QLabel("Selected path: " + self.libpath)

        title = QLabel("Summary", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(label1, 2, 0)
        self.gridLayout.addWidget(label2, 1, 0)
        self.gridLayout.addWidget(label3, 3, 0)
        self.gridLayout.addWidget(button, 4, 0)

    def switch(self):
        self.switch_window.emit(self.param_arg, self.libname, self.liblang, self.libpath)


class ProcessingWindow(QWidget):
    switch_window = QtCore.pyqtSignal(QLabel)

    def __init__(self, param_arg, libname, liblang, libpath):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.libname = libname
        self.liblang = liblang
        self.libpath = libpath
        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        self.buttonUp = QPushButton("Upload")
        self.buttonUp.clicked.connect(self.processUpload)
        self.buttonUp.setFixedSize(QtCore.QSize(100, 40))
        self.buttonUp.setStyleSheet(BUTTON_STYLE)

        self.label1 = QLabel("Please click on the upload button.")

        self.title = QLabel("Processing...", self)
        self.title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(self.title, 0, 0)
        self.gridLayout.addWidget(self.label1, 2, 0)
        self.gridLayout.addWidget(self.buttonUp, 2, 2)

    def processUpload(self):
        # Ne update pas
        self.buttonUp.setStyleSheet(BUTTON_DEACTIVED)
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
        doxyfileBuffer = []
        url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/' + useful.dicoLangDoxy[language] + '/Doxyfile'
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
            url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/' + useful.dicoLangDoxy[language] + '/' + fileName

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


class EndWindow(QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)

        title = QLabel("Upload was successful!", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(button, 1, 3)

    def switch(self):
        self.switch_window.emit()


class Controller:
    def __init__(self):
        pass

    def show_WelcomeWindow(self, param_arg):
        self.welcome = WelcomeWindow(param_arg)
        self.welcome.switch_window.connect(self.show_InputInfoWindow)
        self.welcome.show()

    def show_InputInfoWindow(self, param_arg):
        self.input = InputInfoWindow(param_arg)
        self.input.switch_window.connect(self.show_SummaryWindow)
        self.welcome.close()
        self.input.show()

    def show_SummaryWindow(self, param_arg, libname, liblang, libpath):
        self.summary = SummaryWindow(param_arg, libname, liblang, libpath)
        self.summary.switch_window.connect(self.show_ProcessingWindow)
        self.input.close()
        self.summary.show()

    def show_ProcessingWindow(self, param_arg, libname, liblang, libpath):
        self.process = ProcessingWindow(param_arg, libname, liblang, libpath)
        self.process.switch_window.connect(self.show_EndWindow)
        self.summary.close()
        self.process.show()

    def show_EndWindow(self):
        self.end = EndWindow()
        self.process.close()
        self.end.show()


def graphicalClient(program_args):
    # Create Qt application
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_WelcomeWindow(program_args)
    return app.exec_()
