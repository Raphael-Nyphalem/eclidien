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



vecteur= np.array(import_tableau_float_csv('vecteur.csv'))
x = np.linspace(0, 199, 200)


coel_final =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
all_coef=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def sin_tot(all_coef):
	sin_0 = np.sin(np.pi/2*x*all_coef[0]/100)
	sin_1 = np.sin(np.pi*2/2*x*all_coef[1]/100)
	sin_2 = np.sin(np.pi*3/2*x*all_coef[2]/100)
	sin_3 = np.sin(np.pi*4/2*x*all_coef[3]/100)
	sin_4 = np.sin(np.pi*5/2*x*all_coef[4]/100)
	sin_5 = np.sin(np.pi*6/2*x*all_coef[5]/100)
	"""
	sin_6 = np.sin(np.pi*7/2*x*all_coef[6]/100)
	sin_7 = np.sin(np.pi*8/2*x*all_coef[7]/100)
	sin_8 = np.sin(np.pi*9/2*x*all_coef[8]/100)
	sin_9 = np.sin(np.pi*10/2*x*all_coef[9]/100)
	sin_10 = np.sin(np.pi*11/2*x*all_coef[10]/100)
	sin_11 = np.sin(np.pi*12/2*x*all_coef[11]/100)
	"""

	sin_tot=sin_0+sin_1+sin_2+sin_3+sin_4+sin_5#+sin_6+sin_7+sin_8+sin_9+sin_10+sin_11
	return(sin_tot)
"""

for i in range(1):
	#print("boucle for i in range(1):", i)
	#print(all_coef)
	for co in range(len(all_coef)):
		val_min= sin_tot(all_coef).dot(vecteur)
		print(val_min)
		for ran in range(0,400):
			all_coef[co]= (ran-200)/100.0
			val_cal = sin_tot(all_coef).dot(vecteur)

			if abs(val_min[0]) > abs(val_cal[0]):
				coel_final[co] = all_coef[co]
				val_min[0] = val_cal[0]
	all_coef[0]=coel_final[0]
	all_coef[1]=coel_final[1]
	all_coef[2]=coel_final[2]
	all_coef[3]=coel_final[3]
	all_coef[4]=coel_final[4]
	all_coef[5]=coel_final[5]
	"""
for co in range(len(all_coef)):
	val_min= sin_tot(all_coef).dot(vecteur)*0.01
	for ran in range(0,400):
		all_coef[co]= (ran-200)/100.0
		val_cal = sin_tot(all_coef).dot(vecteur)*0.01
		if abs(val_min[0]) > abs(val_cal[0]):
			coel_final[co] = all_coef[co]
			val_min[0] = val_cal[0]

print("coel_final",coel_final)
print("val_min",val_min)


sin_tot = sin_tot(coel_final)
plt.plot(x, vecteur,label="sortie")
plt.plot(x, sin_tot,label="sin")
plt.grid()
plt.show()
