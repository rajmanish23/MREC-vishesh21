import sqlite3
from sqlite3 import Error

washaDB = sqlite3.connect('washaDB/orders.db')
cur = washaDB.cursor()

def cleanType(types):
    try:
        typeString = ','.join(types)
        cur.execute("INSERT INTO orders(cleanType) VALUES(:cleantype)",
                    {'cleantype':typeString})
        washaDB.commit()
    except Error as e:
        print(f"error : {e}")

def ironYN(ironStatus):
    try:
        if ironStatus==True:
            cur.execute("INSERT INTO orders(ironYN) VALUES(:ironStatus)",
                {'ironStatus':"YES"})
            washaDB.commit()
        else:
            cur.execute("INSERT INTO orders(ironYN) VALUES(:ironStatus)",
                {'ironStatus':"NO"})
        pass
    except Error as e:
        print(f"error : {e}")

def orderWeight(weight):
    try:
        cur.execute("INSERT INTO orders(orderWeight) VALUES(:weight)",
                {'weight':weight})
        washaDB.commit()
    except Error as e:
        print(f"error : {e}")

def dressTypes(dressTypes):
    try:
        dressTypeString = ','.join(dressTypes)
        cur.execute("INSERT INTO orders(dressType) VALUES(:dresstype)",
                    {'dresstype':dressTypeString})
        washaDB.commit()
    except Error as e:
        print(f"error : {e}")

def slotTime(sltime):
    try:
        cur.execute("INSERT INTO orders(slotTime) VALUES(:slot)",
                {'slot':sltime})
        washaDB.commit()
    except Error as e:
        print(f"error : {e}")

def disconnect():
    washaDB.commit()
    washaDB.close()
