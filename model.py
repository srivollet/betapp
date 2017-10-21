from enum import Enum

class TypeCompetition(Enum):
    CHAMPIONNAT = 0
    COUPE = 1
    AMICAL = 2

class Pays:
    nom = ""
    continent = ""
    def __str__(self):
         return "nom= %s continent=%s" % (self.nom, self.continent)

class Competition:
    nom = ""
    pays = Pays()
    type = Enum
    def __str__(self):
         return "nom=%s pays=%s type=%s" % (self.nom, self.pays, self.type) 

class Equipe:
    nom = ""
    pays = ""

class Match:
    date = ""
    equipe_domicile = Equipe()
    score_domicile = 0
    cote_equipe_domicile = 0
    equipe_visiteur = Equipe()
    score_visiteur = 0
    cote_equipe_visiteur = 0
    competition = Competition()


