import graphicalClient as gc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class EndWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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
        self.resize(gc.WIDTH, gc.HEIGHT)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Upload successful !"))
        self.label_2.setText(_translate("MainWindow", "Thank you for your patience"))
        self.pushButton.setText(_translate("MainWindow", "Close"))

    """def __init__(self):
        QMainWindow.__init__(self)

        self.resize(gc.WIDTH, gc.HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        self.stylesheet =
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
        self.setStyleSheet(self.stylesheet)

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        button.setFixedSize(QtCore.QSize(100, 40))

        title = QLabel("Upload was successful!", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)
        title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(button, 1, 3)"""

    """def switch(self):
        self.switch_window.emit()"""
