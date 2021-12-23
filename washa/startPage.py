from PyQt5 import QtCore, QtGui, QtWidgets
import loginPage,registerWindow


class Ui_welcomePage(object):

    def openLogin(self):
        self.loginwindow = QtWidgets.QMainWindow()
        self.loginUi = loginPage.Ui_loginPage()
        self.loginUi.setupUi(self.loginwindow, welcomePage)
        self.loginwindow.show()

    def openRegister(self):
        self.registerWindow = QtWidgets.QMainWindow()
        self.registerUi = registerWindow.Ui_registerPage()
        self.registerUi.setupUi(self.registerWindow, welcomePage)
        self.registerWindow.show()

    def setupUi(self, welcomePage):
        welcomePage.setObjectName("welcomePage")
        welcomePage.resize(362, 528)
        welcomePage.setMinimumSize(QtCore.QSize(362, 528))
        welcomePage.setMaximumSize(QtCore.QSize(362, 528))
        self.centralwidget = QtWidgets.QWidget(welcomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openLogin())
        self.loginButton.setGeometry(QtCore.QRect(50, 250, 271, 41))
        self.loginButton.setAutoDefault(False)
        self.loginButton.setDefault(False)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openRegister())
        self.registerButton.setGeometry(QtCore.QRect(50, 310, 271, 41))
        self.registerButton.setObjectName("registerButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 130, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(56)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        welcomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(welcomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        welcomePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(welcomePage)
        self.statusbar.setObjectName("statusbar")
        welcomePage.setStatusBar(self.statusbar)

        self.retranslateUi(welcomePage)
        QtCore.QMetaObject.connectSlotsByName(welcomePage)

    def retranslateUi(self, welcomePage):
        _translate = QtCore.QCoreApplication.translate
        welcomePage.setWindowTitle(_translate("welcomePage", "Welcome"))
        welcomePage.setWindowIcon(QtGui.QIcon("icon.png"))
        self.loginButton.setText(_translate("welcomePage", "LOGIN"))
        self.registerButton.setText(_translate("welcomePage", "REGISTER"))
        self.label.setText(_translate("welcomePage", "OLS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcomePage = QtWidgets.QMainWindow()
    ui = Ui_welcomePage()
    ui.setupUi(welcomePage)
    welcomePage.show()
    sys.exit(app.exec_())
