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
from selenium.webdriver.support.ui import WebDriverWait
import re
import time

#browser = webdriver.Chrome()
browser = webdriver.PhantomJS()

browser.get('http://www.flashresultats.fr/')

#On va sur la page des cotes
resultats = browser.find_element_by_css_selector('.ifmenu-odds.li4').click()

print("before")
time.sleep(10)
print("after")

#On recupere le tableau des resultats
resultats = browser.find_element_by_class_name('odds-content')

soup = BeautifulSoup(resultats.get_attribute('innerHTML'), 'html.parser')

for soccer in soup.find_all("table", class_="soccer odds"):
    #On extrait la competition
    print soccer.find("span", class_="tournament_part").text

    #On extrait chaque match
    for match in soccer.find('tbody').find_all('tr'):
        print("\t" + match.text)
    
browser.quit()