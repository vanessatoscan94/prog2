from flask import Flask
import folium
import pandas as pd
from flask import render_template
from flask import request
from flask import redirect
import daten
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import FloatImage
from natsort import natsorted, ns
from operator import attrgetter
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px






app = Flask(__name__)




    

@app.route("/", methods=['GET', 'POST']) #Formular erstellen
def kilometer_speichern():                            #Einträge im Formularfeld Name und Kilometer werden im Json gespeichert
    if request.method == 'POST':
        kilometer = request.form['kilometer']
        nachname = request.form['nachname']
        nachname, kilometer = daten.kilometer_speichern(kilometer, nachname)
        
        return redirect('/ranking') #Wenn man auf den Button "Speichern" klickt, gelangt man auf die Seite mit dem Ranking

    return render_template("start1.html")



def data():     # Datenherkunft Barplot
                                                     
    data = daten.kilometer_laden() #Daten aus dem Json fürs Ranking werden für den Barplot verwendet

   
    data_df = pd.DataFrame.from_dict(data, orient="index")
    data_df=data_df.reset_index()  #Index entfernen, damit 0 nicht der erste Eintrag ist

    data_df.columns=["Kilometer", "Name"]

    data_df=data_df.sort_values(by=["Kilometer"], ascending = False) #Erzeugung aufsteigender Reihenfolge der Balken


    return data_df


def viz():  #Erstellung Diagramm
    data_df = data()

    fig = px.bar(
        data_df,
        x=data_df.Kilometer, y=data_df.Name,
        orientation='h',
        height=400, 
        width=800
    )

    fig.layout.template = 'plotly_white'



    
    div = plot(fig, output_type="div") #gibt Diagramm als String zurück, der für die Erstellung des Diagrammes erforderlich ist
   
    return div
    
@app.route('/ranking') #Erstellung Tabelle für Ranking
def ranking():
    kilometer = daten.kilometer_laden()
    sortiert=natsorted(kilometer.items()) #ermöglicht Sortierung der Werte "Kilometer"
    nummeriert=enumerate(sortiert,start = 1) #Erzeugung Nummierierung für die Spalte "Rang"
    div = viz()

    
    
    return render_template("ranking1.html", nummeriert=nummeriert,viz_div=div) #Anzeigen des Ranikngs und des Diagrammes im HTML ranking1.html



@app.route('/karte') #Anzeigen Karte
def index():
    folium_map = folium.Map(
        location=[46.8667, 8.2333], # Zentrierung der Karte auf den Mittelpunkt der Schweiz. Ortschaft Sachseln
        zoom_start=8,
        tiles= "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}", #Karten Design
        attr="Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
        
        )
    #Koordinaten in Pandas speichern
    data = pd.DataFrame({
              'lat':[47.390434, 47.330769, 47.385849, 47.486614, 47.559601, 46.947922, 46.806403, 46.20222, 47.04057, 46.84986, 47.36493, 47.05048, 46.99179, 46.95805, 46.89611, 47.42391, 47.69732, 47.02076, 47.20791, 47.55776, 46.19278, 46.88042, 46.22739, 46.51600, 47.17242, 47.36667],
              'lon':[8.045701, 9.41104, 9.27884, 7.733427, 7.588576, 7.444608, 7.153656, 6.14569, 9.06804, 9.53287, 7.34453, 8.30635, 6.931000, 8.36609, 8.24531, 9.37477, 8.63493, 8.65414, 7.53714, 8.89893, 9.01703, 8.64441, 7.35559, 6.63282, 8.51745, 8.55000],
              'name':["Aarau", "Appenzell", "Herisau", "Liestal", "Basel", "Bern", "Fribourg", "Genf", "Glarus", "Chur",  "Delsberg", "Luzern", "Neuenburg", "Stans", "Sarnen", "Sankt Gallen", "Schaffhausen", "Schwyz", "Solothurn", "Frauenfeld", "Bellinzona", "Altdorf", "Sion", "Lausanne", "Zug",  "Zurich"]
               }) #Koordinaten für Marker festlegen

               
                                  #Marker setzen
    for i in range(0,len(data)): 
          folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=folium.Popup(data.iloc[i]['name'], show=True, sticky=True), tooltip =data.iloc[i]["name"]) .add_to(folium_map) #Hoovereffekt der den Ortsnamen anzeigt und Marker der permanent ist
          
  


    
    folium_map.add_child(MeasureControl()) #Hinzufügen des Plugins, mit dem man die Strecke bemessen kann


   
    url = ('https://media.licdn.com/mpr/mpr/shrinknp_100_100/AAEAAQAAAAAAAAlgAAAAJGE3OTA4YTdlLTkzZjUtNDFjYy1iZThlLWQ5OTNkYzlhNzM4OQ.jpg')
    FloatImage(url, bottom=5, left=85).add_to(folium_map)

    
    folium_map.save('templates/map.html') #Erzeugung der Map als HTML-Datei, damit man sie mit einem iframe in die Seite einbinden kann
    return render_template('start1.html') #Anzeigen der Map auf der Startseite


@app.route('/map') #Erstellen approute für Map als HTML
def map():
    return render_template('map.html')




@app.route("/creators") #Erstellen approute für Seite Creators, damit man sie mit Jinja verlinken kann
def creators():

  return render_template("creators.html")







if __name__ == "__main__":
    app.run(debug=True, port=5000)



