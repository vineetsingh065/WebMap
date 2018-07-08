# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 11:50:50 2018

@author: Vineet
"""

import numpy as np
import folium #used for webmaps
import pandas as pd

dataset = pd.read_csv("Volcanoes_USA.txt") #importing dataset
latitude = list(dataset["LAT"]) #getting selected columns from dataset
longitude = list(dataset["LON"]) #getting selected columns from dataset
elevation = list(dataset["ELEV"]) #getting selected columns from dataset

def color_formatter(ele):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6)#, tiles="Mapbox Bright")
fgroup = folium.FeatureGroup(name="webmap")
fgroup_Population = folium.FeatureGroup(name="Population")

for lat, lan, elevation in zip(latitude, longitude, elevation):
    fgroup.add_child(folium.CircleMarker(location=[lat, lan], radius = 6, popup=str(elevation)+" m",
    fill_color=color_formatter(elevation), fill=True,  color = 'grey', fill_opacity=0.7))
    
fgroup_Population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'black'}))
    
map.add_child(fgroup_Population)
map.add_child(fgroup)
map.add_child(folium.LayerControl())

map.save("Webmap.html") #map file saved in html format  