#!/usr/bin/python2.7

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re, time, csv, os, sys
from datetime import datetime
from model import *

reload(sys)
sys.setdefaultencoding('utf-8')

browser = webdriver.Chrome()

#On ouvre le site
browser.get('http://www.flashresultats.fr/')

#On va sur la page des cotes
resultats = browser.find_element_by_css_selector('.ifmenu-odds.li4').click()

time.sleep(3)

#On recupere le tableau des resultats
resultats = browser.find_element_by_class_name('odds-content')

#On extrait le HTML pour traitement
soup = BeautifulSoup(resultats.get_attribute('innerHTML'), 'html.parser')

for soccer in soup.find_all("table", class_="soccer odds"):

    #On extrait la competition
    competition = Competition()
    competition.nom = soccer.find("span", class_="tournament_part").get_text()
    competition.pays = soccer.find("span", class_="country_part").get_text()

    #On extrait chaque match dans notre modèle
    for line in soccer.find('tbody').find_all('tr'):
        match = Match()
        
        match.competition = competition

        match.date = datetime.now().strftime("%d%m%Y")
        match.heure = line.find('td', class_="cell_ad").get_text()

        match.equipe_1.nom = line.find('td', class_="team-home").get_text()
        match.equipe_2.nom = line.find('td', class_="team-away").get_text()

        score = line.find('td', class_="score").get_text(strip=True)
        if score != "-":
            scores = score.split(":")
            match.score_1 = scores[0].strip()
            match.score_2 = scores[1].strip()

        cote_1 = line.find('td', class_="cell_oa").get_text()
        if cote_1 != "-":
            match.cote_1 = cote_1
            match.cote_2 = line.find('td', class_="cell_oc").get_text()
            match.cote_N = line.find('td', class_="cell_ob").get_text()

browser.close()