#ceci est un commentaire seule ligne
"""ceci est un commentaire"""

nom_prenom = "Jean Dupont" 
age = 12
print(type(nom_prenom))

if age <= 10:
    print("Vous êtes un enfant.")
elif 10 < age <= 18:
    print("Vous êtes un adolescent.")
else :
    print("Vous êtes un adulte.")
entier=12
boolean=3>5
comlex=2+3j
chaine="Bonjour"
float_number=3.14

liste=[1, "deux", 3.0, [4,5]]

ex_tuple=(1,2.5)
ex_set={1,2,2,3,4,4,5,5}
var={}
print(type(var))
print(ex_set)
print(type(boolean))
a=5
b=2

print(a+b)
print(a**b)
chaine1="Bonjour"
chaine2=" le monde"
concat=chaine1 + chaine2
res=len(concat)
sous_chaine=concat[0:3]
print(concat)
print(res)
print(sous_chaine)
liste=[1,2,3]
liste.append(4)
liste2=[5,6]
liste_finale=liste + liste2
print(liste_finale[0])
dictionnaire={"nom": "Dupont", "prenom": "Jean", "age": 30}
print(dictionnaire["prenom"])
dictionnaire["classe"]="Terminale"
dictionnaire["age"]=70
print(dictionnaire)

for n in liste_finale:
    print(n*2)
c=0
while c<5:
    print(c)
    if c>3:
        break
    c+=1
def somme(a:int,b:int)->int:
    return a+b
print(somme(2,5))
print(somme("Bonjour ","le monde"))
#print(somme(1,"salut"))
def greeting(nom:str="X")->str:
    return f"Bonjour {nom}!"  
print(greeting("Alice"))
print(greeting())
nom=input("Entrez votre nom: ")
age=int(input("Entrez votre âge: "))
print(f"Bonjour {nom}, vous avez {age} ans.")

try:
    nombre=int(input("Entrez un nombre: "))
    res=nombre/0
    print(res)
except ValueError:
    print("Veuillez entrer un nombre valide.")
except ZeroDivisionError:
    print("Division par zéro impossible.")