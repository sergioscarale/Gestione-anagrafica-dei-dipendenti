import os
def es1():
    c=0
    nomeFile="prova.txt"
    brano="L'altro ieri\nson\no andato in\ns\n campagna\ncon i miei fratelli\ngiacomo\nantonio" 
    if(os.path.exists(nomeFile)):
        with open (nomeFile,"r") as mioFile:
            for linea in mioFile:
                c+=1
        print(f"ci sono {c} righe!")
    else:
        with open (nomeFile,"a")as mioFile:
            mioFile.write(brano)
            print("file creato!\nDigitare 1 per conteggiare le righe\n")

def es2():
    numero=[]
    nomeFile="tappe.txt"
    tappe="prima=100, seconda=200, terza=300"
    if(os.path.exists(nomeFile)):
        with open (nomeFile,"r") as mioFile:
            for linea in mioFile:
                split=linea.split(",")
                for parola in split:
                    chiave=parola.split("=")
                    numero.append(int(chiave[1]))
            print(f"media lunghezza: {(sum(numero)/len(numero)):.2f}")   
    else:
        with open (nomeFile,"a") as mioFile:
            mioFile.write(tappe)
            print("file creato!\n")

def es3():
    nomeFile="prova.txt"
    c=0
    if(os.path.exists(nomeFile)):
        with open(nomeFile,"w") as mioFile:
            numero=1
            while numero!="0":
                numero=input("numero:\n> ")
                if(numero!="0"):
                    mioFile.write(numero+" ")
        with open(nomeFile,"r") as mioFile:
            numeroRicerca=input("numero da ricercare:\n> ")
            splitMe=[]
            for linea in mioFile:
                splitMe.append(linea.split(" "))
            print(splitMe)
            for numero in str(splitMe):
                if numero in numeroRicerca:
                    c+=1
            print(f"il numero è presente {c} volte!")

def es4():
    nome_file = "studenti.txt"
    nome_file_output = "studenti_classi.txt"
    studenti = "Sergio Scarale,Davide Cocomazzi,Matteo De Bonis,Renato Bisceglia"

    with open(nome_file, "w") as mio_file:
        mio_file.write(studenti)

    with open(nome_file, "r") as mio_file:
        linee=mio_file.readline()
        lista_studenti=linee.split(",")

    with open(nome_file_output, "w") as file_output:
        for studente in lista_studenti:
            studente=studente.strip() 
            classe=input(f"Inserisci la classe per {studente}: ")
            file_output.write(f"{studente}, Classe: {classe}\n")

    print(f"Dati salvati nel file '{nome_file_output}'.")
    stampa_file(nome_file_output)

def es5():
    nome_file_nazioni = "nazioni.txt"
    nome_file_output = "nazioni_capitali.txt"

    nazioni = "Italia,Francia,Germania,Spagna"

    with open(nome_file_nazioni, "w") as file_nazioni:
        file_nazioni.write(nazioni)

    with open(nome_file_nazioni, "r") as file_nazioni:
        linee = file_nazioni.readline()
        lista_nazioni = linee.split(",")

    with open(nome_file_output, "w") as file_output:
        for nazione in lista_nazioni:
            nazione = nazione.strip()
            capitale = input(f"Inserisci la capitale di {nazione}: ")
            file_output.write(f"{nazione}, Capitale: {capitale}\n")

    print(f"Dati salvati nel file '{nome_file_output}'.")

    stampa_file(nome_file_output)

def stampa_file(nome_file_output):
    comando = f"notepad /p {nome_file_output}"
    os.system(comando)
    print(f"File '{nome_file_output}' inviato alla stampante.")

def es6():
    nomeFile="insegnanti.txt"
    insegnanti="Martella M.: TPSIT, Gravina A.: Italiano, P.M.Russo: Inglese, D'Addetta G.: Matematica"
    with open(nomeFile,"w")as mioFile:
        mioFile.write(insegnanti)

    with open(nomeFile, "r") as mioFile:
        contenuto=mioFile.read()
        print("Lista Insegnanti:")
        print(contenuto)

    ricercaInsegnante=input("Inserisci il nome dell'insegnante da cercare:\n> ")
    if ricercaInsegnante.lower() in contenuto.lower():
        print("Insegnante presente!")
    else:
        print("Insegnante non presente!")

def main():
    scelta=1
    while scelta!=0:
        print("1 - Conteggio righe")
        print("2 - Lunghezza media tappe")
        print("3 - Insieme numeri")
        print("4 - Studenti")
        print("5 - Nazioni")
        print("6 - Insegnanti")
        scelta=int(input("\n> "))
        match(scelta):
            case 1: es1()
            case 2: es2()
            case 3: es3()
            case 4: es4()
            case 5: es5()
            case 6: es6()


main()