import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = 0
count = 0

tags = soup.find_all('span')

for tag in tags:
    num = int(tag.string)
    total = total + num
    count = count + 1

print(count)
print(total)
