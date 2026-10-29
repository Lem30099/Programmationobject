import random
import time
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
        resultat=""
        resultat="pour l'objet "+self.nom+" son multiplicateur est égal à "+self.multiplicateur+" il a une valeur de "+ self.valeur+" et un modificateur qui est "+self.modificateur
        return resultat
def aleascii(n):
    trefle = [
    ""                                                                                                                                                                
    ,'''          ..                  '''
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
    ""
    ,'''               -:               '''
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
    ""       
    ,'''                        :.    '''
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
        ""         
    ,'''                                 '''
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
        ""
    ,'''  @++++++++++++++++++++*@:'''
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
        return diamon
    elif n==2:
        return citron 
    elif n==3:
        return cloch
    elif n==4:
        return sep
def print_ascii(somme,dette):
    print("Vous devez renboursez votre dette, elle a atteint ",dette,"€")
    time.sleep(10)
    resultat=""
    p=0
    a=aleascii(random.randint(0,4))
    if a[0]=='''          ..                  ''':
        variablea=symbole(1.5,5,"trefle",None)
    elif a[0]=='''               -:               ''':
        variablea=symbole(1,5,"citron",None)
    elif a[0]=='''                        :.    ''':
        variablea=symbole(1,7.5,"cloche",None)
    elif a[0]=='''                                 ''':
        variablea=symbole(1.75,10,"diamand",None)
    elif a[0]=='''  @++++++++++++++++++++*@:''':
        variablea=symbole(2,15,"sept",None)
    b=aleascii(random.randint(0,4))
    if b[0]=='''          ..                  ''':
        variableb=symbole(1.5,5,"trefle",None)
    elif b[0]=='''               -:               ''':
        variableb=symbole(1,5,"citron",None)
    elif b[0]=='''                        :.    ''':
        variableb=symbole(1,7.5,"cloche",None)
    elif b[0]=='''                                 ''':
        variableb=symbole(1.75,10,"diamand",None)
    elif b[0]=='''  @++++++++++++++++++++*@:''':
        variableb=symbole(2,15,"sept",None)
    c=aleascii(random.randint(0,4))
    if c[0]=='''          ..                  ''':
        variablec=symbole(1.5,5,"trefle",None)
    elif c[0]=='''               -:               ''':
        variablec=symbole(1,5,"citron",None)
    elif c[0]=='''                        :.    ''':
        variablec=symbole(1,7.5,"cloche",None)
    elif c[0]=='''                                 ''':
        variablec=symbole(1.75,10,"diamand",None)
    elif c[0]=='''  @++++++++++++++++++++*@:''':
        variablec=symbole(2,15,"sept",None)
    d=aleascii(random.randint(0,4))
    if d[0]=='''          ..                  ''':
        variabled=symbole(1.5,5,"trefle",None)
    elif d[0]=='''               -:               ''':
        variabled=symbole(1,5,"citron",None)
    elif d[0]=='''                        :.    ''':
        variabled=symbole(1,7.5,"cloche",None)
    elif d[0]=='''                                 ''':
        variabled=symbole(1.75,10,"diamand",None)
    elif d[0]=='''  @++++++++++++++++++++*@:''':
        variabled=symbole(2,15,"sept",None)
    for i in a:
        resultat+=i
        resultat+=b[p]
        resultat+=c[p]
        resultat+=d[p]+"\n"
        p+=1
    print(resultat)
    resultat=""
    p=0
    e=aleascii(random.randint(0,4))
    if e[0]=='''          ..                  ''':
        variablee=symbole(1.5,5,"trefle",None)
    elif e[0]=='''               -:               ''':
        variablee=symbole(1,5,"citron",None)
    elif e[0]=='''                        :.    ''':
        variablee=symbole(1,7.5,"cloche",None)
    elif e[0]=='''                                 ''':
        variablee=symbole(1.75,10,"diamand",None)
    elif e[0]=='''  @++++++++++++++++++++*@:''':
        variablee=symbole(2,15,"sept",None)
    f=aleascii(random.randint(0,4))
    if f[0]=='''          ..                  ''':
        variablef=symbole(1.5,5,"trefle",None)
    elif f[0]=='''               -:               ''':
        variablef=symbole(1,5,"citron",None)
    elif f[0]=='''                        :.    ''':
        variablef=symbole(1,7.5,"cloche",None)
    elif f[0]=='''                                 ''':
        variablef=symbole(1.75,10,"diamand",None)
    elif f[0]=='''  @++++++++++++++++++++*@:''':
        variablef=symbole(2,15,"sept",None)
    g=aleascii(random.randint(0,4))
    if g[0]=='''          ..                  ''':
        variableg=symbole(1.5,5,"trefle",None)
    elif g[0]=='''               -:               ''':
        variableg=symbole(1,5,"citron",None)
    elif g[0]=='''                        :.    ''':
        variableg=symbole(1,7.5,"cloche",None)
    elif g[0]=='''                                 ''':
        variableg=symbole(1.75,10,"diamand",None)
    elif g[0]=='''  @++++++++++++++++++++*@:''':
        variableg=symbole(2,15,"sept",None)
    h=aleascii(random.randint(0,4))
    if h[0]=='''          ..                  ''':
        variableh=symbole(1.5,5,"trefle",None)
    elif h[0]=='''               -:               ''':
        variableh=symbole(1,5,"citron",None)
    elif h[0]=='''                        :.    ''':
        variableh=symbole(1,7.5,"cloche",None)
    elif h[0]=='''                                 ''':
        variableh=symbole(1.75,10,"diamand",None)
    elif h[0]=='''  @++++++++++++++++++++*@:''':
        variableh=symbole(2,15,"sept",None)
    for i in e:
        resultat+=i
        resultat+=f[p]
        resultat+=g[p]
        resultat+=h[p]+"\n"
        p+=1
    print(resultat)
    resultat=""
    p=0
    j=aleascii(random.randint(0,4))
    if j[0]=='''          ..                  ''':
        variablej=symbole(1.5,5,"trefle",None)
    elif j[0]=='''               -:               ''':
        variablej=symbole(1,5,"citron",None)
    elif j[0]=='''                        :.    ''':
        variablej=symbole(1,7.5,"cloche",None)
    elif j[0]=='''                                 ''':
        variablej=symbole(1.75,10,"diamand",None)
    elif j[0]=='''  @++++++++++++++++++++*@:''':
        variablej=symbole(2,15,"sept",None)
    k=aleascii(random.randint(0,4))
    if k[0]=='''          ..                  ''':
        variablek=symbole(1.5,5,"trefle",None)
    elif k[0]=='''               -:               ''':
        variablek=symbole(1,5,"citron",None)
    elif k[0]=='''                        :.    ''':
        variablek=symbole(1,7.5,"cloche",None)
    elif k[0]=='''                                 ''':
        variablek=symbole(1.75,10,"diamand",None)
    elif k[0]=='''  @++++++++++++++++++++*@:''':
        variablek=symbole(2,15,"sept",None)
    l=aleascii(random.randint(0,4))
    if l[0]=='''          ..                  ''':
        variablel=symbole(1.5,5,"trefle",None)
    elif l[0]=='''               -:               ''':
        variablel=symbole(1,5,"citron",None)
    elif l[0]=='''                        :.    ''':
        variablel=symbole(1,7.5,"cloche",None)
    elif l[0]=='''                                 ''':
        variablel=symbole(1.75,10,"diamand",None)
    elif l[0]=='''  @++++++++++++++++++++*@:''':
        variablel=symbole(2,15,"sept",None)
    m=aleascii(random.randint(0,4))
    if m[0]=='''          ..                  ''':
        variablem=symbole(1.5,5,"trefle",None)
    elif m[0]=='''               -:               ''':
        variablem=symbole(1,5,"citron",None)
    elif m[0]=='''                        :.    ''':
        variablem=symbole(1,7.5,"cloche",None)
    elif m[0]=='''                                 ''':
        variablem=symbole(1.75,10,"diamand",None)
    elif m[0]=='''  @++++++++++++++++++++*@:''':
        variable=symbole(2,15,"sept",None)
    for i in j:
        resultat+=i
        resultat+=k[p]
        resultat+=l[p]
        resultat+=m[p]+"\n"
        p+=1
    print(resultat)
    if a==f and f==l:
        somme += variablea.get_valeur * variablea.get_multiplicateur
    elif b==g and g==m:
        somme += variableb.get_valeur * variableb.get_multiplicateur
    elif d==g and g==k:
        somme += variabled.get_valeur * variabled.get_multiplicateur
    elif c==f and f==j:
        somme += variablec.get_valeur * variablec.get_multiplicateur
    elif a==e and e==j:
        somme += variablea.get_valeur * variablea.get_multiplicateur
    elif b==f and f==k:
        somme += variablea.get_valeur * variablea.get_multiplicateur
    elif c==g and g==l:
        somme += variablea.get_valeur * variablea.get_multiplicateur
    elif d==h and h==m:
        somme += variablea.get_valeur * variablea.get_multiplicateur
    elif a==b and b==c and c==d:
        somme += variablea.get_valeur * variablea.get_multiplicateur * 1.5
    elif e==f and f==g and g==h:
        somme += variablee.get_valeur * variablee.get_multiplicateur * 1.5
    elif j==k and k==l and l==m:
        somme += variablej.get_valeur * variablej.get_multiplicateur * 1.5
    elif b==c and c==d and d==e:
        if e==k and k==l and l==m:
            somme += variableb.get_valeur * variableb.get_multiplicateur*3
    elif a==b and b==c and c==h:
        if h==j and j==k and k==l:
                somme += variablea.get_valeur * variablea.get_multiplicateur*3
    elif a==b and b==c and c==d:
        if d==e and e==f and f==h:
            if h==j and j==k and k==l:
                if l==m:
                    somme += variablea.get_valeur * variablea.get_multiplicateur*1000
    print()
    print_ascii(somme,dette*1,5)
somme=0
dette=100
print_ascii(somme,dette)