dictionnaire_1 = {
        "chien" : "dog",
        "chat" : "cat",
        "cheval" : "horse",
        "oiseau" : "bird"
    }

inventaire = {
    "banane" : 5000,
    "pommes" : 2500,
    "peches" : 8000
    }

dictionnaire_3 = {
    "dict_1" : dictionnaire_1,
    "dict_2" : inventaire
    }


#impression
print(inventaire.values())
print(inventaire.keys())

#tailles
print(len(inventaire))

#ajout
inventaire["cerises"] = 11000
print(inventaire.values())

#cherche une val associée à une clée
print(inventaire.get("cerises",1)) 
#si y'en a pas, ca retourne la val 1 âr default


#fromkeys crée un dict à partir d'une liste par exemple
list_1 = ["paris", "lisbonne", "londre"]
inventaire.fromkeys(list_1, 'default')
#crée le dictionnaire avec valeur par default "defaut"


#"pop" permet de retirer une association d'un dict
#inventaire.pop("banane")  #banane est retirée
#la valeur de l'association retirée est enregistrée : par exemple
fruit_ex = inventaire.pop("banane")
print(fruit_ex)


#
for i in inventaire:
    print(i)

for i in inventaire.values():
    print(i)
    
for i,j in inventaire.items():
    print(i,j)



#practice
classeur = {
    "positif" : [],
    "negatif" : []
    }

def trier(classeur, nombre):
    if nombre>0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)

    return classeur



print(trier(classeur, 4))
print(trier(classeur, -1))

