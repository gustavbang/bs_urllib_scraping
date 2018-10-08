import urllib.request
import time
from bs4 import BeautifulSoup

data = urllib.request.urlopen("https://www.reddit.com/r/food/").read()

soup = BeautifulSoup(data, "html.parser")

for link in soup.findAll("p", "title"):
    print(link)
    time.sleep(0.5)