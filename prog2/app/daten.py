from datetime import datetime
import json


def speichern(datei, key, value, nachname):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key) + nachname] = value



    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def kilometer_speichern(kilometer,nachname):
    datei_name = "ranking.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, str(zeitpunkt), nachname, kilometer )
    return nachname, kilometer, str(zeitpunkt)


def kilometer_laden():
    datei_name = "ranking.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


