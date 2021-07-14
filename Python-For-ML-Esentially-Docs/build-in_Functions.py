#most important

x = -1
print(abs(x))

x = 3.14
print(round(x))


liste = [0, 5, 1, 14, 23]
print(min(liste))
print(max(liste))
print(sum(liste))
print(len(liste))
print(any(liste))
print(all(liste))

liste2 = [True, False, True, True]
print(any(liste2))
print(all(liste2))


x = 10
print(type(x))

print(str(x))
print(float(x))

y = '20'
print(int(y))


liste3 = [0, 61, 63, 243]
print(tuple(liste3))

inventaire = {
    "banane" : 5000,
    "pommes" : 2094,
    "pores"  : 41500
    }

print(list(inventaire.keys()))
print(list(inventaire.values()))

print(bin(15))
print(hex(15))
print(oct(15))


a = input('entrez un nombre : ')
print(a)
print(type(a))

a = int(a)
y = a + 15
print(y)


# la fonction format
#exemple : message = "la temperature est de 17 à paris"
#remplacer la temperature et ville dynamiquement

temp = 20
ville = 'paris'

#message = "la temperature est de 20 à paris"

#dynamiquement

message = "La temperature est de {} à {}". format(temp, ville)
print(message)

#◘autre maniére
message = f"La temperature est de {temp} à {ville}"
print(message)


#function OPEN()

f = open('fichier.txt', 'w')

f.write('Bonjour')
f.close()

f = open('fichier.txt', 'r')
print(f.read())

#dans la pratique: on ecrit plus
with open('fichier.txt', 'r') as f:
    print(f.read())


#practice : ecrire tout les nombre carrée de 1-10 dans un fichier

with open('fichier.txt', 'w') as f:
    for i in range(10):
      f.write("{}^2 => {}\n".format(i, i**2))


#practice 2: ecrire les ligne d'un fichier dans une liste
liste = []
with open('fichier.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        liste.append(line.strip())

print(liste)


#with liste comprehension 

liste1 = [line.strip() for line in open('fichier.txt', 'r')]    
print(liste1)
    












