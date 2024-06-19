import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Prueboita", layout="wide")

# Introducción
with st.container():
    st.header("Hola, soy la prueba")
    st.title("Este es el título de la prueba")
    st.write("Esto es con write")
    st.write("Esto es con write también")
    st.write("[Saber más >](https://www.youtube.com/watch?v=mAhJ_mQEoO4)")

