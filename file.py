

exist = False

#Ouverture du fichier / creation du fichier
if os.path.exists("data/" + tournament_part + ".csv"):
    exist = True

c = csv.writer(open("data/" + tournament_part + ".csv", "ab"))

if not exist:
    c.writerow(["date", "horaire","team_home","team_away","score","cote1","coteN","cote2"])

c.writerow([datetime.now().strftime("%d%m%Y"), horaire,team_home,team_visitor,score,cote1,coteN,cote2])