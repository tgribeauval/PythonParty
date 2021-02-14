import urllib.request, urllib.parse, urllib.error
import json
import ssl

#API Url
apiurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

#Ignore SSL Certification Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #prompt user
    address = input('Enter location: ')
    #No input error handling
    if len(address) < 1: exit()
    #format url
    url = apiurl + urllib.parse.urlencode(
    {
    'key': api_key,
    'address': address
    })
    #connecting to server and requesting data from service
    res = urllib.request.urlopen(url, context=ctx)
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
    if not js or 'status' not in js or js['status'] != 'OK':
        print(' ==== Failure To Retrieve ==== ')
        print(data)
        continue
    #print(json.dumps(js, indent=4))
    print(js["results"][0]["place_id"])

    exit()
