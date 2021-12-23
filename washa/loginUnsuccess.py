from PyQt5 import QtCore, QtGui, QtWidgets
import registerWindow

class Ui_loginFail(object):

    def openRegAndCloseLogin(self, loginPage, welcomePage, loginFail):
        self.registerWindow = QtWidgets.QMainWindow()
        self.registerUi = registerWindow.Ui_registerPage()
        self.registerUi.setupUi(self.registerWindow, welcomePage)
        self.registerWindow.show()
        loginPage.close()
        loginFail.close()

    def setupUi(self, loginFail, loginPage, welcomePage):
        loginFail.setObjectName("loginFail")
        loginFail.resize(410, 160)
        loginFail.setMinimumSize(QtCore.QSize(410, 160))
        loginFail.setMaximumSize(QtCore.QSize(410, 160))
        self.centralwidget = QtWidgets.QWidget(loginFail)
        self.centralwidget.setObjectName("centralwidget")
        self.dialogText = QtWidgets.QLabel(self.centralwidget)
        self.dialogText.setGeometry(QtCore.QRect(20, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dialogText.setFont(font)
        self.dialogText.setObjectName("dialogText")
        self.okButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: loginFail.close())
        self.okButton.setGeometry(QtCore.QRect(190, 84, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.askRegButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openRegAndCloseLogin(loginPage, welcomePage, loginFail))
        self.askRegButton.setGeometry(QtCore.QRect(300, 84, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.askRegButton.setFont(font)
        self.askRegButton.setObjectName("askRegButton")
        loginFail.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginFail)
        QtCore.QMetaObject.connectSlotsByName(loginFail)

    def retranslateUi(self, loginFail):
        _translate = QtCore.QCoreApplication.translate
        loginFail.setWindowTitle(_translate("loginFail", "Login Unsuccessful"))
        loginFail.setWindowIcon(QtGui.QIcon("icon.png"))
        self.dialogText.setText(_translate("loginFail", "❌  LOGIN UNSUCCESFULL "))
        self.okButton.setText(_translate("loginFail", "OK"))
        self.askRegButton.setText(_translate("loginFail", "REGISTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginFail = QtWidgets.QMainWindow()
    ui = Ui_loginFail()
    ui.setupUi(loginFail)
    loginFail.show()
    sys.exit(app.exec_())
