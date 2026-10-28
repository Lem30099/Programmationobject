class Carte:
    def __init__(self, nom, definition):
        self.nom = nom
        self.definition= definition

    def phrase_de_presentation(self):
        print("Bienvenue sur la map",self.nom,"")
    
    def set_nom(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def construction(self):
        print(self.definition)

                