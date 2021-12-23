import sqlite3
from sqlite3.dbapi2 import Error

# to get email and password from user and verify if they are in the database which confirms that they are an active user.

def login(email,password):
    try:
        washaDB = sqlite3.connect('washaDB/users.db')
        cur = washaDB.cursor()
        cur.execute("SELECT * FROM users WHERE email=:email AND password=:password",
                    {'email':email,'password':password})
        userList = cur.fetchall()
        if userList == []:
            washaDB.close()
            return 0
        else:
            # print(userList)
            userTup = userList[0]
            userID = userTup[0]
            washaDB.close()
            return userID

    except Error as e:
        print(f"error : {e}")

# login(email="rajmanish@gmail.com",password="washa123")
# email = input()
# password = input()
# if login(email,password) == 0:
#     print("error")