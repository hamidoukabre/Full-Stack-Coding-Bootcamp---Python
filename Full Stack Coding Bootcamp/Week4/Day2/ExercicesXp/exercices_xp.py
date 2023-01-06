

#********************ExercicesXp Days 2 ********************************

#          exercice 1

print("Exercice 1")
my_fav_numbers=[66106581, 78624879,79685231]
my_fav_numbers.append(72741568)
my_fav_numbers.append(55741568)
del my_fav_numbers[4]
friend_fav_numbers=[74165525,76585546,552689455,63258695]
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)
print("\n\n")

#***************************************************************


#          exercice 2
print("Exercice 2")
my_tuple = (1+3, 2.7, 'Thursday')
print(my_tuple)
print("Non, les luples sont comme des listes, mais elles sont immuables c'est a dire elles ne peuvent pas être modifiées ")
print("\n\n")
#***************************************************************


#          exercice 3
print("Exercice 3")
nombre_pommes=0
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
del basket[0]
basket.append("Kiwi")
basket.insert(-5, "Apple")
for i in basket:
     if i =='pommes':
         nombre_pommes=nombre_pommes+1
print(basket)
print("le nombre de pomme est:",nombre_pommes)
print("\n\n")
del basket
print("\n\n")


#***************************************************************
#          exercice 4
print("Exercice 4")
print("1) Le float est utilisé pour stocker des nombres à virgule flottante")
print("2) Un nombre entier est un nombre qui ne possède pas de décimales (chiffres après la virgule)" "\n"" tandis que Le float est utilisé pour stocker des nombres à virgule ")
list=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(list)
print("\n\n")



#***************************************************************
#          exercice 5
print("Exercice 5")
list1=[x for x in range(21)]
list2=[]
print("la liste")
print(list1)
for i in list1:
    if list1[i]%2==0:
        list2.append(list1[i])
print("la liste paire")
print(list2)
print("\n\n")
#***************************************************************


#          exercice 6
print("Exercice 6")
mon_nom="kabre hamidou"
name = input("donner votre nom et prenom")
while name != mon_nom:
    name = input("donner votre nom et prenom")
print("\n\n")
#***************************************************************


#          exercice 7
print("Exercice 7")
fruits = input("Entrer vos fruits préférés " "NB" "séparer les fruits avec un seul espace:")
liste_fruits=fruits.split()
print(liste_fruits)
fruits_prefere = input("Entrer un nom de n’importe quel fruit:")
if fruits_prefere in liste_fruits:
    print("Vous avez choisi l’un de vos fruits préférés! Profitez-en!")
else:
    print("Vous avez choisi un nouveau fruit. J’espère que vous apprécierez")
print("\n\n")
#***************************************************************


#          exercice 8
print("Exercice 8")
echap = "quitter"
list=[]
print(" si vous avez fini d'entrer, taper quitter ")
garnitures = input("entrer une série de garnitures de pizza.")
while garnitures != echap:
    garnitures = input("vous ajouterez cette garniture à votre pizza")
    list.append(garnitures)
print(" Votre liste de garnitures:",list)
print("\n\n")
#***************************************************************


#          exercice 9
print("Exercice 9")
age = int(input("Quel est votre age?"))
if age < 3:
    print("billet est gratuit  ")
elif age > 3 and age < 12:
    billet= 10
    print("billet coute",billet)
else:
    billet = 15
    print("billet coute", billet)
#***************************************************************


#          exercice 10
print("Exercice 10 ")
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches= []
for i in sandwich_orders:
    finished_sandwiches.append(i)
for j in finished_sandwiches:
    print("I made your tuna sandwich",j)

#***************************************************************


#          exercice 11
print("Exercice 11 ")
finished_sandwiches= []
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.append('Pastrami sandwich')
sandwich_orders.append('Pastrami sandwich')
print("la charcuterie est à court de pastrami")
for i in sandwich_orders:
    finished_sandwiches.append(i)
for j in finished_sandwiches:
    if j == "Pastrami sandwich":
        finished_sandwiches.remove('Pastrami sandwich')
print(finished_sandwiches)

#***************************************************************

