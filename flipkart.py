import requests
from bs4 import BeautifulSoup
import re

def flipp(k):
    d = []
    url = "http://www.flipkart.com/search?q=" + str(k) + "&as=off&as-show=on&otracker=start"
    ss = requests.get(url)
    src = ss.text
    obj = BeautifulSoup(src)
    for e in obj.findAll("a",class_=re.compile("-title")):
        title = e.text
        print title.strip()

h = raw_input("Enter a keyword:")
print flipp(h)
