import sqlite3
from sqlite3 import Error

def orderStatus(orderNum,status):

# sets the status of the order to whatever i end up giving in the main one.

    try:
        washaDB = sqlite3.connect('washaDB/orders.db')
        cur = washaDB.cursor()
        with washaDB:
            cur.execute("UPDATE orders SET orderStatus=:status WHERE orderNum=:orderNUm",
                            {'orderStatus':status.lower(),'orderNum':orderNum})
        washaDB.close()
        return True
    except:
        print("error occured")

def printOrder(orderNum):

# basically saves the order as a txt file for now.
# would be nice if this actually hooks up to an irl printer but eh who cares. it's just a prototype!
# also returns a string "processing" which means order is picked up at laundry and is being processed

    try:
        washaDB = sqlite3.connect('washaDB/orders.db')
        cur = washaDB.cursor()
        cur.execute("SELECT * FROM orders WHERE orderNum=:orderNum",
                    {'orderNum':orderNum})
        orderList = cur.fetchall()
        orderTuple = orderList[0]
        orderFile = open(f"orders/order-{orderNum}.txt",'w')
        cleanType = orderTuple[1]
        ironYN = orderTuple[2]
        orderWeight = str(orderTuple[3])
        dressTypes = orderTuple[4]
        slotTime = orderTuple[5]
        deliveryAddress = orderTuple[6]
        orderPrinted = f'''
====== Order number {orderNum} ======

Types of cleaning requested :
{cleanType}

Ironing requested : {ironYN}

Weight of the order : {orderWeight} KGS

Types of dresses to be washed :
{dressTypes}

Time to be delivered by : {slotTime}

Delivery Address :
{deliveryAddress}

==========================================='''
        orderFile.write(orderPrinted)
        orderFile.close
        return "processing"
    except Error as e:
        print(f"error occured : {e}")

# debug shit below
#!!!do not run the main file before commenting out the code below!!!

# printOrder(orderNum=2021112000000001)