import os
import time
'''from amazon_city_builder import amazon_city_builder'''


def end():
        while True: 
            dragon=input("Accepter la quete (oui/non) ")
            if dragon.lower()=='non':
                dragon2=input('Tu est sur que tu veux pas (oui/non)?')
                if dragon2.lower=='oui':
                    print('Ok la mauviette bah va sur un autre monde looser')
                    time.sleep(5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('bonjour')
                    '''amazon_city_builder()'''
                    break
                elif dragon2.lower=='non':
                    print('ojoih')
                    break
            elif dragon.lower=='oui': 
                print('aurevoir')
                break

print("Maintenant, tu dois construire ta cité de L'End")
print("Pour ce faire tu vas devoir tuer l'Ender Dragon")
time.sleep(2)
end()

    

        