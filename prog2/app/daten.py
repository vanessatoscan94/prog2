from datetime import datetime
import json


def speichern(datei,  kilometer, nachname):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[nachname] = kilometer  # wenn  datei_inhalt[str(key) + nachname] = value --> dann wird auch das Datum angezeigt



    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

def kilometer_speichern(kilometer,nachname):
    datei_name = "ranking.json"
   
    speichern(datei_name, nachname, kilometer )
    return nachname, kilometer


def kilometer_laden():
    datei_name = "ranking.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt






    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)