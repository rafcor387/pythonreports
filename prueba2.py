import streamlit as st
from PIL import Image
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Prueboita",layout="wide")

#introsefs

with st.container():
    st.header("Hola, soy la prueba")
    st.title("este es el titulo de la prueba")
    st.write("esto es con write")
    st.write("esto es con write tambien")
    st.write("[saber mas >](https://www.youtube.com/watch?v=mAhJ_mQEoO4)")



# Leer el archivo naturalearth.land para obtener datos del mundo
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Crear un recorte para África
bbox_africa = [-20, -40, 60, 40]  # Borde de África (aproximado)

# Filtrar el mapa para África
africa = world.cx[bbox_africa[0]:bbox_africa[2], bbox_africa[1]:bbox_africa[3]]

# Leer los datos de los países africanos desde el archivo CSV
geo_data = pd.read_csv('/mnt/data/covid_africa.csv')

# Crear un GeoDataFrame a partir de los datos de latitud y longitud
gdf = gpd.GeoDataFrame(
    geo_data, geometry=gpd.points_from_xy(geo_data.longitude, geo_data.latitude))

# Configurar el sistema de coordenadas
gdf = gdf.set_crs(epsg=4326)

# Crear la figura y los ejes
fig, ax = plt.subplots(1, 1, figsize=(15, 15))

# Plotear el mapa de África
africa.plot(ax=ax, color='white', edgecolor='black')

# Agregar los puntos de los países
gdf.plot(ax=ax, color='red', markersize=10, label='Country')

# Agregar etiquetas de países
for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['Country/Other']):
    ax.text(x, y, label, fontsize=8, ha='right')

# Configurar la leyenda de forma horizontal
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5, frameon=False)

# Mostrar el mapa
plt.show()
