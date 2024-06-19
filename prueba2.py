import pandas as pd
import streamlit as st

st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Covid en Africa")

df = pd.read_csv('covid_africa.csv')

if st.checkbox('Mostrar dataframe'):
    st.write(df)

option = st.selectbox(
'Selecciona el pais: ',
df['Country/Other'])
'Tu selección: ', option
df.loc[df['Country/Other'] == option]


st.text('grafico de paises vs total de muertes')
st.line_chart(
df,
x = 'Country/Other',
y = 'Total Cases'
)

st.text('Gráfico de barras de muertes por país') 
st.bar_chart(
    df.groupby('Country/Other')['Total Deaths'].sum()
)

st.text('Mapa de los países') 
st.map(df[['latitude', 'longitude']])


st.text('Gráfico de torta de Total Cases por país') 
total_cases_by_country = df.groupby('Country/Other')['Total Cases'].sum()
st.pie_chart(total_cases_by_country)