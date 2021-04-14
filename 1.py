import folium

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[22.5122502,88.3875295],popup="Science City Kolkata  "))

map=folium.Map(location=[22.5122502,88.3875295],zoom_start=5)

map.add_child(fg)
map.save("test.html")