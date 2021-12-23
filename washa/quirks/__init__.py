import sqlite3

# basically creates database files and tables within them if not present

washaDB = sqlite3.connect('washaDB/users.db')
# checking wether database is present or not. if not present, it creates table
with washaDB:
    washaDB.execute("""CREATE TABLE IF NOT EXISTS users(
                    userID integer,
                    email text,
                    password text,
                    phNumber integer,
                    userType text,
                    deliveryAddress text
                )""") #deliveryAddress and deliveryAddressCoords saves the already entered address for future orders
washaDB.close()

washaDB = sqlite3.connect('washaDB/orders.db')
with washaDB:
    washaDB.execute("""CREATE TABLE IF NOT EXISTS orders(
                    orderNum integer,
                    userID integer,
                    cleanType text,
                    ironYN text,
                    orderWeight integer,
                    dressType text,
                    slotTime text,
                    deliveryLocAddress text,
                    orderStatus text
                )""") # deliveryLocAddress saves delivery location as plain text
                      # deliveryLocAddressCoords saves location as coordinates for calculating distance
washaDB.close()

washaDB = sqlite3.connect('washaDB/laundryServices.db')
with washaDB:
    washaDB.execute("""CREATE TABLE IF NOT EXISTS serviceDetails(
                    serviceID integer,
                    serviceName text,
                    acceptedTypes text,
                    acceptedIron text,
                    maxLoad integer,
                    pricePerKG integer,
                    serviceLocAddress text
                )""") # serviceLocAddress saves laundry service location as text (to display that to end user)
                      # serviceLocAddressCoords saves the service location as coordinate for calculating distance
    washaDB.execute("""CREATE TABLE IF NOT EXISTS serviceUsers(
                    userID integer,
                    serviceID integer,
                    upiNum integer
                )""")
washaDB.close()

washaDB = sqlite3.connect('washaDB/deliveryUsers.db')
with washaDB:
    washaDB.execute("""CREATE TABLE IF NOT EXISTS deliveryUsers(
                    userID integer,
                    phNumber integer,
                    deliveryID integer
                )""")
washaDB.close()