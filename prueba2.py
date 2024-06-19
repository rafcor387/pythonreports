import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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


# Crear gráfico de torta con Matplotlib
fig, ax = plt.subplots()
ax.pie(total_cases_by_country, labels=total_cases_by_country.index, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# Mostrar el gráfico utilizando st.pyplot()
st.pyplot(fig)