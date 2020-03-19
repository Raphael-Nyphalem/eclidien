import math
import csv
import numpy as np



def import_tableau_float_csv(filename):
    tableau_valeur=[]
    spreadsheet = csv.reader(open(filename, 'r'), delimiter=';')
    for row in spreadsheet: # List of columns
        result = []
        for elem in row:
            result.append(float(elem))
        tableau_valeur.append(result)
    return(tableau_valeur)

def matrice_identiter():
	M=[]
	for y in range(200):
		M.append([])
		for x in range(200):
			if x==y:
				M[y].append([1])
			else:
				M[y].append([0])
	return(M)

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

def multiplication_matrice(P200_200,V200_1):
	if (len(P200_200[0])==len(V200_1)):
		M=creer_matrice(200,1)
		for y_m in range(len(M)):
			resulta = 0.0
			for x_m in range(len(M[0])):
				for a in range(len(M)):
					resulta += float(P200_200[y_m][a])*float(V200_1[a][0])
				M[y_m][x_m] = resulta
	else:
		print ("Erreur matrice non multipliable")
	M[0][0]=0.0
	M[199][0]=0.0
	return(M)

def main():
	vecteur= import_tableau_float_csv('vecteur.csv')
	V=np.array(vecteur)	
	print(V)

	alfa_0 =0.0495
	dt=1.0
	dx=1.0

	alfa = alfa_0 *dt *(1/dx)**2

	P=Matrice_P(alfa)
	final = creer_matrice(199,2)
	final[0]=vecteur
	for i in range(51):
		M=multiplication_matrice(P,vecteur)
		vecteur = M
		if i%50 ==0:
			final[1]=M
			print(i)




	matrice=np.array(M)
	print(final)
	print(matrice)

	return()


main()

