from PyQt5 import QtCore, QtGui, QtWidgets
from quirks.mainApp import _washOptions, _checkAddressPresentProfile
import noDetailsError, orderPlaced

class Ui_orderWindow(object):

    def addressToTxtBox(self):
        # print(self.userID)
        userAddress = _checkAddressPresentProfile.sendAddressToTxtBox(self.userID)
        if userAddress != 0:
            self.addressTextBox.document().setPlainText(userAddress)
        

    def placeOrder(self, ordersPage):
        dressTypes = self.dressTypesTextBox.toPlainText()
        address = self.addressTextBox.toPlainText()
        weight = self.weightSpinBox.value()
        selectedWashTypes = self.getWashTypes()
        ironStatus = []
        slotTime = []
        ironStatus = self.getIronStatus()
        slotTime = self.getSlotTime()
        if (dressTypes == '' or address == '' or weight == 0 or selectedWashTypes == '' or ironStatus == [] or slotTime == []):
            self.detailsError = QtWidgets.QMainWindow()
            self.detailsErrorui = noDetailsError.Ui_loginFail()
            self.detailsErrorui.setupUi(self.detailsError)
            self.detailsError.show()
        else:
            # print(dressTypes)
            # print(address)
            # print(weight)
            # print(selectedWashTypes)
            # print(ironStatus[0])
            # print(slotTime[0])
            # print(self.userID)
            orderNum = _washOptions.optionsCommit(selectedWashTypes, self.userID, ironStatus[0], weight, dressTypes, slotTime[0], address)
            self.orderConfirmed = QtWidgets.QDialog()
            self.orderPlacedUi = orderPlaced.Ui_orderPlacedDialog()
            self.orderPlacedUi.setupUi(self.orderConfirmed, ordersPage)
            self.orderConfirmed.show()
            self.orderPlacedUi.userid = self.userID
            self.orderPlacedUi.ordernum = orderNum

    def checkedCT1(self,checked):
        if checked:
            self.WTypes['Dry Clean'] = 1
        else:
            self.WTypes['Dry Clean'] = 0
        self.getWashTypes()

    def checkedCT2(self,checked):
        if checked:
            self.WTypes['Wet Clean'] = 1
        else:
            self.WTypes['Wet Clean'] = 0
        self.getWashTypes()

    def getWashTypes(self):
        selectedWashTypes = '\n'.join([key for key in self.WTypes.keys()
                                                if self.WTypes[key] == 1])
        return selectedWashTypes

    def selectedIronY(self, selected):
        if selected:
            self.ironYN[True] = 1
        else:
            self.ironYN[True] = 0
        self.getIronStatus()
                                                               #nice
    def selectedIronN(self, selected):
        if selected:
            self.ironYN[False] = 1
        else:
            self.ironYN[False] = 0
        self.getIronStatus()
    
    def getIronStatus(self):
        ironStatus = [key for key in self.ironYN.keys()
                        if self.ironYN[key] == 1]
        return ironStatus

    def selectedSlotTime1(self, selected):
        if selected:
            self.slotTime["10AM - 12PM"] = 1
        else:
            self.slotTime["10AM - 12PM"] = 0
        self.getSlotTime()
    
    def selectedSlotTime2(self, selected):
        if selected:
            self.slotTime["12PM - 2PM"] = 1
        else:
            self.slotTime["12PM - 2PM"] = 0
        self.getSlotTime()
    
    def selectedSlotTime3(self, selected):
        if selected:
            self.slotTime["2PM - 4PM"] = 1
        else:
            self.slotTime["2PM - 4PM"] = 0
        self.getSlotTime()
    
    def selectedSlotTime4(self, selected):
        if selected:
            self.slotTime["4PM - 6PM"] = 1
        else:
            self.slotTime["4PM - 6PM"] = 0
        self.getSlotTime()
    
    def selectedSlotTime5(self, selected):
        if selected:
            self.slotTime["6PM - 8PM"] = 1
        else:
            self.slotTime["6PM - 8PM"] = 0
        self.getSlotTime()
    
    def getSlotTime(self):
        slotTime =[key for key in self.slotTime.keys()
                    if self.slotTime[key] == 1]
        return slotTime

    def setupUi(self, orderWindow):
        self.userID = 0
        self.WTypes = {'Dry Clean':0, 'Wet Clean':0}
        self.ironYN = {True:0,False:0}
        self.slotTime = {"10AM - 12PM":0,"12PM - 2PM":0,"2PM - 4PM":0,"4PM - 6PM":0,"6PM - 8PM":0}
        orderWindow.setObjectName("orderWindow")
        orderWindow.resize(750, 500)
        orderWindow.setMinimumSize(QtCore.QSize(750, 500))
        orderWindow.setMaximumSize(QtCore.QSize(750, 500))
        self.centralwidget = QtWidgets.QWidget(orderWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(750, 500))
        self.centralwidget.setMaximumSize(QtCore.QSize(750, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.cleanType1ChkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.cleanType1ChkBox.stateChanged.connect(self.checkedCT1)
        self.cleanType1ChkBox.setGeometry(QtCore.QRect(50, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cleanType1ChkBox.setFont(font)
        self.cleanType1ChkBox.setObjectName("cleanType1ChkBox")
        self.cleanType2ChkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.cleanType2ChkBox.stateChanged.connect(self.checkedCT2)
        self.cleanType2ChkBox.setGeometry(QtCore.QRect(50, 90, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cleanType2ChkBox.setFont(font)
        self.cleanType2ChkBox.setObjectName("cleanType2ChkBox")
        self.cleanTypesLabel = QtWidgets.QLabel(self.centralwidget)
        self.cleanTypesLabel.setGeometry(QtCore.QRect(30, 40, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cleanTypesLabel.setFont(font)
        self.cleanTypesLabel.setObjectName("cleanTypesLabel")
        self.ironYNLabel = QtWidgets.QLabel(self.centralwidget)
        self.ironYNLabel.setGeometry(QtCore.QRect(30, 140, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ironYNLabel.setFont(font)
        self.ironYNLabel.setObjectName("ironYNLabel")
        self.ironYesRBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.ironYesRBtn.toggled.connect(self.selectedIronY)
        self.ironYesRBtn.setGeometry(QtCore.QRect(50, 166, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ironYesRBtn.setFont(font)
        self.ironYesRBtn.setObjectName("ironYesRBtn")
        self.ironNoRBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.ironNoRBtn.toggled.connect(self.selectedIronN)
        self.ironNoRBtn.setGeometry(QtCore.QRect(50, 185, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ironNoRBtn.setFont(font)
        self.ironNoRBtn.setObjectName("ironNoRBtn")
        self.weightLabel = QtWidgets.QLabel(self.centralwidget)
        self.weightLabel.setGeometry(QtCore.QRect(30, 230, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weightLabel.setFont(font)
        self.weightLabel.setObjectName("weightLabel")
        self.weightSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.weightSpinBox.setGeometry(QtCore.QRect(50, 260, 61, 22))
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.dressTypesLabel = QtWidgets.QLabel(self.centralwidget)
        self.dressTypesLabel.setGeometry(QtCore.QRect(30, 310, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dressTypesLabel.setFont(font)
        self.dressTypesLabel.setObjectName("dressTypesLabel")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 20, 391, 201))
        self.widget.setObjectName("widget")
        self.slotTimeRbtn1 = QtWidgets.QRadioButton(self.widget)
        self.slotTimeRbtn1.toggled.connect(self.selectedSlotTime1)
        self.slotTimeRbtn1.setGeometry(QtCore.QRect(50, 50, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slotTimeRbtn1.setFont(font)
        self.slotTimeRbtn1.setObjectName("slotTimeRbtn1")
        self.slotTimeRbtn4 = QtWidgets.QRadioButton(self.widget)
        self.slotTimeRbtn4.toggled.connect(self.selectedSlotTime4)
        self.slotTimeRbtn4.setGeometry(QtCore.QRect(50, 140, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slotTimeRbtn4.setFont(font)
        self.slotTimeRbtn4.setObjectName("slotTimeRbtn4")
        self.slotTimeRbtn2 = QtWidgets.QRadioButton(self.widget)
        self.slotTimeRbtn2.toggled.connect(self.selectedSlotTime2)
        self.slotTimeRbtn2.setGeometry(QtCore.QRect(50, 80, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slotTimeRbtn2.setFont(font)
        self.slotTimeRbtn2.setObjectName("slotTimeRbtn2")
        self.slotTimeRbtn3 = QtWidgets.QRadioButton(self.widget)
        self.slotTimeRbtn3.toggled.connect(self.selectedSlotTime3)
        self.slotTimeRbtn3.setGeometry(QtCore.QRect(50, 110, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slotTimeRbtn3.setFont(font)
        self.slotTimeRbtn3.setObjectName("slotTimeRbtn3")
        self.slotTimeLabel = QtWidgets.QLabel(self.widget)
        self.slotTimeLabel.setGeometry(QtCore.QRect(20, 20, 361, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slotTimeLabel.setFont(font)
        self.slotTimeLabel.setObjectName("slotTimeLabel")
        self.slotTimeRbtn5 = QtWidgets.QRadioButton(self.widget)
        self.slotTimeRbtn5.toggled.connect(self.selectedSlotTime5)
        self.slotTimeRbtn5.setGeometry(QtCore.QRect(50, 170, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slotTimeRbtn5.setFont(font)
        self.slotTimeRbtn5.setObjectName("slotTimeRbtn5")
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        self.addressLabel.setGeometry(QtCore.QRect(350, 240, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.addressTextBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.addressTextBox.setGeometry(QtCore.QRect(370, 270, 281, 121))
        self.addressTextBox.setObjectName("addressTextBox")
        self.dressTypesTextBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.dressTypesTextBox.setGeometry(QtCore.QRect(50, 340, 141, 71))
        self.dressTypesTextBox.setObjectName("dressTypesTextBox")
        self.confirmOrder = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.placeOrder(orderWindow))
        self.confirmOrder.setGeometry(QtCore.QRect(530, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirmOrder.setFont(font)
        self.confirmOrder.setObjectName("confirmOrder")
        self.cancleOrder = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: orderWindow.close())
        self.cancleOrder.setGeometry(QtCore.QRect(630, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancleOrder.setFont(font)
        self.cancleOrder.setObjectName("cancleOrder")
        orderWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(orderWindow)
        QtCore.QMetaObject.connectSlotsByName(orderWindow)

    def retranslateUi(self, orderWindow):
        _translate = QtCore.QCoreApplication.translate
        orderWindow.setWindowTitle(_translate("orderWindow", "Order Details"))
        orderWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.cleanType1ChkBox.setText(_translate("orderWindow", "Dry Clean"))
        self.cleanType2ChkBox.setText(_translate("orderWindow", "Wet Clean"))
        self.cleanTypesLabel.setText(_translate("orderWindow", "TYPES OF CLEANING YOU WANT"))
        self.ironYNLabel.setText(_translate("orderWindow", "DO YOU WANT IRONING?"))
        self.ironYesRBtn.setText(_translate("orderWindow", "YES"))
        self.ironNoRBtn.setText(_translate("orderWindow", "NO"))
        self.weightLabel.setText(_translate("orderWindow", "NO. OF PAIRS IN THE ORDER"))
        self.dressTypesLabel.setText(_translate("orderWindow", "WHAT KIND OF DRESSES YOUR ORDDER HAS?"))
        self.slotTimeRbtn1.setText(_translate("orderWindow", "10AM - 12PM"))
        self.slotTimeRbtn4.setText(_translate("orderWindow", "4PM - 6PM"))
        self.slotTimeRbtn2.setText(_translate("orderWindow", "12PM - 2PM"))
        self.slotTimeRbtn3.setText(_translate("orderWindow", "2PM - 4PM"))
        self.slotTimeLabel.setText(_translate("orderWindow", "BY WHAT TIME SLOT YOU WANT YOUR ORDER TO BE WASHED?"))
        self.slotTimeRbtn5.setText(_translate("orderWindow", "6PM - 8PM"))
        self.addressLabel.setText(_translate("orderWindow", "ENTER YOUR ADDRESS"))
        self.confirmOrder.setText(_translate("orderWindow", "CONFIRM"))
        self.cancleOrder.setText(_translate("orderWindow", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orderWindow = QtWidgets.QMainWindow()
    ui = Ui_orderWindow()
    ui.setupUi(orderWindow)
    orderWindow.show()
    sys.exit(app.exec_())
