import pandas as pd
import streamlit as st
from PIL import Image

st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Covid en Africa")


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
    x = 'Country/Other',
    y = 'Total Cases'
)
