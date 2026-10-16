import os
import time
import sys
from  Perso import Perso
from  Carte import Carte

def amazon_city_builder():
    def choix_maps(maps,nom):
        if maps.lower()==nom.lower():
            return True
    def get_maps_with_name(nom):
        for i in range (len(maps)):
            if maps[i].get_nom().lower()==nom.lower():
                return maps[i]

    maps=[Carte("Hyrule"),Carte("End"), Carte("Mordudumordor")]
    print("Bienvenu dans Amazon City Builder  bâtisseur ! Ici, la terre t'appartient. Deviens le plus grand maire que le monde ait jamais connu...")
    time.sleep(2)
    print("Tu vas devenir le plus grand bâtisseur du pays!!")
    time.sleep(2)
    print("Mais tout d'abord il te faut un prénom")
    time.sleep(1)
    Hero = Perso(input("Quel est votre prénom: "))
    print("Bienvenu ", Hero.prenom, " !")
    print("AH oui et quelle est ton genre ?")   
    Hero.change_genre()
    print(Hero)
    time.sleep(2)
    print("\n")
    carte_choisie=None
    while True:
        for i in range (len(maps)):
            print(maps[i].get_nom())
        nomCarte=input("Quelle map veux-tu choisir pour constuire ta futur ville Amazon ? ")
        
        if nomCarte.lower()=='chrystelle':
            print("Ah bah tu viens d'activer le cheatcode pour avoir l'argent infini")
            time.sleep(2)
            print("Bah ça sert plus a rien que tu joue au jeu")
            print("En plus Chrystelle c'est la meilleur maman du monde <3<3")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            amazon_city_builder()
        
        if choix_maps(nomCarte, 'Hyrule'):
            carte_choisie = get_maps_with_name('Hyrule')
            break
        
        if choix_maps(nomCarte, 'End'):
            carte_choisie=get_maps_with_name('End')
            break
        
        if choix_maps(nomCarte, 'Mordudumordor'):
            carte_choisie=get_maps_with_name('Mordudumordor')
            break    

    carte_choisie.phrase_de_presentation()
    carte_choisie.Construction()


amazon_city_builder()