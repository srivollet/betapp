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
browser = webdriver.Chrome()

browser.get('http://www.flashresultats.fr/')

#On va sur la page des cotes
resultats = browser.find_element_by_css_selector('.ifmenu-odds.li4').click()

time.sleep(3)

#On recupere le tableau des resultats
resultats = browser.find_element_by_class_name('odds-content')

soup = BeautifulSoup(resultats.get_attribute('innerHTML'), 'html.parser')

for soccer in soup.find_all("table", class_="soccer odds"):
    #On extrait la competition
    tournament_part = soccer.find("span", class_="tournament_part").text
    #print tournament_part
    if tournament_part == "Coupe du Monde - Qualification":
        #print tournament_part
        #On extrait chaque match
        for match in soccer.find('tbody').find_all('tr'):
            horaire = match.find('td', class_="cell_ad").text
            team_home = match.find('td', class_="team-home").text
            team_away = match.find('td', class_="team-away").text
            score = match.find('td', class_="score").text
            cote1 = match.find('td', class_="cell_oa").text
            coteN = match.find('td', class_="cell_ob").text
            cote2 = match.find('td', class_="cell_oc").text

            print horaire + ' ' + team_home + ' ' + team_away + ' ' + score + ' ' + cote1 + ' ' + coteN + ' ' + cote2
    
browser.close()