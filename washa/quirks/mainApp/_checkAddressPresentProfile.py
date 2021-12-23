import sqlite3
from sqlite3 import Error

# VVV checks if address is already present in database VVV

def checkAddressPresent(userID):
    try:
        washaDB = sqlite3.connect('washaDB/users.db')
        cur = washaDB.cursor()
        cur.execute("SELECT * FROM users WHERE userID=:userID",
                    {'userID':userID})
        leList = cur.fetchall()
        leTuple = leList[0]
        if (leTuple[5] == None):
            washaDB.close()
            return False # an address is not present in database
        else:
            washaDB.close()
            return True # an address is present in database
    except Error as e:
        print(f"error occured : {e}")

# VVV sends the addresss present in database hopefully to address text entry box
#     if i manage to work that out... VVV

def sendAddressToTxtBox(userID):
    try:
        washaDB = sqlite3.connect('washaDB/users.db')
        cur = washaDB.cursor()
        cur.execute("SELECT * FROM users WHERE userID=:userID",
                    {'userID':userID})
        leList = cur.fetchall()
        leTuple = leList[0]
        address = ''
        address = leTuple[5]
        if address == None:
            return 0
        else:
            washaDB.close()
            return address
    except Error as e:
        print(f"error occured : {e}")

# debug shit down here.
# !!!do not forgot to comment them out before executing main file!!!

# userID = input('enter userID : ')
# print(sendAddressToTxtBox(userID=877202111000001))