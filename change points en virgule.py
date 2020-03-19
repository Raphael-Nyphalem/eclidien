import sys
import os


def SAVE_FILE_XML(save,filename):
    #ecrase le fichier "filename" pour le remplacer par "save"
    myFile=open(filename,"w")
    myFile.write(save)
    myFile.close()
    return()

def OPEN_FILE_XML(filename):
    #Lit le fichier selectionner "filename" et le renvois
    myFile=open(filename,"r")
    txt=myFile.read()
    myFile.close()
    return(txt)

filename = 'mesuresPrecises.csv'

file=OPEN_FILE_XML(filename)
file=file.replace(',','.')
SAVE_FILE_XML(file,filename)
