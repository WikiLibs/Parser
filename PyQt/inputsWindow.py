from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class InputsWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(object, str, str, str)

    def __init__(self, param_arg):
        QMainWindow.__init__(self)
        self.param_arg = param_arg
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
        self.setStyleSheet(self.stylesheet)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(724, 471)
        self.lib_path_txt = "Please choose a location"

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
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setMaximumSize(QtCore.QSize(120, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(475, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(475, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["C", "PYTHON3", "JAVA"])
        self.horizontalLayout.addWidget(self.comboBox, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(475, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(475, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(475, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(475, 16777215))
        self.lineEdit.setText(self.lib_path_txt)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.browseLibPathFolder)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.switch)
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WikiLibs Uploader"))
        self.label.setText(_translate("MainWindow", "Please input the following informations"))
        self.label_2.setText(_translate("MainWindow", "Language"))
        self.label_3.setText(_translate("MainWindow", "Library Name"))
        self.label_4.setText(_translate("MainWindow", "Library Location"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "Next"))

    def browseLibPathFolder(self):
        self.lib_path_txt = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit.setText(self.lib_path_txt)

    def switch(self):
        self.switch_window.emit(self.param_arg, self.lineEdit_2.text(), self.comboBox.currentText(), self.lib_path_txt)


""" class InputInfoWindow(QWidget):
    switch_window = QtCore.pyqtSignal(object, str, str, str)

    def __init__(self, param_arg):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.lib_path_txt = "Please choose a location"
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

        self.setStyleSheet(self.stylesheet)

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(100, 40))

        buttton2 = QPushButton('Browse', self)
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
        title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

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
 """
