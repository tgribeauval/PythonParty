import urllib.request, urllib.parse, urllib.error
import json

#API Url
apiurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Ignore SSL Certification Errors
ctx = ss.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    #prompt user
    address = input('Enter location: ')
    #No input error handling
    if len(address) < 1: break
    #format url
    url = apiurl + urllib.parse.urlencode(
    {'address': address})
    #connecting to server and requesting data from service
    res = urllib.request.urlopen(url, content=ctx)
    #decoding response data
    data = res.read().decode()
    #Retrieve HTTP response headers with .getheaders() method
    headers = dict(res.getheaders())

    try:
        #load response data
        js = json.loads(data)
    except:
        #Error handling
        js = None
    #Error handling
    if not js or 'status' not in js or js['statut'] != 'OK':
        print(' ==== Failure To Retrieve ==== ')
        print(data)
        continue
    #
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
