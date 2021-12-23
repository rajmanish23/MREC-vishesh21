from geopy.geocoders import GoogleV3
from geopy.distance import geodesic

# using GeoPy to fetch the rough coordinates of the entered address.
def addressCoord(address):
    geolocater = GoogleV3(user_agent="request")
    location = geolocater.geocode(address)
    print(location.latitude,location.longitude)
    # coords = str(location.latitude)+','+str(location.longitude)
    # return coords

# calculating distance between two coordinates
def distanceCalc(coords1,coords2):
    try:
        coords1Tup = eval(coords1)
        coords2Tup = eval(coords2)
        return geodesic(coords1Tup,coords2Tup).km
    except:
        print("error occured")

# takes a dictonary of diatances and checkes the nearest i.e. least distance in them
def checkNearest(coordsDict):
    try:
        coordsDictSorted=dict(sorted(coordsDict.items(),key= lambda x:x[1]))
        return next(iter(coordsDictSorted)) # returns the nearest service shop id i guess...
    except:
        print("error occured")