import requests
from bs4 import BeautifulSoup

def flipp(k):
    url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + str(k)
    ss = requests.get(url)
    src = ss.text
    obj = BeautifulSoup(src)
    for e in obj.findAll("span", {'class' : 'lrg bold'}):
        title = e.string
        print unicode(title)

    for e in obj.findAll("span", {'class' : 'med reg'}):
        title = e.string
        print unicode(title)    

h = raw_input("Enter a keyword:")
print flipp(h)

    
