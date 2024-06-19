import pandas as pd
import streamlit as st
from PIL import Image

st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Grand Prix de Países Bajos")

image = Image.open('Verstappen-pole-lap-Zandvoort-Netherlands-2021.jpg')
st.image(image, caption='Max Verstappen')


st.text_input("¿Cuál es tu nombre?", key="name")
st.session_state.name

st.text('¡Hola '+st.session_state.name+' !') 
'Hola cómo estás? ',st.session_state.name

df = pd.read_csv('https://raw.githubusercontent.com/LilianaC/streamlit3/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv')

if st.checkbox('Mostrar dataframe'):
    df


option = st.selectbox(
    'Selecciona tu corredor favorito: ',
     df['DRIVER'])

'Tu selección: ', option

df.loc[df['DRIVER'] == option]


st.line_chart(
    df,
    x = 'AVG SPEED',
    y = 'LAP'
)
