import os
import subprocess
import time
import random

from Perso import Perso
from Carte import Carte
from End import End
from Hyrule import Hyrule
from Mordudumordor import Mordudumordor
from Ganondorf import Ganondorf

debug_mode = True
Hero = None
carte_choisie = None


def mon_sleep(temps):
    if debug_mode==False:
        time.sleep(temps)



def amazon_city_builder():
    global carte_choisie, Hero
    
    def choix_maps(maps,nom):
        if maps.lower()==nom.lower():
            return True

    def get_maps_with_name(nom):
        for i in range (len(maps)):
            if maps[i].get_nom().lower()==nom.lower():
                return maps[i]

    maps=[Hyrule(), End(), Mordudumordor()]
    print("Bienvenu dans Amazon City Builder  bâtisseur ! Ici, la terre t'appartient. Deviens le plus grand maire que le monde ait jamais connu...")
    mon_sleep(2)
    print("Tu vas devenir le plus grand bâtisseur du pays!!")
    mon_sleep(2)
    print("Mais tout d'abord il te faut un prénom")
    mon_sleep(1)
    Hero = Perso(input("Quel est votre prénom: "))
    print("Bienvenu ", Hero.prenom, " !")
    print("AH oui et quelle est ton genre ?")   
    Hero.change_genre()
    print(Hero)
    mon_sleep(2)
    print("\n")
    while True:
        for map in maps:  
            print(map.get_nom())
        
        nomCarte=input("Quelle map veux-tu choisir pour constuire ta futur ville Amazon ? ")
        
        if nomCarte.lower()=='chrystelle':
            print("Ah bah tu viens d'activer le cheatcode pour avoir l'argent infini")
            mon_sleep(2)
            print("Bah ça sert plus a rien que tu joue au jeu")
            print("En plus Chrystelle c'est la meilleur maman du monde <3<3")
            mon_sleep(5)
            subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
            amazon_city_builder()
            return
        
        selected_map = None
        for map in maps:
            if map.get_nom().lower() == nomCarte.lower():
                selected_map = map
                break

        if selected_map:
            carte_choisie = selected_map
            if nomCarte.lower() == 'hyrule':
                hyrule()
                break
            elif nomCarte.lower() == 'end':
                end()
                break
            elif nomCarte.lower() == 'mordudumordor':
                mordudumordor()
                break


def presentation_hyrule():
    carte_choisie.phrase_de_presentation()
    mon_sleep(2)
    carte_choisie.construction()    
    print('Mais pour cela tu dois sauver la princesse Zelda qui a été enlevée par Ganondorf !')
    mon_sleep(2)


def hyrule():
    presentation_hyrule()
    while True:
        quete = input("Accepter la quete (oui/non) ")
        if quete.lower() == 'non':
            print('Ok')
            mon_sleep(2)
            print("Dommage tu ne pourras pas construire ton chateau...")
            mon_sleep(5)
            subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
            amazon_city_builder()
            return
        elif quete.lower() == 'oui':
            print("ok c'est parti pour la quete")
            mon_sleep(1)
            print('Va et sauve la princesse !')
            mon_sleep(2)
            print("Alors tu marchais dans la foret quand tu apercois un coffre. Tu l'ouvres et tu trouves une epee et une hache.")
            Hero.set_arme("Epee")  
            mon_sleep(2)
            print('Puis tu continues ton chemin et tu arrives devant le chateau de Ganondorf.')
            mon_sleep(2)
            print("Ganondorf t'attend devant son chateau !")
            mon_sleep(1)
            combat_ganondorf()


def combat_ganondorf():
    global Hero
    ganondorf = Ganondorf()
    print(f"\n=== COMBAT CONTRE {ganondorf.nom.upper()} ===")
    print(f"{ganondorf.nom} : {ganondorf.vie} PV | {Hero.prenom} : {Hero.vie} PV")
    mon_sleep(2)

    while Hero.vie > 0 and ganondorf.vie > 0:
        print("\n1. Attaquer")
        print("2. Fuir")
        print("3. Boire une fiole de vie")
        print("4. Changer d'arme")
        choix = input("Que fais-tu ? (1/4) : ")

        if choix == "1":
            Hero.attaquer(ganondorf)
            if ganondorf.vie > 0:
                ganondorf.attaquer(Hero)
        elif choix == "2":
            print(f"\n{Hero.prenom} fuit le combat... LACHE !")
            Hero.vie -= 10
            print(f"Tu perds 10 PV par lâcheté. Il te reste {Hero.vie} PV.")
            mon_sleep(2)
            return False
        elif choix =='3':
            Hero.boire_fiole()
            mon_sleep(2)
        elif choix=="4":
            choix_arme=input("Quel arme voulez-vous prendre ? (Epee ou Hache) ")
            Hero.set_arme(choix_arme)

        mon_sleep(2)
        print(f"\n{ganondorf.nom} : {ganondorf.vie} PV | {Hero.prenom} : {Hero.vie} PV")

    if Hero.vie > 0:
        print(f"\nVICTOIRE ! {Hero.prenom} a vaincu {ganondorf.nom} !")
        mon_sleep(2)
        print("La princesse Zelda est sauvée !")
        print('Tu peux maintenant construire et vivre paisblement dans ton chateau')
        print("Mais quelque chose t'intrigue dans le Chateau de Ganondorf")
        print("Il s'agit d'un miroir mais qui est bizarre. Tu remarque qeu tu me passer la main à travers")
        print("Tu décides alors de passer entièrement dans le miroir...")
        mon_sleep(3)
        subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
        #clover_cyt() a jaouter dès que tu as la fonction
        exit()
    else:
        print(f"\n{Hero.prenom} est vaincu par {ganondorf.nom}...")
        mon_sleep(3)
        subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
        amazon_city_builder()
        exit()


def présentation_end():
    print("Maintenant, tu dois construire ta cité de L'End")
    print("Pour ce faire tu vas devoir tuer l'Ender Dragon")
    mon_sleep(2)


def lancer_de():
    print("\nTu saisis ton de...", end="", flush=True)
    time.sleep(0.8)
    print(" il roule sur le sol...", end="", flush=True)
    time.sleep(0.8)
    print(" il rebondit...", end="", flush=True)
    time.sleep(0.8)
    resultat = random.randint(1, 6)
    print(f" TOMBE SUR {resultat} !\n")
    return resultat


def detruire_cristaux():
    global Hero
    print("Il y a 3 cristaux violets a detruire pour affaiblir l'Ender Dragon.")
    print("Si tu ne fais pas 4, 5 ou 6 au de, tu perds 20 PV.")
    mon_sleep(2)

    cristaux_detruits = 0
    
    for i in range(1, 4):
        print(f"\n--- Cristal {i}/3 ---")
        input("Appuie sur Entree pour lancer le de...")
        de = lancer_de()

        if de >= 4:
            print(f"SUCCES ! Le cristal {i} explose en eclats violets !")
            cristaux_detruits += 1
        else:
            print(f"ECHEC ! Le cristal {i} resiste...")
            Hero.subir_degats(20)
            if Hero.vie <= 0:
                print(f"\n{Hero.prenom} est vaincu... GAME OVER !")
                mon_sleep(3)
                subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
                amazon_city_builder()
                exit()
        
        mon_sleep(2)

    print(f"\n Score : {cristaux_detruits}/3 cristaux détruits.")
    mon_sleep(1)

    if cristaux_detruits == 3:
        print("\n TOUS LES CRISTAUX SONT DÉTRUITS !")
        mon_sleep(1)
        print("L'Ender Dragon rugit de douleur... Il est affaibli !")
        mon_sleep(2)
        print("Tu lui met alors le coups final")
        print("Tu as alors ta cité de l'end mes félicitation jeune aventurier")
        mon_sleep(3)
        subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
        amazon_city_builder() 
        
    else:
        print("\n Il reste uniquement des cristaux intacts...")
        Hero.subir_degats(100)
        if Hero.vie <= 0:
            print(f"\n{Hero.prenom} est vaincu...")
            mon_sleep(3)
            subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
            amazon_city_builder()
            exit() 


def end():
    présentation_end()
    while True: 
        dragon=input("Accepter la quete (oui/non) ")
        if dragon.lower()=='non':
            print('Ok la mauviette bah recommence looser')
            mon_sleep(5)
            subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
            amazon_city_builder()
            return
        elif dragon.lower()=='oui':
                print("ok c'est parti pour la quete")
                mon_sleep(2)
                print("Tu arrive au milieu d'une île flottante. Tu vois un dragon noir qui te regarde avec des yeux violets.") 
                print("Tu apercois des pillier en pierre noir et à leur sommet des cristaux violets.")
                mon_sleep(3)
                print("Tu dois détruire ces cristaux pour affaiblir le dragon et le tuer.")
                mon_sleep(2)
                print("BONNE CHANCE AVENTURIER !")
                detruire_cristaux()
                break


def presentation_mordudumordor():
    carte_choisie.phrase_de_presentation()
    mon_sleep(2)
    carte_choisie.construction()
    print("Bienvenue à Mordudumordor, terre de Sauronchon ! (et oui on avait pas le budget pour la license LOTR mdr)")
    mon_sleep(2)
    print("Ici, une seule mission : détruire l'Anneau Unique en le jetant dans la Montagne du Destin.")
    mon_sleep(2)
    print("Mais pour y accéder, tu dois d'abord vaincre Sauronchon lui-même...")
    mon_sleep(2)


def combat_sauronchon():
    global Hero
    print("\n=== COMBAT CONTRE SAURONCHON ===")
    print("Sauronchon te fixe avec ses yeux rouges...")
    mon_sleep(2)
    print("\nQue fais-tu ?")
    print("1. Utiliser le baton magique de Gandébile")
    print("2. Attaquer avec ton epee de Mithril")
    print("3. Fuir en criant 'MAMAN !'")

    choix_sauronchon = input("Ton choix (1/2/3) : ")

    if choix_sauronchon == "1":
        print("Tu utilises le baton de Gandébile")
        mon_sleep(2)
        print("Vous ne passerez pas... sauf si vous avez le code Wi-Fi !")
        mon_sleep(2)
        print('OOH NONN !!! Un trou apparait sous tes pieds')
        print('Apres quelle idee de choisir le baton magique de ce debile de Gandébile LLLLOOOOLLLL')
        mon_sleep(2)
        print("AU REVOIR JEUNE AVENTURIERRRR..!!!")
        subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
        # clover_cyt()  # À ajouter quand tu auras la fonction
        amazon_city_builder()
        return

    elif choix_sauronchon == "2":
        print("Grace a la puissance du ciel tu oneshot Sauronchon")
        print("Tu peux maintenant detruire l'Anneau Unique !")
        return True 

    elif choix_sauronchon == "3":
        print("Sauronchon te voit fuir et te teleporte")
        mon_sleep(2)
        print("Tu es envoye dans un autre monde...")
        subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
        # clover_cyt()  # À ajouter quand tu auras la fonction
        amazon_city_builder()  
        return


def mordudumordor():
    presentation_mordudumordor()
    while True:
        choix = input("\nVeux-tu affronter Sauronchon pour detruire l'Anneau ? (oui/non) ").lower()
        if choix == "oui":
            print("\nTu marches vers la tour de Barad-dur")
            mon_sleep(2)
            print("Sur le chemin tu trouves une epee en mithril plantee dans le cadavre d'un orque")
            mon_sleep(3)
            Hero.arme = "Epee de Mithril"  
            print("Grace a ta force tu extirpes cette extraordinaire epee.")
            mon_sleep(3)
            print("Sauronchon apparait devant toi, ses yeux brulants comme du feu.")
            mon_sleep(2)
            if combat_sauronchon():
                print("\nTu peux maintenant detruire l'Anneau Unique !")
                print("Maintenant, il faut jeter l'Anneau dans la Montagne de Dustin")
                print("Après avoir jeter l'Anneu vous avez réussit la mission vous voila récompenser avec le meilleur fromage du royaume mes félicitations")
                mon_sleep(3)
                print('A une prochaine jeune aventurier')
                mon_sleep(2)
                subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
                amazon_city_builder()
                break
        else:
            print("Gandébile se met a crier et POUF tu tombes dans un long trou")
            mon_sleep(2)
            subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
            # clover_cyt()  # À ajouter quand tu auras la fonction
            amazon_city_builder()
            return


amazon_city_builder()