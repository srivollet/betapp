#!/usr/bin/python2.7
import urllib2
from bs4 import BeautifulSoup

#specify the url
url_flashresultat = "'http://www.bloomberg.com/quote/SPX:IND'"

#page = urllib2.urlopen(url_flashresultat)

#soup = BeautifulSoup(page, 'html.parser')

#print(soup);
#print(soup.find_all('span', { 'class' : 'country_part' }))

#import webbrowser

#webbrowser.open('https://www.lequipe.fr/Football/ligue-1-resultats.html')

from selenium import webdriver
import re

#browser = webdriver.Chrome()
browser = webdriver.PhantomJS()

browser.get('http://www.flashresultats.fr/')

#On recupere le tableau des resultats
resultats = browser.find_element_by_class_name('table-main')

soup = BeautifulSoup(resultats.get_attribute('innerHTML'), 'html.parser')



for tag in soup.find_all("span", class_="tournament_part"):
    print(tag.text)

browser.close()