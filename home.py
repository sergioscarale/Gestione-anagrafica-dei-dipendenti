from fileDipendente import *; 
import os          

def lunghezzaFile(nomeFile):
    c=0
    with open(nomeFile,"r") as mioFile:
         c=len(mioFile.readlines())+1
    return c

def inserisciRecord(nomeFile):
    dipendente=creazioneDipendente()
    if(os.path.exists(nomeFile)):
        with open(nomeFile,"a") as mioFile:
            mioFile.write(f"{lunghezzaFile(nomeFile)} {dipendente[0]} {dipendente[1]} {dipendente[2]}\n")
    else:
        with open (nomeFile,"a") as mioFile:
            print("file creato!\n")

def visualizzaRecord(nomeFile):
    if(os.path.exists(nomeFile)):
        with open(nomeFile,"r") as mioFile:
            for linea in mioFile:
                print(linea.strip())
    else:
        with open (nomeFile,"a") as mioFile:
            print("file creato!\n")

def gestisciArchivio():
    print("ciao")

def modTutto(nomeFile):
    with open(nomeFile,"r") as mioFile:
        for linea in mioFile:
            linea.strip()


#def modAnagrafica():


#def modStipendio():


def modificaRecord(nomeFile):
    scelta="1"
    if(os.path.exists(nomeFile)):
            while scelta!="0":
                print("quale campo vuoi modificare?\n0-Esci\n1-Anagrafica e stipendio\n2-Anagrafica\n3-Stipendio")
                scelta=input("\n> ")
                match scelta:
                    case "1": modTutto(nomeFile)
                    #case "2": modAnagrafica()
                    #case "3": modStipendio()
    else:
        with open (nomeFile,"a") as mioFile:
            print("file creato!\n")

def eliminaRecord():
    print("ciao")

def main():
    nomeFile="anagrafe.txt"
    scelta=1
    while scelta!=0:
        print("0 - Esci")
        print("1 - Inserisci record")
        print("2 - Visualizza record")
        print("3 - Gestisci archivio")
        print("4 - Modifica record")
        print("5 - Elimina record")
        scelta=int(input("\n> "))
        match scelta:
            case 1: inserisciRecord(nomeFile)
            case 2: visualizzaRecord(nomeFile)
            case 3: gestisciArchivio()
            case 4: modificaRecord(nomeFile)
            case 5: eliminaRecord()

main()