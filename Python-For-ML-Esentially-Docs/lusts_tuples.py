# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:10:00 2021

@author: Lounes-Kheris
"""

#listes

liste_1 = [1, 4, 2, 7, 35]
print(liste_1[1])
print(liste_1[-1]) #indexing : accéder au dernier élement
print(liste_1[-2]) #indexing : accéder à l'avant dernier élement

#slicing : liste[deb:fin:pas]
print(liste_1[0:3])
print(liste_1[:3]) #on ignore l'index 0 : inclue par defaut
print(liste_1[3:]) #jusqu'au dernier element
print(liste_1[1:4:2]) #pas de 2
print(liste_1[::2]) #deb->fin avec pas de 2
print(liste_1[::-1]) #inverser la seq



villes = ['paris', 'berlin', 'alger']
print(villes[2])
villes[0] = 'dublin' #modifier paris a dublin
print(villes[0])

liste_2 = [liste_1, villes] #list length 2  
liste_3 = [] #empty list

#tuples : une fois crées, on ne peut pas modifier

tuples_1 = (1, 2, 2, 8, 6)

#string

prenom = 'Nicolas'
print(prenom[:3])


#functions on liste

villes.append('Marseille') #adding in the end
villes.insert(2,'Madrid') #adding in the middle
villes_2 = ['londre', 'casablanca']
villes.extend(villes_2)
print(len(villes)) #taille de la liste

villes.sort() #ordonner la liste
villes.sort(reverse=True)#inverser la liste en l'ordonnant

villes.count('paris') #compter


#structure & lists

if 'alger' in villes : 
    print('oui')
else:
    print('non')
    

for i in villes:
    print(i)
    
for i in enumerate(villes):
    print(i)
    
for index, valeur in enumerate(villes):
    print(index, valeur)
    
#pour deux listes

for a, b in zip(villes, liste_1):
    print(a, b)
        