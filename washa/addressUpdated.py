from PyQt5 import QtCore, QtGui, QtWidgets
import homePage

class Ui_addressUpdatedDialog(object):

    def openHome(self, addressUpdatedDialog):
        addressUpdatedDialog.close()

    def setupUi(self, addressUpdatedDialog):
        self.userId = 0
        addressUpdatedDialog.setObjectName("addressUpdatedDialog")
        addressUpdatedDialog.resize(410, 160)
        addressUpdatedDialog.setMinimumSize(QtCore.QSize(410, 160))
        addressUpdatedDialog.setMaximumSize(QtCore.QSize(410, 160))
        self.buttonBox = QtWidgets.QDialogButtonBox(addressUpdatedDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.addressUpdatedLable = QtWidgets.QLabel(addressUpdatedDialog)
        self.addressUpdatedLable.setGeometry(QtCore.QRect(20, 40, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addressUpdatedLable.setFont(font)
        self.addressUpdatedLable.setObjectName("addressUpdatedLable")
        self.okButton = QtWidgets.QPushButton(addressUpdatedDialog, clicked = lambda: self.openHome(addressUpdatedDialog))
        self.okButton.setGeometry(QtCore.QRect(299, 82, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")

        self.retranslateUi(addressUpdatedDialog)
        self.buttonBox.accepted.connect(addressUpdatedDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(addressUpdatedDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(addressUpdatedDialog)

    def retranslateUi(self, addressUpdatedDialog):
        _translate = QtCore.QCoreApplication.translate
        addressUpdatedDialog.setWindowTitle(_translate("addressUpdatedDialog", "Address Updated"))
        self.addressUpdatedLable.setText(_translate("addressUpdatedDialog", "✅  ADDRESS UPDATED"))
        self.okButton.setText(_translate("addressUpdatedDialog", "GREAT!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addressUpdatedDialog = QtWidgets.QDialog()
    ui = Ui_addressUpdatedDialog()
    ui.setupUi(addressUpdatedDialog)
    addressUpdatedDialog.show()
    sys.exit(app.exec_())
