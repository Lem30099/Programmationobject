import time

class Perso:
    
    def __init__(self,Prenom, Vie = 100, Arme = None, Genre="None"):
        self.prenom = Prenom
        self.vie = Vie
        self.arme = Arme
        self.genre = Genre

    def attaquer (self,cible,puissance):
        cible.vie -= puissance

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


def choix_maps(maps):
     if Carte.lower()=="nom":
       return 
        
     





maps = [
    {"nom": "Hyrule"},
    {"nom": "End"},
    {"nom": "Mordudumordor"},
    {"nom": "Mordor"}]



print("Bienvenu dans Amazon City Builder  bâtisseur ! Ici, la terre t'appartient. Deviens le plus grand maire que le monde vert ait jamais connu...")
time.sleep(2)
print("Tu vas devenir le plus grand bâtisseur du pays!!")
time.sleep(2)
print("Mais tout d'abord il te faut un prénom")
time.sleep(1)
Prenom = Perso(input("Quel est votre prénom: "))
print("AH oui et quelle est ton genre ?")
Prenom.change_genre()
print(Prenom)
while True:
    for i in range (len(maps)) :
        print(maps[i]["nom"])
        Carte=input("Quelle map veux-tu choisir pour constuire ton Magasin Amazon ?")

