from PyQt5 import QtCore, QtGui, QtWidgets
# import startPage

class Ui_askLogoutDialog(object):

    # def openLogin(self, logoutDialog, homePage):
    #     self.loginwindow = QtWidgets.QMainWindow()
    #     self.loginUi = startPage.Ui_welcomePage()
    #     self.loginUi.setupUi(self.loginwindow)
    #     self.loginwindow.show()
    #     logoutDialog.close()
    #     homePage.close()

    def setupUi(self, askLogoutDialog):
        askLogoutDialog.setObjectName("askLogoutDialog")
        askLogoutDialog.resize(410, 160)
        askLogoutDialog.setMinimumSize(QtCore.QSize(410, 160))
        askLogoutDialog.setMaximumSize(QtCore.QSize(410, 160))
        self.buttonBox = QtWidgets.QDialogButtonBox(askLogoutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.askLogout = QtWidgets.QLabel(askLogoutDialog)
        self.askLogout.setGeometry(QtCore.QRect(20, 40, 370, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.askLogout.setFont(font)
        self.askLogout.setObjectName("askLogout")
        self.logoutNo = QtWidgets.QPushButton(askLogoutDialog, clicked = lambda: askLogoutDialog.close())
        self.logoutNo.setGeometry(QtCore.QRect(299, 82, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logoutNo.setFont(font)
        self.logoutNo.setObjectName("logoutNo")
        self.logoutYes = QtWidgets.QPushButton(askLogoutDialog, clicked = lambda: exit())
        # self.openLogin(askLogoutDialog, homePage))
        self.logoutYes.setGeometry(QtCore.QRect(195, 82, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logoutYes.setFont(font)
        self.logoutYes.setObjectName("logoutYes")

        self.retranslateUi(askLogoutDialog)
        self.buttonBox.accepted.connect(askLogoutDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(askLogoutDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(askLogoutDialog)

    def retranslateUi(self, askLogoutDialog):
        _translate = QtCore.QCoreApplication.translate
        askLogoutDialog.setWindowTitle(_translate("askLogoutDialog", "Logout?"))
        self.askLogout.setText(_translate("askLogoutDialog", "DO YOU WANT TO LOG OUT AND EXIT?"))
        self.logoutNo.setText(_translate("askLogoutDialog", "NO"))
        self.logoutYes.setText(_translate("askLogoutDialog", "YES"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askLogoutDialog = QtWidgets.QDialog()
    ui = Ui_askLogoutDialog()
    ui.setupUi(askLogoutDialog)
    askLogoutDialog.show()
    sys.exit(app.exec_())
