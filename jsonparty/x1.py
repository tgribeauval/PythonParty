import urllib.request, urllib.parse, urllib.error
import json

url = input('Url:')
sum = 0


#Error handling
if len(url) < 1: exit()
#requet response
res = urllib.request.urlopen(url)
#decode response
data = res.read().decode()
#Retrieve HTTP response headers with .getheaders() method
headers = dict(res.getheaders())

try:
    js = json.loads(data)
except:
    js = None

for count in js["comments"]:
    num = int(count["count"])
    sum = sum + num

print(sum)
