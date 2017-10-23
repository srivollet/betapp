#!/usr/bin/python2.7

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re, time, csv, os, sqlite3
from datetime import datetime, timedelta

browser = webdriver.Chrome()

#On ouvre le site
browser.get('http://www.flashresultats.fr/')

resultats = browser.find_element_by_css_selector('.ifmenu-odds.li4').click()

time.sleep(3)

#On va sur la page des cotes
yesterday = datetime.today() - timedelta(1)
print yesterday.strftime("%d%m%Y")
browser.find_element_by_class_name('yesterday').click()

time.sleep(10)

#On recupere le tableau des resultats
resultats = browser.find_element_by_class_name('odds-content')

#On extrait le HTML pour traitement
soup = BeautifulSoup(resultats.get_attribute('innerHTML'), 'html.parser')

for soccer in soup.find_all("table", class_="soccer odds"):

    #On extrait la competition
    tournament_part = soccer.find("span", class_="tournament_part").text

    exist = False

    #Ouverture du fichier / creation du fichier
    if os.path.exists("data/" + tournament_part + ".csv"):
        exist = True

    c = csv.writer(open("data/" + tournament_part + ".csv", "ab"))

    if not exist:
        c.writerow(["date", "horaire","team_home","team_away","score","cote1","coteN","cote2"])

    #db = sqlite3.connect('db/betapp.db')
    #cursor = db.cursor()

    #On extrait chaque match
    for match in soccer.find('tbody').find_all('tr'):
        horaire = match.find('td', class_="cell_ad").text.encode('utf-8')
        team_home = match.find('td', class_="team-home").text.encode('utf-8')
        team_visitor = match.find('td', class_="team-away").text.encode('utf-8')
        score = match.find('td', class_="score").text.encode('utf-8')
        cote1 = match.find('td', class_="cell_oa").text.encode('utf-8')
        coteN = match.find('td', class_="cell_ob").text.encode('utf-8')
        cote2 = match.find('td', class_="cell_oc").text.encode('utf-8')

        #insertion dans la base
        c.writerow([yesterday.strftime("%d%m%Y"), horaire,team_home,team_visitor,score,cote1,coteN,cote2])
        #cursor.execute("INSERT INTO TEAMS(name,country) VALUES(?,?)", (str(team_visitor), 'null'))
        #saveTeams(cursor, team_home)
#        cursor.execute("INSERT INTO MATCHS(date,heure,score_home, score_visitor, team_home, team_visitor) VALUES(?,?,?,?,?,?)", 
#            (datetime.now().strftime("%d%m%Y"), horaire, score_visitor, 0, team_home, team_visitor))


browser.close()
    