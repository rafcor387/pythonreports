import pandas as pd
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

st.header('Gráficas utilizando Pandas y streamlit', divider='rainbow')
st.title("Resultados de analisis de discotecas")

df = pd.read_csv('datasetdisco.csv')

if st.checkbox('Mostrar dataframe'):
    st.write(df)


option = st.selectbox(
'Selecciona el cliente: ',
df['cliente'])
'Tu selección: ', option
df.loc[df['cliente'] == option]


#pa fecha 
# Convierte la columna 'fechaHora' al tipo de dato de fecha y hora
df['fechaHora'] = pd.to_datetime(df['fechaHora'])
# Establece la fecha por defecto
default_date = datetime(2023, 1, 1)
# Campo de texto para filtrar por fecha con fecha por defecto
date_input = st.date_input('Selecciona una fecha:', default_date)
# Filtra los registros que coinciden con la fecha seleccionada
filtered_data = df[df['fechaHora'].dt.date == date_input]
# Calcula el total de registros para cada nombre
nombre_counts = filtered_data['discoteca'].value_counts()
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    nombre_counts, labels=nombre_counts.index, autopct='%1.1f%%', startangle=90)
ax.legend(
    wedges, [f'{name}: {count} reservas' for name, count in nombre_counts.items()],
    title='Discotecas', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title(f'Distribución de reservas realizadas por fecha seleccionada: {date_input}')
# Muestra el gráfico de pastel
st.pyplot(fig)
# Muestra el número total de filas
st.write(f'Total de reservas para la fecha {date_input}: {len(filtered_data)}')
# Campo de selección para elegir entre Forum, Pacha, Zouk Boulevard
#selected_location = st.selectbox('Selecciona una ubicación:', ['Forum', 'Pacha', 'Zouk Boulevard'])




# -------------------------------
# Primer gráfico de líneas
# -------------------------------
# Campo de selección para elegir un mes
months = {
    'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4,
    'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8,
    'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
}
selected_month = st.selectbox('Selecciona un mes:', list(months.keys()), key='month_select_1')

# Campo de selección para elegir un nombre
names = df['discoteca'].unique()
selected_name = st.selectbox('Selecciona la discoteca:', names, key='name_select_1')

# Filtra los registros que coinciden con el mes y el nombre seleccionados
month_num = months[selected_month]
filtered_data = df[(df['fechaHora'].dt.month == month_num) & (df['discoteca'] == selected_name)]

# Cuenta el número de filas para cada día del mes
daily_counts = filtered_data['fechaHora'].dt.day.value_counts().sort_index()

# Crea un gráfico de líneas usando Matplotlib
fig, ax = plt.subplots()
#ax.plot(daily_counts.index, daily_counts.values, marker='o')
ax.bar(daily_counts.index, daily_counts.values)
ax.set_xlabel('Día del mes')
ax.set_ylabel('Número de filas')
ax.set_title(f'Número de filas por día en {selected_month} para {selected_name}')
# Muestra el gráfico de líneas
st.pyplot(fig)
# Muestra el DataFrame filtrado (opcional)
st.write(filtered_data)

# -------------------------------
# Segundo gráfico de barras
# -------------------------------
# Campo de selección para elegir un mes
selected_month1 = st.selectbox('Selecciona un mes para reservas canceladas:', list(months.keys()), key='month_select_2')

# Campo de selección para elegir una discoteca
selected_name1 = st.selectbox('Selecciona la discoteca para reservas canceladas:', names, key='name_select_2')

# Filtra los registros que coinciden con el mes, nombre seleccionados y estado "Cancelado"
month_num1 = months[selected_month1]
filtered_data_cancelled = df[(df['fechaHora'].dt.month == month_num1) & 
                             (df['discoteca'] == selected_name1) & 
                             (df['estado'] == 'Cancelado')]

# Cuenta el número de filas para cada día del mes
daily_counts_cancelled = filtered_data_cancelled['fechaHora'].dt.day.value_counts().sort_index()

# Crea un gráfico de barras usando Matplotlib
fig, ax = plt.subplots()
ax.bar(daily_counts_cancelled.index, daily_counts_cancelled.values)
ax.set_xlabel('Día del mes')
ax.set_ylabel('Número de filas canceladas')
ax.set_title(f'Número de reservas canceladas por día en {selected_month1} para {selected_name1}')
# Muestra el gráfico de barras
st.pyplot(fig)
# Muestra el DataFrame filtrado (opcional)
st.write(filtered_data_cancelled)