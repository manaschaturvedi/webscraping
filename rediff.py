import requests
from bs4 import BeautifulSoup

def flipp(k):
    url = "http://books.rediff.com/" + str(k) + "?sc_cid=books_inhomesrch"
    ss = requests.get(url)
    src = ss.text
    obj = BeautifulSoup(src)
    for e in obj.findAll("a", {'class' : 'bold'}):
        title = e.text
        print unicode(title)

    for e in obj.findAll("span", {'class' : 'med reg'}):
        title = e.get('title')
        print unicode(title)    

h = raw_input("Enter a keyword:")
print flipp(h)

    
