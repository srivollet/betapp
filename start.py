#!/usr/bin/python2.7

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re, time, csv, os

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
    tournament_part = soccer.find("span", class_="tournament_part").text

    exist = False

    #Ouverture du fichier / creation du fichier
    if os.path.exists(tournament_part + ".csv"):
        exist = True

    c = csv.writer(open(tournament_part + ".csv", "ab"))

    if not exist:
        c.writerow(["horaire","team_home","team_away","score","cote1","coteN","cote2"])

    #On extrait chaque match
    for match in soccer.find('tbody').find_all('tr'):
        horaire = match.find('td', class_="cell_ad").text.encode('utf-8')
        team_home = match.find('td', class_="team-home").text.encode('utf-8')
        team_away = match.find('td', class_="team-away").text.encode('utf-8')
        score = match.find('td', class_="score").text.encode('utf-8')
        cote1 = match.find('td', class_="cell_oa").text.encode('utf-8')
        coteN = match.find('td', class_="cell_ob").text.encode('utf-8')
        cote2 = match.find('td', class_="cell_oc").text.encode('utf-8')

        #insertion dans la base
        c.writerow([horaire,team_home,team_away,score,cote1,coteN,cote2])

browser.close()