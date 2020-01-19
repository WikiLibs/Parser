import useful
import Lang_C_CPP.parserC as parserC
import Lang_Python.parserPython as parserPython
import Lang_Java.parserJava as parserJava

from urllib.request import urlopen
import os
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


def getFunctionsLang():
    dispatch = {
        'C': parserC.parserC,
        'PYTHON3': parserPython.parserPython,
        'JAVA': parserJava.parserJava
    }
    return dispatch


class ProcessingWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal()

    # def __init__(self, param_arg, libname, liblang, libpath):
    #     QMainWindow.__init__(self)
    #     self.param_arg = param_arg
    #     self.libname = libname
    #     self.liblang = liblang
    #     self.libpath = libpath
    #     self.setupStyle()
    #     self.setupUi()
    #     # self.processUpload()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupStyle()
        self.setupUi()

    def setParamArg(self, paramArg):
        self.param_arg = paramArg

    def setLibName(self, libname):
        self.libname = libname

    def setLibLang(self, liblang):
        self.liblang = liblang

    def setLibPath(self, libpath):
        self.libpath = libpath

    def setupStyle(self):
        self.stylesheet = """
            QMainWindow{
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

            QPushButton:disabled{
                background-color: #757575;
            }
        """
        self.setStyleSheet(self.stylesheet)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(705, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.switch)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WikiLibs Uploader"))
        self.label.setText(_translate("MainWindow", "Processing and uploading"))
        self.label_2.setText(_translate("MainWindow", "Status :"))
        self.label_3.setText(_translate("MainWindow", "starting"))
        self.pushButton.setText(_translate("MainWindow", "Finish"))

    """def __init__(self, param_arg, libname, liblang, libpath):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.libname = libname
        self.liblang = liblang
        self.libpath = libpath
        self.resize(gc.WIDTH, gc.HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        self.stylesheet =
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
        self.gridLayout.addWidget(self.buttonUp, 2, 2)"""

    def processUpload(self):
        # Process Everything to Parse
        self.runDoxyfile(self.liblang)
        files = useful.getAllFiles(self.liblang)
        dispatch = getFunctionsLang()
        self.progressBar.setProperty("value", 20)

        i = 1

        for filename in files:
            self.label_3.setText("parsing files... (" + str(i) + "/" + str(len(files)) + ")")
            useful.logInfo('Starting parsing \'' + filename.ogFilename + '\'')
            obj = dispatch[self.liblang](self.liblang, self.libname)
            obj.parseXMLFile(filename.xmlFilename)
            self.update()
            i += 1

        self.progressBar.setProperty("value", 70)
        self.label_3.setText("sending data to the server")
        useful.callOptimizer()

        self.progressBar.setProperty("value", 90)
        self.label_3.setText("deleting temporary files")
        useful.deleteFiles()

        self.progressBar.setProperty("value", 100)
        self.label_3.setText("finished !")
        self.pushButton.setEnabled(True)

    def runDoxyfile(self, language):
        base_url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/'
        doxyfileBuffer = []
        url = base_url + useful.dicoLangDoxy[language] + '/Doxyfile'

        if language == "PYTHON3" and os.name == 'nt':
            url += 'Windows'

        self.label_3.setText("retrieving Doxyfile")
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
        self.progressBar.setProperty("value", 10)
        self.label_3.setText("excuting Doxygen")
        if os.name == 'nt':
            os.system('doxygen Doxyfile')
        else:
            os.system('doxygen Doxyfile > /dev/null')

    def switch(self):
        self.switch_window.emit()
