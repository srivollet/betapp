from enum import Enum

class TypeCompetition(Enum):
    CHAMPIONNAT = 0
    COUPE = 1
    AMICAL = 2
   
class Competition:
    nom = ""
    pays = Pays()
    type = Enum
    def __str__(self):
         return "nom=%s pays=%s type=%s" % (self.nom, self.pays, self.type) 

class Equipe:
    nom = ""
    pays = ""
    def __str__(self):
         return "nom=%s pays=%s" % (self.nom, self.pays) 

class Match:
    date = ""
    heure = ""
    equipe_1 = Equipe()
    score_1 = ""
    equipe_2 = Equipe()
    score_2 = ""
    cote_1 = ""
    cote_N = ""
    cote_2 = ""
    competition = Competition()
    def __str__(self):
        return "competition=%s date=%s heure=%s equipe_1=%s score_1=%s equipe_2=%s score_2=%s cote_1=%s cote_N=%s cote_2=%s" % (self.competition, self.date, self.heure, self.equipe_1, self.score_1, self.equipe_2, self.score_2, self.cote_1, self.cote_N, self.cote_2)


