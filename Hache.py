import random
from Arme import Arme

class Hache(Arme):
    
    def __init__(self):
        super().__init__("Hache", 35)


    def get_degats(self):
        proba_touche=random.randint(1, 10)
        if proba_touche<=5:
            nbr_point=self.degats
        else:
            nbr_point=10
        return nbr_point
