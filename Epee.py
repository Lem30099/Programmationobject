import random
from Arme import Arme

class Epee(Arme):
    
    def __init__(self):
        super().__init__("Epee", 20)

    def get_degats(self):
        proba_touche=random.randint(1, 10)
        if proba_touche<=7:
            nbr_point=self.degats
        else:
            nbr_point=5
        return nbr_point
