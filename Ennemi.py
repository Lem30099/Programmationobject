class Ennemi:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    def attaquer(self, cible):
        print(f"\n{self.nom} attaque {cible.prenom} et lui inflige {self.attaque} degats !")
        cible.subir_degats(self.attaque)

    def subir_degats(self, degats):
        self.vie -= degats
        print(f"\n{self.nom} subit {degats} degats ! Il reste {self.vie} PV.")
        return self.vie <= 0