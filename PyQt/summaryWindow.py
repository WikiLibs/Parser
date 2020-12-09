from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class SummaryWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(object, str, str, str, str)
    switch_window_prev = QtCore.pyqtSignal(object)

    def __init__(self, param_arg, libname, liblang, libpath, apiKey, width, height):
        QMainWindow.__init__(self)
        self.param_arg = param_arg
        self.libname = libname
        self.liblang = liblang
        self.libpath = libpath
        self.apiKey = apiKey
        self.winWidth = width
        self.winHeight = height
        self.setMinimumHeight(320)
        self.setupStyle()
        self.setupUi()

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
        """
        self.styleSheetRound = """
            QMainWindow{
                background-color: #FFFFFF
            }

            QLabel{
                color: #202020;
            }

            QPushButton {
                color: #7B68EE;
                border: 2px solid #7B68EE;
                border-radius: 20px;
                background: qradialgradient(
                cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
                radius: 1.35,
                );
                background-color: #FFFFFF;
                padding: 5px;
            }
        """
        self.styleSheetRoundFill = """
            QMainWindow{
                background-color: #FFFFFF
            }

            QLabel{
                color: #202020;
            }

            QPushButton {
                color: #FFFFFF;
                border: 2px solid #7B68EE;
                border-radius: 20px;
                background: qradialgradient(
                cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
                radius: 1.35,
                );
                background-color: #7B68EE;
                padding: 5px;
            }
        """
        self.setStyleSheet(self.stylesheet)

    def resizeEvent(self, event):
        self.line.setGeometry(QtCore.QRect(self.width() / 2 - 50, 100, 21, 20))
        self.line_3.setGeometry(QtCore.QRect(self.width() / 2 + 30, 100, 21, 20))
        self.pushButton_6.setGeometry(QtCore.QRect(self.width() / 2 - 100, 90, 41, 41))
        self.pushButton_3.setGeometry(QtCore.QRect(self.width() / 2 - 20, 90, 41, 41))
        self.pushButton_5.setGeometry(QtCore.QRect(self.width() / 2 + 60, 90, 41, 41))

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(self.winWidth, self.winHeight)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(165, 0))
        self.label_3.setMaximumSize(QtCore.QSize(165, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(160, 0))
        self.label_4.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.switch_prev)
        self.horizontalLayout_4.addWidget(self.pushButton2)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(160, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.switch)
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        #stepper
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(270, 100, 21, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 90, 41, 41))
        self.pushButton_3.setStyleSheet(self.styleSheetRoundFill)
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(350, 100, 21, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 90, 41, 41))
        self.pushButton_5.setStyleSheet(self.styleSheetRound)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 90, 41, 41))
        self.pushButton_6.setStyleSheet(self.styleSheetRound)
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WikiLibs Uploader"))
        self.label.setText(_translate("MainWindow", "Summary"))
        self.label_2.setText(_translate("MainWindow", "Selected language :"))
        self.label_5.setText(_translate("MainWindow", self.liblang))
        self.label_3.setText(_translate("MainWindow", "Selected library name :"))
        self.label_6.setText(_translate("MainWindow", self.libname))
        self.label_4.setText(_translate("MainWindow", "Selected library path :"))
        self.label_7.setText(_translate("MainWindow", self.libpath))
        self.pushButton.setText(_translate("MainWindow", "Process and Upload"))
        self.pushButton2.setText(_translate("MainWindow", "Prev"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "1"))

    def switch(self):
        self.switch_window.emit(self.param_arg, self.label_6.text(), self.label_5.text(), self.label_7.text(), self.apiKey)

    def switch_prev(self):
        self.switch_window_prev.emit(self.param_arg)
