import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
counts = soup.find_all("count")

for count in counts:
    x = int(count.string)
    sum = sum + x

print(sum)
