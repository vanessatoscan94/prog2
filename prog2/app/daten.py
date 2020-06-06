import json


def speichern(datei,  kilometer, nachname): #Funktion um Einträge aus dem Formular im Json zu speichern
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {} 

    datei_inhalt[nachname] = kilometer  #nachname ist Key, kilometer ist value im Dictionair datei_inhalt



    

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

def kilometer_speichern(kilometer,nachname): #Angaben der Variablen, die im Json gespeichert werden sollen
    datei_name = "ranking.json"
   
    speichern(datei_name, nachname, kilometer )
    return nachname, kilometer


def kilometer_laden():  #Anzeigen der gespeicherten Werte im Json
    datei_name = "ranking.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt






   

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)