from quirks.mainApp import _login, _register, _washOptions, _updateAddress, _checkAddressPresentProfile

email=input("email : ")
password=input("password : ")
loginStatus=_login.login(email,password)
if loginStatus == True:
    print("login success")
else:
    print("login unsuccess. please register")
    phNumber=int(input("phone number : "))
    address = input("enter your address : ")
    regiterStatus = _register.registration(email,password,phNumber,address)
    if regiterStatus == True:
        print("registration successful")
    else:
        print("registration unsuccesfull... please try again...")
        exit()

cleanTypes=[]
washTypesNum = int(input("enter no. of wash types"))
for i in range(0,washTypesNum):
    cleanTypes.append(input())

ironStatus=(input("do you want ironing? (Y/N) : ")).upper()
if ironStatus=='Y':
    ironSendStatus=True
else:
    ironSendStatus=False

weight=int(input("weight of load? : "))

dressTypes=[]
dressTypesNum=int(input("how many types? : "))
print("enter cloth types")
for i in range(0,dressTypesNum):
    dressTypes.append(input())

def slotswitch(option):
    slotSwitch={
        1:"10AM-12AM",
        2:"12AM-2PM",
        3:"2PM-4PM",
        4:"4PM-6PM",
        5:"6PM-8PM"
    }
    return slotSwitch.get(option)
print("""enter slot time
1:10AM-12AM
2:12AM-2PM
3:2PM-4PM
4:4PM-6PM
5:6PM-8PM""")
while True:
    opt=int(input())
    if (opt<=5 and opt>0):
       sltime=slotswitch(opt)
       break
    else:
        print("invalid option")

address=input("enter address")
orderNum=_washOptions.optionsCommit(cleanTypes,ironSendStatus,weight,dressTypes,sltime,address,addressCoords="0,0")
print("order placed!")
addPresent = _checkAddressPresentProfile.checkAddressPresent(email)
if addPresent == False:
    updateAddress=input("would you like to save this address for future use?(Y/N)(p1)").upper()
    if updateAddress=='Y':
        updateAddStatus = _updateAddress.updateAddressUser(email,orderNum)
        if updateAddStatus == True:
            print("address updated successfully")
    else:
        print("we would reccomend to save an address later for your convience")
else:
    updateAddress=input("would you like to save this address for future use?(Y/N)(p2)").upper()
    if updateAddress=='Y':
        updateAddStatus = _updateAddress.updateAddressUser(email,orderNum)
        if updateAddStatus == True:
            print("address updated successfully")
        else:
            print("address is already saved")
