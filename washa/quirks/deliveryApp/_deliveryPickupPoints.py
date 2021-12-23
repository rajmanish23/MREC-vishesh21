import sqlite3

def sendPickupPoints(serviceID,orderNum):
    try:
        conn1 = sqlite3.connect('washaDB/laundryServices.db')
        conn2 = sqlite3.connect('washaDB/orders.db')
        cur1 = conn1.cursor()
        cur2 = conn2.cursor()
        cur1.execute("SELECT * FROM serviceDetails WHERE serviceID=:serviceID",{'serviceID':serviceID})
        cur2.execute("SELECT * FROM orders WHERE orderNun=:orderNum",{'orderNum':orderNum})
        list1 = cur1.fetchall()
        tup1 = list1[0]
        list2 = cur2.fetchall()
        tup2 = list2[0]
        addressService = tup1[6]
        addressOrder = tup2[7]
        conn1.close()
        conn2.close()
        addresses = [addressService,addressOrder]
        return addresses

    except:
        print("error occured")