import sqlite3
from sqlite3 import Error

# updates the address associated with their account.

def updateAddressUser(userID,orderNum):
    try:
        washaDB1 = sqlite3.connect('washaDB/users.db')
        cur1 = washaDB1.cursor()
        washaDB2 = sqlite3.connect('washaDB/orders.db')
        cur2 = washaDB2.cursor()
        # cur1.execute("SELECT * FROM users WHERE userID=:userID",
        #             {'userID':userID})
        # oldAddressList=cur1.fetchall()
        # oldAddressTuple=oldAddressList[0]
        cur2.execute("SELECT * FROM orders WHERE orderNum=:orderNum",
                    {'orderNum':orderNum})
        newAddressList=cur2.fetchall()
        newAddressTuple=newAddressList[0]
        with washaDB1:
            cur1.execute("UPDATE users SET deliveryAddress=:newAddress WHERE userID=:userID",
                    {'newAddress':newAddressTuple[7],'userID':userID})
        washaDB1.close()
        washaDB2.close()
    except Error as e:
        print(f"error occured\n{e}")

# debug shit here
# updateAddressUser(userID=877202111000001, orderNum=2021112300000008)