from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from sesam import PasswordGenerator


class Ui_MainWindow(object):
    def __init__(self):
        self.passwordLength = 25
        self.masterpassword = ""
        self.domain = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 220)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 161, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pic = QtWidgets.QLabel(MainWindow)
        self.pic.setGeometry(250, 50, 220, 100)
        self.pic.setPixmap(QtGui.QPixmap("shield.ico").scaledToWidth(64).scaledToHeight(64))
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.Masterpassword_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Masterpassword_label.setObjectName("Masterpassword_label")
        self.gridLayout.addWidget(self.Masterpassword_label, 0, 0, 1, 1)
        self.Domain_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Domain_input.setObjectName("Domain_input")
        self.gridLayout.addWidget(self.Domain_input, 3, 0, 1, 1)
        self.Master_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Master_input.setObjectName("Master_input")
        self.Master_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.Master_input, 1, 0, 1, 1)
        self.Domain_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Domain_label.setObjectName("Domain_label")
        self.gridLayout.addWidget(self.Domain_label, 2, 0, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton.clicked.connect(self.handleButton)
        self.Master_input.returnPressed.connect(self.handleMasterInput)
        self.Domain_input.returnPressed.connect(self.handleDomainInput)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "sesam"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton
        self.Masterpassword_label.setText(_translate("MainWindow", "Masterpassword"))
        self.Domain_label.setText(_translate("MainWindow", "Domain"))

    def handleMasterInput(self):
        self.masterpassword = self.Master_input.text()

    def handleDomainInput(self):
        self.domain = self.Domain_input.text()

    def handleButton(self):
        self.domain = self.Domain_input.text()
        self.masterpassword = self.Master_input.text()
        password = PasswordGenerator().get_password(self.domain, self.masterpassword, self.passwordLength)
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(password)
        r.update()  # now it stays on the clipboard after the window is closed
        r.destroy()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(open("darkorange.css").read())
    sys.exit(app.exec_())
