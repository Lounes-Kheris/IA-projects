# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:00:09 2021

@author: Lounes-Kheris
"""

# l'element le plus important : NDarray
# la fonction la plus importante est shape
    #retourne un tuple qui est les dimensions du tableau
# shape est immutable et protégé


import numpy as np

# array : constructor
tab = np.array([1,2,3]) #1 dimension

print(tab.shape)

tab1 = np.zeros((3,2)) #initialiser un tab 2dim avec des zeros
print(tab1.shape)

tab2 = np.ones((3,4))
print(tab2.size)

tab3 = np.full((3,4), 9)

# ---------------------

np.random.seed(0)
tab4 = np.random.randn(3, 4)
print(tab4)

print(np.eye(4)) #matrice identité

#------------------------
# constructor linspace :  

print(np.linspace(0, 10, 20)) #avoir 20 points répartis equitablement 
#entre 0 et 10 

print(np.arange(0, 10, 2))

# on peut rajouter le dtype ...... voir la dacs


# -------- Operation sur les tableaux --------

A = np.zeros((3, 2))
B = np.ones((3, 2))

print(A)
print(B)

print(np.hstack((A, B)))
#ou
print(np.concatenate((A, B), axis=1))

print(np.vstack((A,B)))

C = np.vstack((A,B))
print(C.reshape((3, 4)))


D = np.array([1, 2, 3])
D = D.reshape((D.shape[0], 1))
print(D.shape)
