import sqlite3

db = sqlite3.connect('db/betapp.db')
cursor = db.cursor()

cursor.execute("INSERT INTO TEAMS(name,country) VALUES(?,?)", (str(team_visitor), 'null'))
cursor.execute("INSERT INTO MATCHS(date,heure,score_home, score_visitor, team_home, team_visitor) VALUES(?,?,?,?,?,?)", (datetime.now().strftime("%d%m%Y"), horaire, score_visitor, 0, team_home, team_visitor))
