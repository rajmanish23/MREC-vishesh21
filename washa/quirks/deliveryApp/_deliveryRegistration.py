import sqlite3
from sqlite3 import Error
from datetime import datetime

# if user wants to register as a delivery agent.

def deliveryUserRegistration(userID):
    try:
        washaDBdelivery = sqlite3.connect('washaDB/deliveryUsers.db')
        washaDBusers = sqlite3.connect('washaDB/users.db')
        curUsers = washaDBusers.cursor()
        curDelivery = washaDBdelivery.cursor()
        # generating delivery agent ID
        curDelivery.execute("SELECT * FROM deliveryUsers")
        deliveryUserListCount = curDelivery.fetchall()
        deliveryUserCount = len(deliveryUserListCount)+1
        currentDate = datetime.now()
        deliveryID = 0
        deliveryID = '335'+str(currentDate.year)+str(currentDate.month)+'{:06d}'.format(deliveryUserCount)
        # fetching email and phone number from users database
        curUsers.execute("SELECT * FROM users WHERE userID=:userID",{'userID':userID})
        userList = curUsers.fetchall()
        userTup = userList[0]
        email = userTup[1]
        phNum = userTup[3]
        # entering details into database
        with washaDBdelivery:
            curDelivery.execute("INSERT INTO deliveryUsers VALUES (:email,:phNumber,:deliveryId)",{
                                        'email':email,
                                        'phNumber':phNum,
                                        'deliveryId':deliveryID
                                    })
        with washaDBusers:
            curUsers.execute("UPDATE users SET userType=:usrType WHERE email=:email",
                                {'usrType':'DELIVEERY AGENT','email':email})
        washaDBdelivery.close()
        washaDBusers.close()
        return True
    except Error as e:
        print(f"error occured : {e}")

# debug shit below...
#!!!comment it out before running the main file!!!

# deliveryUserRegistration(input("enter email : "))