import random
#********************Exercices Days 5 ********************************
#          exercice 1


def display_message():
    """A function that says hello"""
    print("Dans ce cours, nous apprenons les fonctions en python!!!")
display_message()


#          exercice 2
def favorite_book(title):
    print("Un de mes livres préférés est:" + title )
favorite_book('Alice au pays des merveilles')


#          exercice 3
def describe_city(city, country):
    print(city+ " is in " + country)
describe_city('ouaga','BF')



#          exercice 4

def getRandom(nombre):
    entier = random.randint(0, 100)
    if nombre == entier:
        print('bravo tu as gagner')
    else:
        print(" échec ")
    print(" Le nombre aleatoire generer est:",entier)
    print(" Votre nombre entrer est:", nombre)
getRandom(3)



#          exercice 5
print("exercices 5")
def make_shirt(size, text):

    print("The size of the shirt is " + size + "  and the text is  " + text)

make_shirt('25', 'texte')
