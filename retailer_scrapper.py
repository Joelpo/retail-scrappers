# Simple tool that allows to recover price on main retailers product website page.
# @Joelpo

# coding: utf-8

from bs4 import BeautifulSoup
import requests
import unicodedata

headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36' }

#DARTY: Returns product info in list [Product Name, Price]
def getDartyInfo(url):
    #request page
	page = requests.get(url, headers)

	#get that soup man
	soup = BeautifulSoup(page.content, 'html.parser')

	#get price based on class attribute
	price_box = soup.find('div', attrs={'class': 'product_price'})

	#get name based on span class attribute
	product_name_box = soup.find('span', attrs={'class': 'product_name'})

	return [product_name_box.get_text().strip(),trimPrice(price_box.get_text())]


#Amazon: Returns product info in list [Product Name, Price]
def getAmazonInfo(url):
    #request page
	page = requests.get(url, headers)

	#get that soup man
	soup = BeautifulSoup(page.content, 'html.parser')

	#get price based on class attribute
	price_box = soup.find('span', attrs={'id': 'priceblock_ourprice'})

	#get name based on span class attribute
	product_name_box = soup.find('span', attrs={'id': 'productTitle'})

	# print('Recuperation des info de chez Amazon: {} :{}'.format(price,title) )
	return [product_name_box.get_text(),trimPrice(price_box.get_text())]


# Cleans up the price string to contain only a number in french format.
def trimPrice(string):
	return string.replace(' ', '').replace('\n','').replace('EUR','').replace(unicodedata.lookup("EURO SIGN"),'').replace(',','.')
