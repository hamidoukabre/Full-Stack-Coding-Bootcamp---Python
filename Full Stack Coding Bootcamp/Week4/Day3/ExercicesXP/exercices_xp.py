

#********************Exercices Days 3 ********************************
#          exercice 1

print("Exercice 1")
dictio = { }
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for i in range(len(keys)):
    dictio[keys[i]] = values[i]
print(dictio)
print("\n\n")
#***************************************************************


#          exercice 2
print("Exercice 2")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print(" la famille rick et beth payent : ",15 ,"$")
print(" la famille summer et morty  payent : ",10 ,"$")
familyfamily ={}
nom = input(" Entrer votre nom:")
while nom != "quitter":
    nom = input(" Entrer votre nom:")
    age = input(" Entrer votre age:")
    familyfamily[nom] = age
print(familyfamily)
print("\n\n")
#***************************************************************


#          exercice 4
print("Exercice 4")
dict1= {}
dict2= {}
dict3= {}
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
key= [ x for x in range(0,5)]
for i in range(len(key)):
    dict1[users[i]] = key[i]
for j in range(len(users)):
    dict2[key[j]] = users[j]
for i in sorted(dict1.keys()):
    print("%s: %s" % (i, dict1[i]))
print(dict1)
print(dict2)



