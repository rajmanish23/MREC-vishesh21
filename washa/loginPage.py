from PyQt5 import QtCore, QtGui, QtWidgets
from quirks.mainApp import _login
import loginUnsuccess, homePage, noDetailsError


class Ui_loginPage(object):

    def clickedLogin(self, welcomePage, loginPage):
        email = self.emailEntry.text()
        password = self.passwordEntry.text()
        # print(email)
        # print(password)
        if email != '' and password != '':
            self.userId = _login.login(email,password)
            if self.userId == 0:
                # print("login unsuccessful")
                self.loginError = QtWidgets.QMainWindow()
                self.loginui = loginUnsuccess.Ui_loginFail()
                self.loginui.setupUi(self.loginError, loginPage, welcomePage)
                self.loginError.show()
            else:
                # print("login successful")
                self.homePage = QtWidgets.QMainWindow()
                self.homeui = homePage.Ui_homePage()
                self.homeui.setupUi(self.homePage)
                self.homePage.show()
                welcomePage.close()
                loginPage.close()
                self.homeui.userID = self.userId
                self.homeui.getEmail(self.userId)
        else:
            self.detailsError = QtWidgets.QMainWindow()
            self.detailsErrorui = noDetailsError.Ui_loginFail()
            self.detailsErrorui.setupUi(self.detailsError)
            self.detailsError.show()

    def setupUi(self, loginPage, welcomePage):
        loginPage.setObjectName("loginPage")
        loginPage.resize(503, 349)
        loginPage.setMinimumSize(QtCore.QSize(503, 349))
        loginPage.setMaximumSize(QtCore.QSize(503, 349))
        self.centralwidget = QtWidgets.QWidget(loginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.emailText = QtWidgets.QLabel(self.centralwidget)
        self.emailText.setGeometry(QtCore.QRect(40, 53, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.emailText.setFont(font)
        self.emailText.setObjectName("emailText")
        self.passwordText = QtWidgets.QLabel(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(40, 140, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.passwordText.setFont(font)
        self.passwordText.setObjectName("passwordText")
        self.emailEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.emailEntry.setGeometry(QtCore.QRect(50, 93, 390, 21))
        self.emailEntry.setClearButtonEnabled(True)
        self.emailEntry.setObjectName("emailEntry")
        self.passwordEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setGeometry(QtCore.QRect(50, 178, 390, 20))
        self.passwordEntry.setClearButtonEnabled(True)
        self.passwordEntry.setObjectName("passwordEntry")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clickedLogin(welcomePage, loginPage))
        self.loginButton.setGeometry(QtCore.QRect(260, 242, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.cancleButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: loginPage.close())
        self.cancleButton.setGeometry(QtCore.QRect(370, 242, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancleButton.setFont(font)
        self.cancleButton.setObjectName("cancleButton")
        loginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)


    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "Login"))
        loginPage.setWindowIcon(QtGui.QIcon("icon.png"))
        self.emailText.setText(_translate("loginPage", "EMAIL"))
        self.passwordText.setText(_translate("loginPage", "PASSWORD"))
        self.loginButton.setText(_translate("loginPage", "LOGIN"))
        self.cancleButton.setText(_translate("loginPage", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginPage = QtWidgets.QMainWindow()
    ui = Ui_loginPage()
    ui.setupUi(loginPage)
    loginPage.show()
    sys.exit(app.exec_())
