from flask import Flask

import folium
import pandas as pd

from folium import plugins

from folium.plugins import MeasureControl

from folium.plugins import FloatImage





app = Flask(__name__)


@app.route('/')
def index():
    folium_map = folium.Map(
        location=[46.8667, 8.2333],
        zoom_start=8,
        tiles= "http://tile.stamen.com/toner/{z}/{x}/{y}.png", 
        attr="toner-bcg",
        

        )
    data = pd.DataFrame({
              'lat':[47.390434, 47.330769, 47.385849, 47.486614, 47.559601, 46.947922, 46.806403, 46.20222, 47.04057, 46.84986, 47.36493, 47.05048, 46.99179, 46.95805, 46.89611, 47.42391, 47.69732, 47.02076, 47.20791, 47.55776, 46.19278, 46.88042, 46.22739, 46.51600, 47.17242, 47.36667],
              'lon':[8.045701, 9.41104, 9.27884, 7.733427, 7.588576, 7.444608, 7.153656, 6.14569, 9.06804, 9.53287, 7.34453, 8.30635, 6.931000, 8.36609, 8.24531, 9.37477, 8.63493, 8.65414, 7.53714, 8.89893, 9.01703, 8.64441, 7.35559, 6.63282, 8.51745, 8.55000],
              'name':["Aarau", "Appenzell", "Herisau", "Liestal", "Basel", "Bern", "Fribourg", "Genf", "Glarus", "Chur",  "Delsberg", "Luzern", "Neuenburg", "Stans", "Sarnen", "Sankt Gallen", "Schaffhausen", "Schwyz", "Solothurn", "Frauenfeld", "Bellinzona", "Altdorf", "Sion", "Lausanne", "Zug",  "Zurich"]
               })

               

    for i in range(0,len(data)):
          folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=folium.Popup(data.iloc[i]['name'], show=True, sticky=True), tooltip =data.iloc[i]["name"]) .add_to(folium_map)
          
    

    
    

# Adds tool to the top right
    
    folium_map.add_child(MeasureControl())

# Fairly obvious I imagine - works best with transparent backgrounds
   
    url = ('https://media.licdn.com/mpr/mpr/shrinknp_100_100/AAEAAQAAAAAAAAlgAAAAJGE3OTA4YTdlLTkzZjUtNDFjYy1iZThlLWQ5OTNkYzlhNzM4OQ.jpg')
    FloatImage(url, bottom=5, left=85).add_to(folium_map)

    return folium_map._repr_html_()




if __name__ == '__main__':
    app.run(debug=True)



