import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')

l = list()

for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')

    for tag in tags[:18]:
        l.append(tag.get('href', None))

    url = l[17]
    l.clear()
    print(url)
