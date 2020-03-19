#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pylab


Tmax = 50000
dt_mesure=500



def import_tableau_float_csv(filename):
    tableau_valeur=[]
    spreadsheet = csv.reader(open(filename, 'r'), delimiter=';')
    for row in spreadsheet: # List of columns
        result = []
        for elem in row:
            result.append(float(elem))
        tableau_valeur.append(result)
    return(tableau_valeur)

def creer_matrice(n,p):
	M=[]
	for y in range(n):
		M.append([])
		for x in range(p):
			M[y].append([])
	return(M)

def Matrice_P(alfa):
	M=creer_matrice(200,200)

	for y in range(200) :
		for x in range(200):
			if x==y:
				M[y][x]=(-2*alfa+1)
				if x==0 or x==199:
					M[y][x]= (-1*alfa+1)
			elif( x==y-1 or x==y+1):
				M[y][x]=1*alfa
			else:
				M[y][x]=0	
	return(M)

def tab(matrice):
    shpeM=np.shape(matrice)
    y = range(shpeM[0]) # definition des y ( longeur de la barre)
    x = np.array(range(shpeM[1])) # definition des x (temps)np.linspace
    x= dt_mesure*x

    X, Y = np.meshgrid(x, y)    # grille
    Z = matrice                 # evaluation de f sur la grille


    fig = plt.figure('Graphique tableau de mesure')         # creation figure
    ax = plt.axes(projection='3d') # creation d'un systeme d'axe
    ax.plot_surface(X, Y, Z, color='red',edgecolor='none',ccount=500,rcount=500, cmap="Spectral")
    ax.set_title('tableau de mesure');
    ax.set_xlabel('temps')
    ax.set_ylabel('longeur')
    ax.set_zlabel('temperature');
    ax.view_init(45, 45)
    #pylab.savefig('fig1.png') # sauvegarde de la figure
    plt.show() # pour faire apparaitre la figure
    return()


def main():

	vecteur= import_tableau_float_csv('vecteur.csv')
	V=np.array(vecteur)
	"""	
	print("V:")
	print(V)
	"""

	alfa_0 =0.0495
	dt=1.0
	dx=1.0

	alfa = alfa_0 *dt *(1/dx)**2

	#création matrice P
	P=np.array(Matrice_P(alfa))

	M=V
	
	for i in range(Tmax):
		M1=P.dot(V)
		M1[0][0]=0.0
		M1[199][0]=0.0
		V=M1
		if i%dt_mesure ==0:
			M=np.insert(M,[np.shape(M)[1]], M1,axis=1)
	"""
	print(M)
	print(a)
	"""
	print("Tmax:",Tmax)
	print("dt_mesure: ",dt_mesure)
	print("M:",np.shape(M))

	tab(M)

main()

