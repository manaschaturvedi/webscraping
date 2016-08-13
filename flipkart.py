import requests
from bs4 import BeautifulSoup

def flipkart(s):
	url = 'http://www.flipkart.com/search?q=' + str(s) + '&as=off&as-show=off&otracker=start'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "lxml")
	for link in soup.findAll('a', {'class' : 'fk-display-block'}):
		print link.get('title')

keyword = raw_input("Enter a keyword: ")
flipkart(keyword)