from PyQt5 import QtCore, QtGui, QtWidgets
from quirks.mainApp import _checkAddressPresentProfile
import askAddressUpdate

class Ui_orderPlacedDialog(object):

    def checkAddress(self, orderPlacedDialog, ordersPage):
        if (_checkAddressPresentProfile.checkAddressPresent(self.userid) == False):
            self.askAddressUpdatePage = QtWidgets.QDialog()
            self.askAddressUpdateUi = askAddressUpdate.Ui_askAddressUpdate()
            self.askAddressUpdateUi.setupUi(self.askAddressUpdatePage)
            self.askAddressUpdatePage.show()
            self.askAddressUpdateUi.userid = self.userid
            self.askAddressUpdateUi.ordernum = self.ordernum
            orderPlacedDialog.close()
            ordersPage.close()
        else:
            orderPlacedDialog.close()
            ordersPage.close()

    # def openHome(self):
    #     self.homePage = QtWidgets.QMainWindow()
    #     self.homeui = homePage.Ui_homePage()
    #     self.homeui.setupUi(self.homePage)
    #     self.homePage.show()

    def setupUi(self, orderPlacedDialog, ordersPage):
        self.userid = 0
        self.ordernum = 0
        orderPlacedDialog.setObjectName("orderPlacedDialog")
        orderPlacedDialog.resize(410, 160)
        orderPlacedDialog.setMinimumSize(QtCore.QSize(410, 160))
        orderPlacedDialog.setMaximumSize(QtCore.QSize(410, 160))
        self.buttonBox = QtWidgets.QDialogButtonBox(orderPlacedDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(orderPlacedDialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.okButton = QtWidgets.QPushButton(orderPlacedDialog, clicked = lambda: self.checkAddress(orderPlacedDialog, ordersPage))
        self.okButton.setGeometry(QtCore.QRect(299, 82, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")

        self.retranslateUi(orderPlacedDialog)
        self.buttonBox.accepted.connect(orderPlacedDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(orderPlacedDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(orderPlacedDialog)

    def retranslateUi(self, orderPlacedDialog):
        _translate = QtCore.QCoreApplication.translate
        orderPlacedDialog.setWindowTitle(_translate("orderPlacedDialog", "Order Placed"))
        orderPlacedDialog.setWindowIcon(QtGui.QIcon("icon.png"))
        self.label.setText(_translate("orderPlacedDialog", "✅  ORDER PLACED"))
        self.okButton.setText(_translate("orderPlacedDialog", "NICE!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orderPlacedDialog = QtWidgets.QDialog()
    ui = Ui_orderPlacedDialog()
    ui.setupUi(orderPlacedDialog)
    orderPlacedDialog.show()
    sys.exit(app.exec_())
