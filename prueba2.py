import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Covid en Africa")

df = pd.read_csv('prueba.csv')

if st.checkbox('Mostrar dataframe'):
    st.write(df)

option = st.selectbox(
'Selecciona el pais: ',
df['Country/Other'])
'Tu selección: ', option
df.loc[df['Country/Other'] == option]


# Gráfico de líneas
st.text('Gráfico de líneas') 
column_options = [
    'Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases',
    'Tot Cases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population'
]
selected_column = st.selectbox('Selecciona una columna para el gráfico de líneas:', column_options)
st.line_chart(df.set_index('Country/Other')[selected_column])



st.text('Gráfico de barras') 
selected_column2 = st.selectbox('Selecciona una columna para el gráfico de barras:', column_options)
st.bar_chart(df.set_index('Country/Other')[selected_column2])






# Campo de texto para filtrar por valor
filter_value = st.text_input('Escribe un valor para filtrar los países por debajo de él:', '')
column_options2 = [col for col in column_options if col != selected_column] 
selected_column3 = st.selectbox('Selecciona una columna para el gráfico de barras:', column_options2)
# Filtrar el DataFrame por el valor ingresado
if filter_value:
    filtered_df = df[df[selected_column3] <= float(filter_value)]

    # Mapa de los países filtrados
    st.text('Mapa de los países')
    st.map(filtered_df[['latitude', 'longitude']])

    st.text('Países con un valor igual o menor a {}:'.format(filter_value))
    st.write(filtered_df[['Country/Other', selected_column3]])


column_options3 = [col for col in column_options if col != selected_column and  col != selected_column2] 
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





