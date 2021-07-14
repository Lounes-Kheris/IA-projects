# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 01:54:03 2021

@author: Lounes-Kheris
"""

import projet_1 as p1

#quand le module à importer comporte beaucoup de fonction, on peut choisir la seule chose à importe, pour cela

# from projet_1 import fibonnaci
# from projet_1 import * : importer tout

print(p1.fibonacci(5))

import math
import random 
import statistics
import os
import glob


#----------------------------
# Math
#----------------------------
print(math.cos(math.pi))
print(math.exp(5))


#---------------------------
# statistics
#---------------------------

liste = [4, 5, 77, 9, -91, 53, 18, -2, 16]

print(statistics.mean(liste))
print(statistics.variance(liste))


#---------------------------
#  random
#---------------------------

print(random.choice(liste))
random.seed(0)  #aléatoire mais la meme valeur a chaque fois
print(random.choice(['lounes', 'mehdi', 'anis']))

print(random.random())
print(random.randint(5, 10))
print(random.randrange(100))

print(random.sample(range(100), 10)) 
print(random.sample(range(100), random.randrange(10)))

print(random.shuffle(liste))



#-----------------------------------
#  OS
#-----------------------------------

print(os.getcwd())

#-----------------------------------
# glob
#-------------------------------
filenames = glob.glob("*.txt")

for file in filenames:
    with open(file, 'r') as  f:
         print(f.read())
         

#ouvrir les fichier txt et enregister leurs contenu

filenames = glob.glob("*.txt")

d = {}
for file in filenames:
    with open(file, 'r') as f:
        d[file] = f.read().splitlines()
    
print(d)
    
              