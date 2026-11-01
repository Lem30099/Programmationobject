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
debug_mode = False
Hero = None
carte_choisie = None
def plovercyt():
    proba = [60, 40, 20, 10, 5]
    class symbole():
        def __init__(self,multiplicator,valor,name,modificator):
            self.multiplicateur=multiplicator
            self.valeur=valor
            self.nom=name
            self.modificateur=modificator
        def set_multiplicateur(self,x):
            self.multiplicateur=x
            print("le multiplicateur du symbole ",self.nom," est égal a: ",self.multiplicateur)
        def set_valeur(self,x):
            self.valeur=x
            print("la valeur du symbole ",self.nom," est égal a: ",self.valeur)
        def set_modificateur(self,x):
            self.modificateur=x
            print("le modificateur ",self.modificateur," a ete ajouté a: ",self.nom)
        def get_multiplicateur(self):
            return self.multiplicateur
        def get_valeur(self):
            return self.valeur
        def get_modificateur(self):
            return self.modificateur
        def get_nom(self):
            return self.nom
        def __str__(self):
            return (
                f"{self.nom} | valeur : {self.valeur} € "
                f"| multiplicateur : x{self.multiplicateur}"
            )
    symboles = {
        "trefle": symbole(1, 7.5, "trefle", None),
        "citron": symbole(1, 10, "citron", None),
        "cloche": symbole(1, 15, "cloche", None),
        "diamand": symbole(1, 20, "diamand", None),
        "sept": symbole(1, 50, "sept", None),
    }
    def aleascii(n):
        trefle = [
        '''          ..                  '''
        ,'''        ==-=-=:   ==--=       '''
        ,'''     ..=---====. =====--      '''
        ,'''   -==------===-=====---=.    '''
        ,'''   ====----=-===========-==-  '''
        ,'''   --===------====--=-======  '''
        ,'''     ---=-----=:--=-=======-  '''
        ,'''     .=--====.:-:=-======     '''
        ,'''  .----------======---=-:     '''
        ,'''  --------========--------:   '''
        ,'''  ==----============------=   '''
        ,'''     =========#======-----:   '''
        ,'''      =======+-========.      '''
        ,'''       -==== ::-==-===        '''
        ,'''             .=               '''
        ,'''              =               '''
        ,'''              -.              '''
        ,'''               =.             '''
        ,'''                =.            '''
        ]
        citron=[
        '''               -:               '''
        ,'''            :--::::.            '''
        ,'''           ::::::::::.          '''
        ,'''        .---:::::::::::.        '''
        ,'''      .----:::::::::::::..      '''
        ,'''     --=--::::::::::::::...     '''
        ,'''    -===--:::::::::::.......    '''
        ,'''   -===--::::::::::..........   '''
        ,'''  .====---:::::::::.:.......:   '''
        ,'''  :==++=-----:::::::...::..:::  '''
        ,'''  :=+++=----:::::::::::::::::.  '''
        ,'''   =+++===-----::::::::::::::   '''
        ,'''   :=+++===------:::::::::::.   '''
        ,'''    ==+++===------:::::::::.    '''
        ,'''     .=++++++===----------      '''
        ,'''       -=***+++++====---.       '''
        ,'''          ++++++++===.          '''
        ,'''            -++++==             '''
        ,'''              +*:               '''
        ]
        cloch=[
        '''                        :.    '''
        ,'''                      .##=    '''
        ,'''                     @#*+%    '''
        ,'''                    %%**#     '''
        ,'''                   .#**%      '''
        ,'''                  %#*#:       '''
        ,'''                 @%*+%        '''
        ,'''                @%%+%         '''
        ,'''            .++..=:%-         '''
        ,'''           ++-.....-          '''
        ,'''         =*+:.... .-:         '''
        ,'''       :=+=..... ..+.         '''
        ,'''  .+++++--.:... ..=+          '''
        ,'''  @@@*=.....::...:=.          '''
        ,'''   :%%%%%+.....:--+           '''
        ,'''      *#%%###....::           '''
        ,'''         +%##+-*::=:          '''
        ,'''            #=+%@@++.         '''
        ,'''                 =@@          '''
        ]
        diamon=[
        '''                                 '''
        ,'''                                 '''    
        ,'''       *%....@.....%.::-@*       '''
        ,'''     =:-::.:@.......@::::=+=     '''
        ,'''   .+=:.:#:@...:::...@:#:::+*.   '''
        ,'''  %.+:..:%%....:.::.:.@%::::*=%  '''
        ,''' #+=#-====-------------====-#=+# '''
        ,'''  @.=@...-%:...:::::::@----@==@  '''
        ,'''   .+=@:.--#...::::::*----@=*.   '''
        ,'''     @-#:--=:.:::::::+---#=@     '''
        ,'''       ++---@:::::::@---*+.      '''
        ,'''        @==---:::::-:-+=@        '''
        ,'''         .+%-#:::::#-%+.         '''
        ,'''           @@-%:::%-@@           '''
        ,'''            -%-:::+%=            '''
        ,'''              @%:%%              '''
        ,'''               =%=               '''
        ,'''                                 '''
        ,'''                                 '''
        ]
        sep=[
        '''  @++++++++++++++++++++*@:'''
        ,'''  @#==================-#@:'''
        ,''' :=#===+*##########*=**@@.'''
        ,''' @**##=*@@@@@@@@@@%##=@*  '''
        ,''' @##@@:.        %=###@.   '''
        ,'''-=#@%.         @#=#@@.    '''
        ,'''@%@@.        -*#+*@@.     '''
        ,'''            @-*=#%@.      '''
        ,'''           @+*+*=@.       '''
        ,'''          @*+++#@*        '''
        ,'''         @*+++*=@.        '''
        ,'''        @+*+++#@#         '''
        ,'''       *=*+++++@.         '''
        ,'''       @#**++*=@.         '''
        ,'''      @******##@          '''
        ,'''      %#*****#%#          '''
        ,'''     *-#*****#@*          '''
        ,'''     @*#######@*          '''
        ,'''     @@@@@@@@@@*          '''
        ]
        if n==0:
            return trefle
        elif n==1:
            return citron
        elif n==2:
            return cloch 
        elif n==3:
            return diamon
        elif n==4:
            return sep
    def choisir_symbole():
        return aleascii(random.choices(range(5),proba,k=1)[0])
    def tour_ascii(somme,dette):
        if somme < dette:
            print(f"argent insuffisant : {somme} € disponibles, {dette} € nécessaires.")
            return None
        somme -= dette
        print(f"Mise du tour : {dette} € ; argent après paiement : {somme} €")
        time.sleep(10)
        resultat=""
        p=0
        a=choisir_symbole()
        if a[0]=='''          ..                  ''':
            variablea=symboles["trefle"]
        elif a[0]=='''               -:               ''':
            variablea=symboles["citron"]
        elif a[0]=='''                        :.    ''':
            variablea=symboles["cloche"]
        elif a[0]=='''                                 ''':
            variablea=symboles["diamand"]
        elif a[0]=='''  @++++++++++++++++++++*@:''':
            variablea=symboles["sept"]
        b=choisir_symbole()
        if b[0]=='''          ..                  ''':
            variableb=symboles["trefle"]
        elif b[0]=='''               -:               ''':
            variableb=symboles["citron"]
        elif b[0]=='''                        :.    ''':
            variableb=symboles["cloche"]
        elif b[0]=='''                                 ''':
            variableb=symboles["diamand"]
        elif b[0]=='''  @++++++++++++++++++++*@:''':
            variableb=symboles["sept"]
        c=choisir_symbole()
        if c[0]=='''          ..                  ''':
            variablec=symboles["trefle"]
        elif c[0]=='''               -:               ''':
            variablec=symboles["citron"]
        elif c[0]=='''                        :.    ''':
            variablec=symboles["cloche"]
        elif c[0]=='''                                 ''':
            variablec=symboles["diamand"]
        elif c[0]=='''  @++++++++++++++++++++*@:''':
            variablec=symboles["sept"]
        d=choisir_symbole()
        if d[0]=='''          ..                  ''':
            variabled=symboles["trefle"]
        elif d[0]=='''               -:               ''':
            variabled=symboles["citron"]
        elif d[0]=='''                        :.    ''':
            variabled=symboles["cloche"]
        elif d[0]=='''                                 ''':
            variabled=symboles["diamand"]
        elif d[0]=='''  @++++++++++++++++++++*@:''':
            variabled=symboles["sept"]
        for i in a:
            resultat+=i
            resultat+=b[p]
            resultat+=c[p]
            resultat+=d[p]+"\n"
            p+=1
        print(resultat)
        resultat=""
        p=0
        e=choisir_symbole()
        if e[0]=='''          ..                  ''':
            variablee=symboles["trefle"]
        elif e[0]=='''               -:               ''':
            variablee=symboles["citron"]
        elif e[0]=='''                        :.    ''':
            variablee=symboles["cloche"]
        elif e[0]=='''                                 ''':
            variablee=symboles["diamand"]
        elif e[0]=='''  @++++++++++++++++++++*@:''':
            variablee=symboles["sept"]
        f=choisir_symbole()
        if f[0]=='''          ..                  ''':
            variablef=symboles["trefle"]
        elif f[0]=='''               -:               ''':
            variablef=symboles["citron"]
        elif f[0]=='''                        :.    ''':
            variablef=symboles["cloche"]
        elif f[0]=='''                                 ''':
            variablef=symboles["diamand"]
        elif f[0]=='''  @++++++++++++++++++++*@:''':
            variablef=symboles["sept"]
        g=choisir_symbole()
        if g[0]=='''          ..                  ''':
            variableg=symboles["trefle"]
        elif g[0]=='''               -:               ''':
            variableg=symboles["citron"]
        elif g[0]=='''                        :.    ''':
            variableg=symboles["cloche"]
        elif g[0]=='''                                 ''':
            variableg=symboles["diamand"]
        elif g[0]=='''  @++++++++++++++++++++*@:''':
            variableg=symboles["sept"]
        h=choisir_symbole()
        if h[0]=='''          ..                  ''':
            variableh=symboles["trefle"]
        elif h[0]=='''               -:               ''':
            variableh=symboles["citron"]
        elif h[0]=='''                        :.    ''':
            variableh=symboles["cloche"]
        elif h[0]=='''                                 ''':
            variableh=symboles["diamand"]
        elif h[0]=='''  @++++++++++++++++++++*@:''':
            variableh=symboles["sept"]
        for i in e:
            resultat+=i
            resultat+=f[p]
            resultat+=g[p]
            resultat+=h[p]+"\n"
            p+=1
        print(resultat)
        resultat=""
        p=0
        j=choisir_symbole()
        if j[0]=='''          ..                  ''':
            variablej=symboles["trefle"]
        elif j[0]=='''               -:               ''':
            variablej=symboles["citron"]
        elif j[0]=='''                        :.    ''':
            variablej=symboles["cloche"]
        elif j[0]=='''                                 ''':
            variablej=symboles["diamand"]
        elif j[0]=='''  @++++++++++++++++++++*@:''':
            variablej=symboles["sept"]
        k=choisir_symbole()
        if k[0]=='''          ..                  ''':
            variablek=symboles["trefle"]
        elif k[0]=='''               -:               ''':
            variablek=symboles["citron"]
        elif k[0]=='''                        :.    ''':
            variablek=symboles["cloche"]
        elif k[0]=='''                                 ''':
            variablek=symboles["diamand"]
        elif k[0]=='''  @++++++++++++++++++++*@:''':
            variablek=symboles["sept"]
        l=choisir_symbole()
        if l[0]=='''          ..                  ''':
            variablel=symboles["trefle"]
        elif l[0]=='''               -:               ''':
            variablel=symboles["citron"]
        elif l[0]=='''                        :.    ''':
            variablel=symboles["cloche"]
        elif l[0]=='''                                 ''':
            variablel=symboles["diamand"]
        elif l[0]=='''  @++++++++++++++++++++*@:''':
            variablel=symboles["sept"]
        m=choisir_symbole()
        if m[0]=='''          ..                  ''':
            variablem=symboles["trefle"]
        elif m[0]=='''               -:               ''':
            variablem=symboles["citron"]
        elif m[0]=='''                        :.    ''':
            variablem=symboles["cloche"]
        elif m[0]=='''                                 ''':
            variablem=symboles["diamand"]
        elif m[0]=='''  @++++++++++++++++++++*@:''':
            variablem=symboles["sept"]
        for i in j:
            resultat+=i
            resultat+=k[p]
            resultat+=l[p]
            resultat+=m[p]+"\n"
            p+=1
        print(resultat)
        grille = [
            [(a, variablea), (b, variableb), (c, variablec), (d, variabled)],
            [(e, variablee), (f, variablef), (g, variableg), (h, variableh)],
            [(j, variablej), (k, variablek), (l, variablel), (m, variablem)],
        ]
        gains = 0
        for ligne in grille:
            if all(case[0] == ligne[0][0] for case in ligne):
                symbole_gagnant = ligne[0][1]
                gain = symbole_gagnant.get_valeur() * symbole_gagnant.get_multiplicateur() * 1.5
                gains += gain
                print(f"Ligne gagnante : {symbole_gagnant.get_nom()} ! +{gain} €")
        for colonne in range(4):
            cases = [grille[ligne][colonne] for ligne in range(3)]
            if all(case[0] == cases[0][0] for case in cases):
                symbole_gagnant = cases[0][1]
                gain = symbole_gagnant.get_valeur() * symbole_gagnant.get_multiplicateur()
                gains += gain
                print(f"Colonne gagnante : {symbole_gagnant.get_nom()} ! +{gain} €")
        somme += gains
        if gains == 0:
            print("Aucun gain cette fois-ci.")
        else:
            print(f"Total des gains de ce tour : {gains} €")
        print()
        return somme
    def restart():
        restart=int(input("continuer de jouer 1? 1 oui, 2 non"))
        if restart==2:
            plovercyt()
        elif restart!=1:
            print("TU VEUX JOUER AVEC MOI, LE DIVIN CRéATEUR")
            time.sleep(1000000000000000000000000000000000000000000000000000)
    def boutique_ameliorations(somme):
        print("BOUTIQUE D'AMÉLIORATIONS")
        print(f"Ton argent : {somme} €")
        print("Choisis le symbole à améliorer :")
        noms = list(symboles.keys())
        for numero, nom in enumerate(noms, start=1):
            print(f"{numero}. {symboles[nom]}")
        try:
            choix = int(input("Numéro du symbole (0 pour passer) : "))
        except ValueError:
            print("Choix invalide : aucune amélioration achetée.")
            boutique_ameliorations(somme)
        if choix == 0:
            print("Tu passes ton tour à la boutique.")
            restart()
            return somme
        if choix < 1 or choix > len(noms):
            print("Ce symbole n'existe pas.")
            boutique_ameliorations(somme)
        symbole_choisi = symboles[noms[choix - 1]]
        print("Que veux-tu améliorer ?")
        print("1. Augmenter la valeur de 2 €")
        print("2. Augmenter le multiplicateur de 0.25")
        try:
            type_amelioration = int(input("Ton choix : "))
        except ValueError:
            print("aucune amélioration achetée.")
            restart()
            boutique_ameliorations(somme)
        prix = symbole_choisi.get_valeur() * 5
        if type_amelioration not in (1, 2):
            print("Amélioration inconnue.")
            boutique_ameliorations(somme)
        if somme < prix:
            print(f"Pas assez d'argent, l'amélioration coûte {prix} €.")
            boutique_ameliorations(somme)
        somme -= prix
        if type_amelioration == 1:
            symbole_choisi.set_valeur(symbole_choisi.get_valeur() + 2)
        else:
            symbole_choisi.set_multiplicateur(
                symbole_choisi.get_multiplicateur() + 0.25
            )
        print(f"Amélioration achetée pour {prix} €.")
        print(f"Nouvelles caractéristiques : {symbole_choisi}")
        print(f"Solde restant : {somme} €")
        restart()
        return somme
    def print_ascii(somme, dette):
        nombre_tours = 0
        tours_max = 50
        dette_totale = 0
        gains_cumules = 0
        print("Objectif : récupérer au moins autant d'argent que le total des mises.")
        print(f"Solde de départ : {somme} € | Première mise : {dette} €")
        while nombre_tours < tours_max:
            if somme < 0:
                print("Tu n'as plus assez d'argent pour payer la prochaine mise, looser ಠ_ಠ")
                amazon_city_builder()
            mise_du_tour = dette
            dette_totale += mise_du_tour
            solde_avant_tour = somme
            nouveau_solde = tour_ascii(somme, mise_du_tour)
            if nouveau_solde is None:
                print("Mise impossible, looser ಠ_ಠ")
                amazon_city_builder()
            gains_du_tour = nouveau_solde - (solde_avant_tour - mise_du_tour)
            gains_cumules += gains_du_tour
            somme = nouveau_solde
            nombre_tours += 1
            print(f"Tour {nombre_tours}/{tours_max}")
            print(f"Solde : {somme} €")
            print(f"Gains cumulés : {gains_cumules} €")
            print(f"Mises cumulées : {dette_totale} €")
            if nombre_tours % 5 == 0 and nombre_tours < tours_max:
                dette *= 1.25
                print(f"Nouvelle mise pour les prochains tours : {dette} €")
                somme = boutique_ameliorations(somme)
        print("FIN")
        print(f"Nombre de tours joués : {nombre_tours}/{tours_max}")
        print(f"Total des gains : {gains_cumules} €")
        print(f"Total des mises accumulées : {dette_totale} €")
        print(f"Solde restant : {somme} €")
        if nombre_tours == tours_max and gains_cumules >= dette_totale:
            print("Tes gain couvrent toutes les mises accumulés, bien joué ദ്ദി(•ᴗ•)")
            amazon_city_builder()
        else:
            print("Tes gain ne couvrent pas toutes les mises accumulés, looser ಠ_ಠ")
            amazon_city_builder()
        return somme
    somme = 1000
    dette = 50
    print_ascii(somme, dette)
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
        print("Il s'agit d'un miroir mais qui est bizarre. Tu remarque que tu peux passer la main à travers")
        print("Tu décides alors de passer entièrement dans le miroir...")
        mon_sleep(3)
        subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
        plovercyt()
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
        plovercyt()
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
        plovercyt()
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
                print("Après avoir jeter l'Anneau vous avez réussit la mission vous voila récompenser avec le meilleur fromage du royaume mes félicitations")
                mon_sleep(3)
                print('A une prochaine jeune aventurier')
                mon_sleep(2)
                subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
                amazon_city_builder()
                break
        else:
            print("Gandébile se met a crier et POUF tu tombes dans un long trou par peur")
            mon_sleep(2)
            subprocess.run(["cmd", "/c", "cls"] if os.name == "nt" else ["clear"], check=False)
            plovercyt()
            amazon_city_builder()
            return
amazon_city_builder()