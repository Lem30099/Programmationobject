import random
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
    cloche=[
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
    diamond=[
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
    sept=[
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
        return diamond
    elif n==2:
        return citron
    elif n==3:
        return cloche
    elif n==4:
        return sept
def print_ascii():
    resultat=""
    p=0
    a=aleascii(random.randint(0,4))
    b=aleascii(random.randint(0,4))
    c=aleascii(random.randint(0,4))
    d=aleascii(random.randint(0,4))
    for i in (0,17):
        resultat+=a[p]
        resultat+=b[p]
        resultat+=c[p]
        resultat+=d[p]+"\n"
        p+=1
    print(resultat)
    resultat=""
    p=0
    e=aleascii(random.randint(0,4))
    f=aleascii(random.randint(0,4))
    g=aleascii(random.randint(0,4))
    h=aleascii(random.randint(0,4))
    for i in (0,17):
        resultat+=e[p]
        resultat+=f[p]
        resultat+=g[p]
        resultat+=h[p]+"\n"
        p+=1
    print(resultat)
    resultat=""
    p=0
    m=aleascii(random.randint(0,4))
    j=aleascii(random.randint(0,4))
    k=aleascii(random.randint(0,4))
    l=aleascii(random.randint(0,4))
    for i in (0,17):
        resultat+=j[p]
        resultat+=k[p]
        resultat+=l[p]
        resultat+=m[p]+"\n"
        p+=1
    print(resultat)
print_ascii()