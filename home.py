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
            mioFile.write(f"{lunghezzaFile(nomeFile)} {dipendente[0]} {dipendente[1]} {dipendente[2]}\n")
            print("file creato!\n")

def visualizzaRecord(nomeFile):
    if(os.path.exists(nomeFile)):
        with open(nomeFile,"r") as mioFile:
            for linea in mioFile:
                print(linea.strip())
    else:
        with open (nomeFile,"a") as mioFile:
            print("file creato!\n")

def gestisciArchivio(nomeFile):
    if not (os.path.exists(nomeFile)):
        open(nomeFile,"x")
        print("file creato!")
    else:
        print("file già creato!")

def modTutto(nomeFile):
    with open(nomeFile,"r") as mioFile:
        nome,cognome=splitNomeCognome(input("\nquale anagrafica vuoi cambiare?\n> "))
        righe=[]
        trovato=False
        for linea in mioFile:
            dati=linea.strip().split(" ")
            if(nome and cognome in linea):
                nome,cognome=splitNomeCognome(input("nome e cognome della nuova anagrafica\n> ").lower())
                stipendio=input("nuovo stipendio\n> ")
                nuovaRiga=(f"{dati[0]} {nome} {cognome} {stipendio}")
                righe.append(nuovaRiga+"\n")
                trovato=True
            else:
                righe.append(linea+"\n")
    if trovato:
        with open(nomeFile, "w") as mioFile:
            mioFile.writelines(righe)
        print("Anagrafica modificata con successo!")
    else:
        print("Anagrafica inesistente!")

def modAnagrafica(nomeFile):
    with open(nomeFile,"r") as mioFile:
        nome,cognome=splitNomeCognome(input("quale anagrafica vuoi modificare?\n> ").lower())
        righe=[]
        trovato=False
        for linea in mioFile:
            dati=linea.strip().split(" ")
            if(nome and cognome in linea):
                nome,cognome=splitNomeCognome(input("nuova anagrafica\n> "))
                nuovaRiga=(f"{dati[0]} {nome} {cognome} {dati[3]}")
                righe.append(nuovaRiga+"\n")
                trovato=True
            else:
                righe.append(linea+"\n")
    if trovato:
        with open(nomeFile, "w") as mioFile:
            mioFile.writelines(righe)
        print("Anagrafica modificata con successo!")
    else:
        print("Anagrafica inesistente!")

def modStipendio(nomeFile):
    with open(nomeFile,"r") as mioFile:
        trovato=False
        righe=[]
        nome,cognome=splitNomeCognome(input("stipendio dell'anagrafica da modificare\n> ").lower())
        for linea in mioFile:
            dati=linea.strip().split(" ")
            if(nome and cognome in linea):
                stipendio=input("nuovo stipendio\n> ")
                nuovaRiga=(f"{dati[0]} {nome} {cognome} {stipendio}")
                righe.append(nuovaRiga+"\n")
                trovato=True
            else:
                righe.append(linea+"\n")
    if trovato:
        with open(nomeFile,"w") as mioFile:
            mioFile.writelines(righe)
        print("Stipendio modificato con successo!")
    else:
        print("Anagrafica inesistente!")

def modificaRecord(nomeFile):
    scelta="1"
    if(os.path.exists(nomeFile)):
            while scelta!="0":
                print("\nquale campo vuoi modificare?\n0-Esci\n1-Anagrafica e stipendio\n2-Anagrafica\n3-Stipendio")
                scelta=input("\n> ")
                match scelta:
                    case "1": modTutto(nomeFile)
                    case "2": modAnagrafica(nomeFile)
                    case "3": modStipendio(nomeFile)
    else:
        with open (nomeFile,"a") as mioFile:
            print("file creato!\n")

def eliminaRecord(nomeFile):
    with open(nomeFile,"r") as mioFile:
        trovato=False
        righe=[]
        nome,cognome=splitNomeCognome(input("anagrafica da cancellare\n> ").lower())
        for linea in mioFile:
            dati=linea.strip().split(" ")
            if(nome and cognome in linea):
                trovato=True
                nuovaRiga=("")
                righe.append(nuovaRiga+"\n")
            else:
                righe.append(linea+"\n")
    if trovato:
        with open(nomeFile,"w") as mioFile:
            mioFile.writelines(righe) 
            print("record cancellato!")
    else:
        print("record inesistente!")

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
            case 3: gestisciArchivio(nomeFile)
            case 4: modificaRecord(nomeFile)
            case 5: eliminaRecord(nomeFile)

main()