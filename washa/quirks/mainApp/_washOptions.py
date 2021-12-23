import sqlite3
from sqlite3 import Error
from datetime import datetime

# adds all the order details entered by the user in orders.db database and essentially places an order.

def optionsCommit(cleanTypes, userID, ironStatus, weight, dressTypes, sltime, address):
    try:
        washaDB = sqlite3.connect('washaDB/orders.db')
        cur = washaDB.cursor()
        currentDate=datetime.now()
        cur.execute("SELECT * FROM orders")
        orderListCount=cur.fetchall()
        orderCount=len(orderListCount)+1
        orderNum=0
        orderNum=str(currentDate.year)+str(currentDate.month)+str(currentDate.day)+'{:08d}'.format(orderCount)
        if ironStatus==True:
            ironStat="YES"
        else:
            ironStat="NO"
        # cleanTypeStr='\n'.join(cleanTypes)
        # dressTypeStr='\n'.join(dressTypes)
        with washaDB:
            cur.execute("INSERT INTO orders VALUES(:orderNum,:userID,:cleantype,:ironStatus,:weight,:dresstype,:slot,:delAddress,:orderStatus)",{
                                                                        'orderNum':int(orderNum),
                                                                        'userID':userID,
                                                                        'cleantype':cleanTypes,
                                                                        'ironStatus':ironStat,
                                                                        'weight':weight,
                                                                        'dresstype':dressTypes,
                                                                        'slot':sltime,
                                                                        'delAddress':address,
                                                                        'orderStatus':'awaiting pickup'
                                                                    })
        washaDB.close()
        return orderNum
    except Error as e:
        print(f"an error has occured\n{e}")
