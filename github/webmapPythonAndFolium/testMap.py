import folium as fm
import pandas as pd
map=fm.Map(location=[52.804819, -6.144514],zoom_start=14, tiles="stamen terrain")

fg_ammenities=fm.FeatureGroup(name="ammenities")

#reading co ordinates and placing markers for a list
#coordinateList=[["My Shopping Center",[52.798478, -6.146480]],["Costa Coffee",[52.799023, -6.147821]]]
#for coordinate  in coordinateList:
#    fg.add_child(fm.Marker(location=coordinate[1], popup = coordinate[0],icon=fm.Icon(color="red")))

html = """<h4>Place information:</h4>
%s
"""
#reading co ordinates and placing markers for a list for type
coordinateList=pd.read_csv("Coordinates.txt",delimiter=",",names=["place Name","Latitude","Longitude","Type"],index_col=False)
for index,row  in coordinateList.iterrows():
    iframe = fm.IFrame(html=html % row["place Name"], width=200, height=100)
    if row["Type"].lower()=="retail":
        fg_ammenities.add_child(fm.Marker(location=[row["Latitude"],row["Longitude"]], popup = fm.Popup(iframe),icon=fm.Icon(color="orange")))
    elif row["Type"].lower()=="sport":
        fg_ammenities.add_child(fm.Marker(location=[row["Latitude"],row["Longitude"]], popup = fm.Popup(iframe),icon=fm.Icon(color="green")))
    elif row["Type"].lower()=="transport":
        fg_ammenities.add_child(fm.Marker(location=[row["Latitude"],row["Longitude"]], popup = fm.Popup(iframe),icon=fm.Icon(color="blue")))
    else:
        fg_ammenities.add_child(fm.Marker(location=[row["Latitude"],row["Longitude"]], popup = fm.Popup(iframe),icon=fm.Icon(color="red")))

# create a geoJSON object
fg_population=fm.FeatureGroup(name="population")
fg_population.add_child(fm.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005'] < 30000000 else 'red'}))

map.add_child(fg_ammenities)
map.add_child(fg_population)
map.add_child(fm.LayerControl())
map.save("testMap.html")
