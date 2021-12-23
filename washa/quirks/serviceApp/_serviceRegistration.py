import sqlite3
from sqlite3 import Error
from datetime import datetime

# if user wants to register as a service. for those who actually have laundry shops or have facillities for that

def serviceCenterRegistration(serviceId,serviceName,acceptedTypes,ironYN,maxLoadHandled,pricePerKG,serviceAddress):
    try:
        washaDB = sqlite3.connect('washaDB/laundryServices.db')
        cur = washaDB.cursor()
        acceptedTypesStr='\n'.join(acceptedTypes)
        with washaDB:
            cur.execute("INSERT INTO serviceDetails VALUES(:serviceID,:serviceName,:acceptedTypes,:ironAccepted,:maxLoadHandled,:pricePerKG,:serviceAddress,:serviceAddressCoords)",{
                                        'serviceID':int(serviceId),
                                        'serviceName':serviceName,
                                        'acceptedTypes':acceptedTypesStr,
                                        'ironAccepted':ironYN,
                                        'maxLoadHandled':maxLoadHandled,
                                        'pricePerKG':pricePerKG,
                                        'serviceAddress':serviceAddress,
                                    })
        washaDB.close()
        return True
    except Error as e:
        print(f"error occured : {e}")

def serviceUserRegistration(userID,upiNum):
    try:
        washaDBService = sqlite3.connect('washaDB/laundryServices.db')
        washaDBusers = sqlite3.connect('washaDB/users.db')
        curService = washaDBService.cursor()
        curUser = washaDBusers.cursor()
        curService.execute("SELECT * FROM serviceUsers")
        serviceUserListCount = curService.fetchall()
        serviceUserCount = len(serviceUserListCount)+1
        currentDate = datetime.now()
        serviceID = 0
        serviceID = '737'+str(currentDate.year)+str(currentDate.month)+'{:06d}'.format(serviceUserCount)
        with washaDBService:
            curService.execute("INSERT INTO serviceUsers VALUES (:userID,:serviceID,:upiNum)",{
                                        'userID':userID,
                                        'serviceID':int(serviceID),
                                        'upiNum':upiNum
                                    })
        with washaDBusers:
            curUser.execute("UPDATE users SET userType=:usrType WHERE userID=:userID",
                                {'usrType':'SERVICE AGENT','userID':userID})
        washaDBService.close()
        washaDBusers.close()
        return serviceID
    except Error as e:
        print(f"error occured : {e}")

# debug shit below.
# !!!do not run main files before commenting out below code!!!

# userID = input("enter userID : ")
# upiNum = int(input("enter phine number associated with upi"))
# serviceID = None
# serviceID = serviceUserRegistration(userID,upiNum)
# if serviceID != None:
    # print("registered succenfully")
# else:
    # print("registration unsuccessful")
# serviceName = input("laundry shop name : ")
# acceptTypes = []
# acceptTypesNum = int(input("how many types are accepted for laundry : "))
# print("enter types :")
# for i in range(0,acceptTypesNum):
    # acceptTypes.append(input())
# ironYN = input("accept ironing? (yes/no) : ").upper()
# maxLoad = int(input("maximum load accepted per order : "))
# price = int(input("price per kg : "))
# address = input("address of shop : ")
# serviceCenterRegistration(serviceID,serviceName,acceptTypes,ironYN,maxLoad,price,address,serviceAddressCoords="0,0")