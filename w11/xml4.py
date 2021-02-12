import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')
xml = urllib.request.urlopen(url).read()

lst = list()

tree = ET.fromstring(xml)
comments = tree.findall('.//comment')

for item in comments:
    count = int(item.find('count').text)
    lst.append(count)

print(sum(lst))
