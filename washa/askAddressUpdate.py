from PyQt5 import QtCore, QtGui, QtWidgets
from quirks.mainApp import _updateAddress
import addressUpdated

class Ui_askAddressUpdate(object):

    def updateAddressInProfile(self, askAddressUpdate):
        _updateAddress.updateAddressUser(self.userid, self.ordernum)
        self.addressUpdatedPage = QtWidgets.QDialog()
        self.addressUpdatedUi = addressUpdated.Ui_addressUpdatedDialog()
        self.addressUpdatedUi.setupUi(self.addressUpdatedPage)
        self.addressUpdatedPage.show()
        self.addressUpdatedUi.userId = self.userid
        askAddressUpdate.close()

    def setupUi(self, askAddressUpdate):
        self.userid = 0
        self.ordernum = 0
        askAddressUpdate.setObjectName("askAddressUpdate")
        askAddressUpdate.resize(410, 160)
        askAddressUpdate.setMinimumSize(QtCore.QSize(410, 160))
        askAddressUpdate.setMaximumSize(QtCore.QSize(410, 160))
        self.buttonBox = QtWidgets.QDialogButtonBox(askAddressUpdate)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.askAddressUpdateLabel = QtWidgets.QLabel(askAddressUpdate)
        self.askAddressUpdateLabel.setGeometry(QtCore.QRect(20, 25, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.askAddressUpdateLabel.setFont(font)
        self.askAddressUpdateLabel.setTextFormat(QtCore.Qt.PlainText)
        self.askAddressUpdateLabel.setObjectName("askAddressUpdateLabel")
        self.confirmAddressUpdateBtn = QtWidgets.QPushButton(askAddressUpdate, clicked = lambda: self.updateAddressInProfile(askAddressUpdate))
        self.confirmAddressUpdateBtn.setGeometry(QtCore.QRect(190, 95, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirmAddressUpdateBtn.setFont(font)
        self.confirmAddressUpdateBtn.setObjectName("confirmAddressUpdateBtn")
        self.negateAddressUpdateBtn = QtWidgets.QPushButton(askAddressUpdate, clicked = lambda: askAddressUpdate.close())
        self.negateAddressUpdateBtn.setGeometry(QtCore.QRect(300, 95, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.negateAddressUpdateBtn.setFont(font)
        self.negateAddressUpdateBtn.setObjectName("negateAddressUpdateBtn")
        self.askAddressUpdteLabel_2 = QtWidgets.QLabel(askAddressUpdate)
        self.askAddressUpdteLabel_2.setGeometry(QtCore.QRect(20, 53, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.askAddressUpdteLabel_2.setFont(font)
        self.askAddressUpdteLabel_2.setTextFormat(QtCore.Qt.PlainText)
        self.askAddressUpdteLabel_2.setObjectName("askAddressUpdteLabel_2")

        self.retranslateUi(askAddressUpdate)
        self.buttonBox.accepted.connect(askAddressUpdate.accept) # type: ignore
        self.buttonBox.rejected.connect(askAddressUpdate.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(askAddressUpdate)

    def retranslateUi(self, askAddressUpdate):
        _translate = QtCore.QCoreApplication.translate
        askAddressUpdate.setWindowTitle(_translate("askAddressUpdate", "Update Address?"))
        self.askAddressUpdateLabel.setText(_translate("askAddressUpdate", "WOULD YOU LIKE TO ADD THAT"))
        self.confirmAddressUpdateBtn.setText(_translate("askAddressUpdate", "YES"))
        self.negateAddressUpdateBtn.setText(_translate("askAddressUpdate", "NO"))
        self.askAddressUpdteLabel_2.setText(_translate("askAddressUpdate", "ADDRESS TO YOUR PROFILE?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    askAddressUpdate = QtWidgets.QDialog()
    ui = Ui_askAddressUpdate()
    ui.setupUi(askAddressUpdate)
    askAddressUpdate.show()
    sys.exit(app.exec_())
