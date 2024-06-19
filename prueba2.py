import pandas as pd
import streamlit as st
from PIL import Image

st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Grand Prix de Países Bajos")


st.text_input("¿Cuál es tu nombre?", key="name")
st.session_state.name

st.text('¡Hola '+st.session_state.name+' !') 
'Hola cómo estás? ',st.session_state.name

df = pd.read_csv('covid_africa.csv')

if st.checkbox('Mostrar dataframe'):
    df


option = st.selectbox(
    'Selecciona el pais: ',
     df['Country/Other'])

'Tu selección: ', option

df.loc[df['Country/Other'] == option]


st.line_chart(
    df,
    x = 'Total Cases',
    y = 'Country/Other'
)
