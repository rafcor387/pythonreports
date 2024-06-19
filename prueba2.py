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






# Opciones para el primer selectbox (país)
country_options = df['Country/Other'].unique()

# Opciones para el segundo selectbox (columna)
column_options = [
    'Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases',
    'Tot Cases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population'
]

# Opciones para el tercer selectbox (tipo de reporte)
report_type_options = ['line', 'pie']

# Widgets de selección
selected_country = st.selectbox('Selecciona un país:', country_options)
selected_column = st.selectbox('Selecciona una columna:', column_options)
selected_report_type = st.selectbox('Selecciona un tipo de reporte:', report_type_options)

# Filtrar el DataFrame por país seleccionado
country_df = df[df['Country/Other'] == selected_country]

# Generar el gráfico según el tipo de reporte seleccionado
if selected_report_type == 'line':
    st.line_chart(country_df[selected_column])
elif selected_report_type == 'pie':
    st.text(f'Gráfico de torta de {selected_column} para {selected_country}')
    st.text('No implementado todavía')  # Aquí puedes implementar el gráfico de torta usando Matplotlib o Plotly