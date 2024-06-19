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


st.text('Gráfico de lineas') 
# Opciones para el segundo selectbox (columna)
column_options = [
    'Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases',
    'Tot Cases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population'
]
# Widget de selección para la columna
selected_column = st.selectbox('Selecciona una columna:', column_options)
# Generar el gráfico de línea
st.text(f'Gráfico de {selected_column} para todos los países')
st.line_chart(df.set_index('Country/Other')[selected_column])




# Generar el gráfico de barras
st.text('Gráfico de barras') 
# Opciones para el segundo selectbox (columna)
column_options2 = [
    'Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases',
    'Tot Cases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population'
]
# Widget de selección para la columna
selected_column2 = st.selectbox('Selecciona una columna:', column_options2)
st.bar_chart(df.set_index('Country/Other')[selected_column2])














st.text('Mapa de los países') 
st.map(df[['latitude', 'longitude']])



# Seleccionar los 10 países con más muertes
top_10_countries_by_deaths = df.nlargest(10, 'Total Deaths')
# Gráfico de torta de Total Cases por país para los 10 países con más muertes
total_cases_by_country = top_10_countries_by_deaths.set_index('Country/Other')['Total Cases']
# Crear gráfico de torta con Matplotlib
fig, ax = plt.subplots()
ax.pie(total_cases_by_country, labels=total_cases_by_country.index, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# Mostrar el gráfico utilizando st.pyplot()
st.pyplot(fig)





