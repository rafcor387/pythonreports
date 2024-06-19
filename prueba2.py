import pandas as pd
import streamlit as st

st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Covid en Africa")

df = pd.read_csv('covid_africa.csv')

if st.checkbox('Mostrar dataframe'):
    st.write(df)

option = st.selectbox(
    'Selecciona el país: ',
    df['Country/Other'])

'Tu selección: ', option

country_df = df.loc[df['Country/Other'] == option]

st.text('Gráfico de países vs total de muertes') 
st.line_chart(
    country_df['Total Deaths']
)

st.text('Gráfico de barras de muertes por país') 
st.bar_chart(
    df.groupby('Country/Other')['Total Deaths'].sum()
)
