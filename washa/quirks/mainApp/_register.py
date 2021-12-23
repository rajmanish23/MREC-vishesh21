import sqlite3
from sqlite3 import Error
from datetime import datetime

# if the user wants to make a new account or if login fails, this enters their details in the database.

def registration(email, password, phNumber):
    try:
        washaDB = sqlite3.connect('washaDB/users.db')
        cur = washaDB.cursor()
        # generating user ID
        cur.execute("SELECT * FROM users")
        userList = cur.fetchall()
        userCount = len(userList)+1
        currentDate = datetime.now()
        userID = 0
        userID = '877'+str(currentDate.year)+str(currentDate.month)+'{:06d}'.format(userCount)
        # entering user details within the database
        with washaDB:
            cur.execute("INSERT INTO users VALUES(:userid,:email,:password,:phNumber,:usertype,:deliveryAddress)",{
                            'userid':int(userID),
                            'email':email,
                            'password':password,
                            'phNumber':phNumber,
                            'usertype':"NORMAL",
                            'deliveryAddress':None,
                        })
        washaDB.close()
        return userID
    except Error as e:
        print(f"error has occured!\n{e}")

# debug shit down here
# email = input("enter email : ")
# password = input("enter password : ")
# phNumber = int(input("enter number : "))
# address = input("enter address : ")
# registration(email,password,phNumber,address)