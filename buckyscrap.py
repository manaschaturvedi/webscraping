import requests
from bs4 import BeautifulSoup

def trade(max_pages):
    page = 1
    while(page <= max_pages):
        url = "https://buckysroom.org/trade/search.php?page=" + str(page)
        u = requests.get(url)
        src = u.text
        obj = BeautifulSoup(src)
        for a in obj.findAll("a", {'class' : 'item-name'}):
            title = a.string
            print unicode(title)
        page += 1

trade(2)        
