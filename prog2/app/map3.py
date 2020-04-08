from flask import Flask

import folium

from folium import plugins

from folium.plugins import MeasureControl

from folium.plugins import FloatImage

app = Flask(__name__)


@app.route('/')
def index():
    folium_map = folium.Map(
        location=[46.8667, 8.2333],
        width=500, 
        height=500,
        zoom_start=6,
        tiles= "http://tile.stamen.com/toner/{z}/{x}/{y}.png", 
        attr="toner-bcg",
        

        )

    
   
    chur = folium.Marker(
        location=[46.849491, 9.530670],
        tooltip ='<strong> Chur </strong>',
        popup='<strong> Chur </strong>'
    
        ).add_to(folium_map)

    bern = folium.Marker(
        location=[46.947922, 7.444608],
        tooltip ='Bern',
        popup='Bern'

        ).add_to(folium_map)

    zurich = folium.Marker(
        location=[47.368650, 8.539183],
        tooltip ='Zurich', 
        popup=folium.Popup("<strong>Zurich</strong>", show=True, sticky=True)
        



        ).add_to(folium_map)

    
    

# Adds tool to the top right
    
    folium_map.add_child(MeasureControl())

# Fairly obvious I imagine - works best with transparent backgrounds
   
    url = ('https://media.licdn.com/mpr/mpr/shrinknp_100_100/AAEAAQAAAAAAAAlgAAAAJGE3OTA4YTdlLTkzZjUtNDFjYy1iZThlLWQ5OTNkYzlhNzM4OQ.jpg')
    FloatImage(url, bottom=5, left=85).add_to(folium_map)

    return folium_map._repr_html_()




if __name__ == '__main__':
    app.run(debug=True)



