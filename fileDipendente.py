def splitNomeCognome(anagrafica):
    """if len(splitto)<2:
        raise ValueError("Inserire sia il nome che il cognome.")"""
    splitto=anagrafica.split(" ")
    return splitto[0],splitto[1]

def creazioneDipendente():
    anagrafica=input("Nome e cognome: ")
    nome,cognome=splitNomeCognome(anagrafica)
    stipendio=input("Stipendio: ")
    print("\n")
    return (nome,cognome,stipendio)

if __name__=="__main__":
    creazioneDipendente()