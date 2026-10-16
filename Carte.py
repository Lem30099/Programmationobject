class Carte:
    def __init__(self, nom):
        self.nom = nom
    
    def phrase_de_presentation(self):
        print("Bienvenue sur la map",self.nom,"")
    
    def set_nom(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def Construction(self):
            if self.nom == "Hyrule":
                print("Dans ce monde tu dois construire un château avec une tour gargantuesque !!")
            if self.nom == "End":
                print("Tu dois construire une cité de l'End !! (Après c'est très vide l'End LOL)")
            if self.nom == "Mordudumordor":
                print("Ici, tu dois construire (\033[3mLa Montagne du Destin\033[0m)")