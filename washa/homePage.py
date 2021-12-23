from PyQt5 import QtCore, QtGui, QtWidgets
import orderPage, askLogout
import sqlite3

class Ui_homePage(object):

    def askLogout(self):
        self.askLogoutDialog = QtWidgets.QDialog()
        self.askLogoutUi = askLogout.Ui_askLogoutDialog()
        self.askLogoutUi.setupUi(self.askLogoutDialog)
        self.askLogoutDialog.show()

    def getEmail(self,userid):
        _translate = QtCore.QCoreApplication.translate
        connDB = sqlite3.connect('washaDB/users.db')
        curDB = connDB.cursor()
        curDB.execute("SELECT * FROM users WHERE userID=:userID",
                    {'userID':userid})
        DBList = curDB.fetchall()
        DBTup = DBList[0]
        self.email = DBTup[1]
        self.profileButton.setText(_translate("homePage", self.email))

    def openOrders(self):
        self.orderWindow = QtWidgets.QMainWindow()
        self.orderUi = orderPage.Ui_orderWindow()
        self.orderUi.setupUi(self.orderWindow)
        self.orderWindow.show()
        self.orderUi.userID = self.userID
        self.orderUi.addressToTxtBox()

    def setupUi(self, homePage):
        self.userID = 0
        self.email = ''
        homePage.setObjectName("homePage")
        homePage.resize(362, 528)
        homePage.setMinimumSize(QtCore.QSize(362, 528))
        homePage.setMaximumSize(QtCore.QSize(362, 528))
        self.centralwidget = QtWidgets.QWidget(homePage)
        self.centralwidget.setObjectName("centralwidget")
        self.newOrderButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openOrders())
        self.newOrderButton.setGeometry(QtCore.QRect(50, 250, 271, 41))
        self.newOrderButton.setAutoDefault(False)
        self.newOrderButton.setDefault(False)
        self.newOrderButton.setFlat(False)
        self.newOrderButton.setObjectName("newOrderButton")
        self.showOrdersButton = QtWidgets.QPushButton(self.centralwidget)
        self.showOrdersButton.setGeometry(QtCore.QRect(50, 310, 271, 41))
        self.showOrdersButton.setObjectName("showOrdersButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 130, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(56)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.profileButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.profileButton.setGeometry(QtCore.QRect(10, 450, 228, 41))
        self.profileButton.setObjectName("profileButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.askLogout())
        self.pushButton.setGeometry(QtCore.QRect(236, 450, 111, 41))
        self.pushButton.setObjectName("pushButton")
        homePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        homePage.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(homePage)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(homePage)
        QtCore.QMetaObject.connectSlotsByName(homePage)

    def retranslateUi(self, homePage):
        _translate = QtCore.QCoreApplication.translate
        homePage.setWindowTitle(_translate("homePage", "Home Page"))
        homePage.setWindowIcon(QtGui.QIcon("icon.png"))
        self.newOrderButton.setText(_translate("homePage", "NEW ORDER"))
        self.showOrdersButton.setText(_translate("homePage", "SHOW ORDERS"))
        self.label.setText(_translate("homePage", "OLS"))
        self.profileButton.setText(_translate("homePage", "example@email.com"))
        self.pushButton.setText(_translate("homePage", "LOGOUT"))
        self.menuAbout.setTitle(_translate("homePage", "Info"))
        self.actionAbout.setText(_translate("homePage", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homePage = QtWidgets.QMainWindow()
    ui = Ui_homePage()
    ui.setupUi(homePage)
    homePage.show()
    sys.exit(app.exec_())
