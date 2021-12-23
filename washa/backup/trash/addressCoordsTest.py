from quirks.mainApp import _addressCoordsStuff
import sqlite3

# fetching coords for order location
conn1 = sqlite3.connect('washaDB/orders.db')
cur1 = conn1.cursor()
cur1.execute("SELECT * FROM orders WHERE orderNum = :orderNum",
                    {'orderNum':2021112000000001})
fetchedList = cur1.fetchall()
fetchedTup = fetchedList[0]
fetchedAddress = fetchedTup[6]
# coords = 
_addressCoordsStuff.addressCoord(fetchedAddress)
# print(coords)