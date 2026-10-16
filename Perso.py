class Perso:
    def __init__(self,Prenom, Vie = 100, Arme = None, Genre="None"):
        self.prenom = Prenom
        self.vie = Vie
        self.arme = Arme
        self.genre = Genre

    def attaquer (self,cible,puissance):
        cible.vie -= puissance

    def changer_nom (self, nouveau_nom):
        self.prenom = nouveau_nom
    
    def change_genre (self):
        while self.genre!="masculin" and self.genre!="féminin":
            self.genre = input("Quel est votre genre (masculin/féminin): ")
            if self.genre.lower()=="masculin": 
                self.genre="masculin"
                return self.genre
            elif self.genre.lower()=="féminin":
                self.genre = "féminin"
                return self.genre        

    def __str__(self):
        return f"Bienvenu {str(self.prenom)}, tu es du genre {self.genre} et tu a {str(self.vie)} pv."