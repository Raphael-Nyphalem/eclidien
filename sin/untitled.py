#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pylab

def import_tableau_float_csv(filename):
    tableau_valeur=[]
    spreadsheet = csv.reader(open(filename, 'r'), delimiter=';')
    for row in spreadsheet: # List of columns
        result = []
        for elem in row:
            result.append(float(elem))
        tableau_valeur.append(result)
    return(tableau_valeur)




precision = int(input("nombre de sinus: "))+1

vecteur= np.array(import_tableau_float_csv('vecteur.csv'))
x = np.array(range(200))
vec_sin=np.zeros( (1, 200) )
coef=np.zeros( (1, precision) )
k_v = np.array(range(1,precision))

sin_tot=np.zeros( (1, 200) )



for k in k_v:
	vec_sin[0][x]=np.sin(k*np.pi*x/200)
	coef[0][k]= vec_sin.dot(vecteur)*0.01

print(coef)





sin_tot=np.sin(coef[0][0]*0*np.pi/2*x/100)

for k in k_v:
	sin_tot[x]+=coef[0][k]*np.sin(k*np.pi/2*x/100)


plt.plot(x, vecteur,label="sortie")
plt.plot(x, sin_tot,label="sin")
plt.grid()
plt.show()
