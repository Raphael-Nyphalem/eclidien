#code1.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pylab
import csv



def import_tableau_float_csv(filename):
    tableau_valeur=[]
    spreadsheet = csv.reader(open(filename, 'r'), delimiter=';')
    for row in spreadsheet: # List of columns
        result = []
        for elem in row:
            result.append(float(elem))
        tableau_valeur.append(result)
    return(tableau_valeur)

def tableau_de_mesure(filename):
    tableau_valeur_mesurer =import_tableau_float_csv(filename)

    y = range(len(tableau_valeur_mesurer)) # definition des y ( longeur de la barre)
    x = range(len(tableau_valeur_mesurer[0])) # definition des x (temps)np.linspace

    X, Y = np.meshgrid(x, y)    # grille
    print("X: ",X)
    print("Y: ",Y)
    Z = np.array(tableau_valeur_mesurer)                 # evaluation de f sur la grille
    print("Z: ",Z)

    fig = plt.figure('Graphique tableau de mesure')         # creation figure
    ax = plt.axes(projection='3d') # creation d'un systeme d'axe
    ax.plot_surface(X, Y, Z, color='red',edgecolor='none',
                ccount=1000,rcount=1000)
    ax.set_title('tableau de mesure');
    ax.set_xlabel('temps')
    ax.set_ylabel('longeur')
    ax.set_zlabel('temperature');
    ax.view_init(45, 45)
    #pylab.savefig('fig1.png') # sauvegarde de la figure
    plt.show() # pour faire apparaitre la figure
    return()

def Prédiction(nb_prediction,delta_T,filename):
    barre_base = import_tableau_float_csv(filename)
    x = range(0,nb_prediction,delta_T) #temps de la barre
    y = range(len(tableau_valeur_mesurer)) # longueur de la barre
    #alfa = delta_T * 0.0495 / delta x carré
    X, Y = np.meshgrid(x, y)
    tableau = []
    len_list_y=len(list(y))
    for a in range(nb_prediction):
        for b in y:
            if (b!=0 and b!=(len_list_y -1)):
                #calcul de prédiction
                tableau[b][a]=f_prediction(tableau[b-1][a-1],tableau[b][a-1],tableau[b+1][a-1])
            elif(b==0):
                # 0 degre car extremiter barre
                tableau[b][a]=0
            else:
                #0 degre car autre extremiter barre
                tableau[b][a]=0
    return()

def f_prediction(val_haut,val_centre,val_bas):
    val_prediction=val_bas+val_haut-val_centre
    return(val_prediction)




def main():
    tableau_de_mesure('mesuresPrecises.csv')

main()
    
