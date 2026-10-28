import time
import subprocess
import os

from Epee import Epee
from Hache import Hache

class Perso:
    def __init__(self, Prenom, vie=100, arme=None, genre="None", puissance=15):
        self.prenom = Prenom
        self.vie = vie
        self.arme = arme
        self.genre = genre
        self.puissance = puissance
        self.fiole=10

    def set_arme(self, mon_arme):
        if mon_arme.lower() == "epee":
            self.arme= Epee()
        elif mon_arme.lower() == "hache":
            self.arme=Hache()
        else:
            print("Vous n'avez pas cette arme.")
            print('Les armes disponibles sont uniquement une Epee ou une Hache')

    def attaquer(self, cible): 
        degats = self.arme.get_degats()  
        print(f"\n{self.prenom} attaque {cible.nom} avec {self.arme.get_type() or 'ses poings'} et inflige {degats} degats !")
        cible.subir_degats(degats)
        return degats

    def subir_degats(self, degats):
        self.vie -= degats
        print(f"\n {self.prenom} subit {degats} dégâts ! Il reste {self.vie} PV.")
        return self.vie <= 0

    def changer_nom(self, nouveau_nom):
        self.prenom = nouveau_nom

    def change_genre(self):
        while self.genre.lower() not in ["masculin", "féminin", "neutre"]:
            self.genre = input("Quel est votre genre (féminin/neutre/masculin) : ").lower()

    def boire_fiole(self):
        if self.fiole>0:
            print("Oullala voud buvez une bonne fiole de point de vie")
            print('Glouglouglou...')
            self.fiole-=1
            self.vie+=20
            print("Il vous reste "+str(self.fiole)+" fiole(s)")
        else:
            print("Eh mon gars t'es un pochtron t'as plus de fioles...")

    def __str__(self):
        return f"Bienvenu {self.prenom}, tu es du genre {self.genre} et tu as {self.vie} PV."