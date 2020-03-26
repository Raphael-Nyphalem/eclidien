#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pylab
from pprint import pprint 

def import_tableau_float_csv(filename):
    tableau_valeur=[]
    spreadsheet = csv.reader(open(filename, 'r'), delimiter=';')
    for row in spreadsheet: # List of columns
        result = []
        for elem in row:
            result.append(float(elem))
        tableau_valeur.append(result)
    return(tableau_valeur)


def tab(matrice):
    shpeM=np.shape(matrice)
    y = range(shpeM[0]) # definition des y ( longeur de la barre)
    x = np.array(range(100)) # definition des x (temps)np.linspace
    #x= dt_mesure*x #echelle du temps

    X, Y = np.meshgrid(x, y)    # grille
    Z = matrice                 # evaluation de f sur la grille


    fig = plt.figure('Graphique tableau de mesure')         # creation figure
    ax = plt.axes(projection='3d') # creation d'un systeme d'axe
    ax.plot_surface(X, Y, Z, color='red',edgecolor='none',ccount=50,rcount=50, cmap="Spectral")
    ax.set_title('tableau de mesure');
    ax.set_xlabel('temps')
    ax.set_ylabel('longeur')
    ax.set_zlabel('temperature');
    ax.view_init(45, 45)
    #pylab.savefig('fig1.png') # sauvesin_tot[x]+=coef[0][k]*np.sin(k*np.pi/2*x/100)*np.exp(-alpha0*(np.pi/2*k)**2*t)garde de la figure

    plt.show() # pour faire apparaitre la figure
    return()




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


np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

alpha0 =0.0495
sin_tot=np.sin(coef[0][0]*0*np.pi/2*x/100)

t=float(input("t: "))
for k in k_v:
    sin_tot[x]+=coef[0][k]*np.sin(k*np.pi/2*x/100)*np.exp(-alpha0*(np.pi/2*k)**2*t)

print(sin_tot)

"""
M= vecteur
print(M)


for t in range(100):
    for k in k_v:
       sin_tot[x]+=coef[0][k]*np.sin(k*np.pi/2*x/100)*np.exp(-alpha0*(np.pi/2*k)**2*t)
    M=np.insert(M,[np.shape(M)[1]], sin_tot,axis=1)
    sin_tot=np.sin(0*x)


print(M)

#tab(M)
"""