import random
import time
def clovercyt():
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
                f"{self.nom} | valeur : {self.valeur:.2f} € "
                f"| multiplicateur : x{self.multiplicateur:.2f}"
            )
    symboles = {
        "trefle": symbole(1.5, 5, "trefle", None),
        "citron": symbole(1, 5, "citron", None),
        "cloche": symbole(1, 7.5, "cloche", None),
        "diamand": symbole(1.75, 10, "diamand", None),
        "sept": symbole(2, 15, "sept", None),
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
            print(f"Solde insuffisant : {somme:.2f} € disponibles, {dette:.2f} € nécessaires.")
            return None
        somme -= dette
        print(f"Mise du tour : {dette:.2f} € | Solde après paiement : {somme:.2f} €")
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
    def boutique_ameliorations(somme):
        """Propose une amélioration payante après chaque série de 5 tours."""
        print("\n===== BOUTIQUE D'AMÉLIORATIONS =====")
        print(f"Ton solde : {somme:.2f} €")
        print("Choisis le symbole à améliorer :")
        noms = list(symboles.keys())
        for numero, nom in enumerate(noms, start=1):
            print(f"{numero}. {symboles[nom]}")
        try:
            choix = int(input("Numéro du symbole (0 pour passer) : "))
        except ValueError:
            print("Choix invalide : aucune amélioration achetée.")
            return somme
        if choix == 0:
            print("Tu passes ton tour à la boutique.")
            return somme
        if choix < 1 or choix > len(noms):
            print("Ce symbole n'existe pas.")
            return somme
        symbole_choisi = symboles[noms[choix - 1]]
        print("\nQue veux-tu améliorer ?")
        print("1. Augmenter la valeur de 2 €")
        print("2. Augmenter le multiplicateur de 0.25")
        try:
            type_amelioration = int(input("Ton choix : "))
        except ValueError:
            print("Choix invalide : aucune amélioration achetée.")
            return somme
        # Le prix est calculé à partir de get_valeur(), comme demandé.
        prix = symbole_choisi.get_valeur() * 5
        if type_amelioration not in (1, 2):
            print("Amélioration inconnue.")
            return somme
        if somme < prix:
            print(f"Pas assez d'argent : l'amélioration coûte {prix:.2f} €.")
            return somme
        somme -= prix
        if type_amelioration == 1:
            symbole_choisi.set_valeur(symbole_choisi.get_valeur() + 2)
        else:
            symbole_choisi.set_multiplicateur(
                symbole_choisi.get_multiplicateur() + 0.25
            )
        print(f"Amélioration achetée pour {prix:.2f} €.")
        print(f"Nouvelles caractéristiques : {symbole_choisi}")
        print(f"Solde restant : {somme:.2f} €")
        return somme
    def print_ascii(somme, dette):
        nombre_tours = 0
        tours_max = 50
        dette_totale = 0
        gains_cumules = 0
        print("Objectif : récupérer au moins autant d'argent que le total des mises.")
        print(f"Solde de départ : {somme:.2f} € | Première mise : {dette:.2f} €\\n")
        while nombre_tours < tours_max:
            if somme < dette:
                print("DÉFAITE ! Tu n'as plus assez d'argent pour payer la prochaine mise.")
                break
            mise_du_tour = dette
            dette_totale += mise_du_tour
            solde_avant_tour = somme
            nouveau_solde = tour_ascii(somme, mise_du_tour)
            if nouveau_solde is None:
                print("DÉFAITE ! Mise impossible.")
                break
            gains_du_tour = nouveau_solde - (solde_avant_tour - mise_du_tour)
            gains_cumules += gains_du_tour
            somme = nouveau_solde
            nombre_tours += 1
            print(f"Tour {nombre_tours}/{tours_max}")
            print(f"Solde : {somme:.2f} €")
            print(f"Gains cumulés : {gains_cumules:.2f} €")
            print(f"Mises cumulées : {dette_totale:.2f} €")
            if nombre_tours % 5 == 0 and nombre_tours < tours_max:
                dette *= 1.5
                print(f"Nouvelle mise pour les prochains tours : {dette:.2f} €")
                somme = boutique_ameliorations(somme)
        print("\\n===== FIN DE LA PARTIE =====")
        print(f"Nombre de tours joués : {nombre_tours}/{tours_max}")
        print(f"Total des gains : {gains_cumules:.2f} €")
        print(f"Total des mises accumulées : {dette_totale:.2f} €")
        print(f"Solde restant : {somme:.2f} €")
        if nombre_tours == tours_max and gains_cumules >= dette_totale:
            print("VICTOIRE ! Tes gains couvrent toutes les mises accumulées.")
        else:
            print("DÉFAITE ! Tes gains ne couvrent pas toutes les mises accumulées.")
        return somme
    somme = 1000
    dette = 100
    print_ascii(somme, dette)
clovercyt()