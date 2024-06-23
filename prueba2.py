import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from reporte1 import create_pdf
from reporte1 import create_pdf2

st.header('Reportes usando Python', divider='rainbow')
st.title("Resultados de análisis de discotecas")
df = pd.read_csv('datsetdisco.csv')
# Convierte la columna 'fechaHora' al tipo de dato de fecha y hora
df['fechaHora'] = pd.to_datetime(df['fechaHora'])
# Convierte la columna 'fecha' al tipo de dato de fecha
df['fecha'] = pd.to_datetime(df['fecha'])
# Campo de selección para elegir un mes
months = {
    'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4,
    'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8,
    'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
}
# Mostrar el dataframe completo
st.text('DATAFRAME DE DISCOTECA')
if st.checkbox('Mostrar dataframe'):
    st.write(df)
# Crear gráficos
figs = []

# Primer gráfico de reservas de un cliente en una discoteca por meses
st.text('1. RESERVAS DE CLIENTES EN UNA DISCOTECA POR MESES')
cliente7 = st.selectbox('Selecciona el cliente:', df['cliente'].unique())
selected_name44 = st.selectbox('Selecciona la discoteca:', df['discoteca'].unique())
filtered_data76 = df[(df['cliente'] == cliente7) & (df['discoteca'] == selected_name44)]
daily_counts45 = filtered_data76['fechaHora'].dt.month.value_counts().sort_index()
max_value = daily_counts45.max()
# Reindexar para asegurar que todos los meses estén presentes
month = np.arange(1, 13)  # Array con los números de los meses (1-12)
reser = np.arange(1, max_value + 1)
daily_counts45 = daily_counts45.reindex(month, fill_value=0)
# Crear un gráfico de barras usando Matplotlib
fig, ax = plt.subplots()
ax.bar(daily_counts45.index, daily_counts45.values)
ax.set_xticks(month)  # Asegurar que todos los meses se muestren en el eje x
ax.set_yticks(reser)  # Asegurar que todas las reservas se muestren en el eje y
ax.set_xlabel('Mes')
ax.set_ylabel('Número de reservas')
ax.set_title(f'Número de reservas realizadas por meses en {selected_name44} para {cliente7}')
st.pyplot(fig)
# Muestra el DataFrame filtrado (opcional)
if st.checkbox(f'Mostrar dataframe de reservas de {cliente7} en {selected_name44}'):
    st.write(filtered_data76)
# Guardar el gráfico en la lista de figuras para el PDF
figs.append(fig)

# Botón para generar y descargar el PDF
pdf_buffer = create_pdf(fig)
st.download_button(
    label="Generar y Descargar PDF Report1",
    data=pdf_buffer,
    file_name="report.pdf",
    mime="application/pdf"
)




# -------------------------------
# Primer gráfico de pie
# -------------------------------
st.text('2. REPORTE DE RESERVAS REALIZADAS EN UNA FECHA')
# Establece la fecha por defecto
default_date = datetime(2023, 1, 1)
# Campo de texto para filtrar por fecha con fecha por defecto
date_input = st.date_input('Selecciona una fecha:', default_date)
# Filtra los registros que coinciden con la fecha seleccionada
filtered_data = df[df['fechaHora'].dt.date == date_input]
# Calcula el total de registros para cada nombre
nombre_counts = filtered_data['discoteca'].value_counts()

# Crear una figura y ejes
fig1, ax = plt.subplots()

# Generar el gráfico de pastel
wedges, texts, autotexts = ax.pie(
    nombre_counts, labels=nombre_counts.index, autopct='%1.1f%%', startangle=90)

# Colocar la leyenda debajo del gráfico
ax.legend(
    wedges, [f'{name}: {count} reservas' for name, count in nombre_counts.items()],
    title='Discotecas', loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

# Ajustar el tamaño del gráfico de pastel
ax.axis('equal')
ax.set_title(f'Distribución de reservas realizadas por fecha seleccionada: {date_input}')

# Muestra el gráfico de pastel
st.pyplot(fig)

# Muestra el número total de filas
st.write(f'Total de reservas para la fecha {date_input}: {len(filtered_data)}')

# Guardar el gráfico en la lista de figuras para el PDF
figs.append(fig1)
# Botón para generar y descargar el PDF
pdf_buffer1 = create_pdf2(fig1)
st.download_button(
    label="Generar y Descargar Report2",
    data=pdf_buffer1,
    file_name="report2.pdf",
    mime="application/pdf"
)



# -------------------------------
# Segundo gráfico de líneas
# -------------------------------
st.text('REPORTE DE RESERVAS REALIZADAS EN UNA FECHA')
selected_month = st.selectbox('Selecciona un mes:', list(months.keys()), key='month_select_145')
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
ax.plot(daily_counts.index, daily_counts.values)
ax.set_xlabel('Día del mes')
ax.set_ylabel('Número de reservas')
ax.set_title(f'Número de reservas realizadas por dia en {selected_month} para {selected_name}')
# Muestra el gráfico de líneas
st.pyplot(fig)
# Muestra el DataFrame filtrado (opcional)
if st.checkbox('Mostrar dataframe de reservas realizadas en una fecha'):
    st.write(filtered_data)




#clientes por nummesa
# Obtener los nombres únicos de los clientes, meses y discotecas
clientes = df['cliente'].unique()
meses = df['fecha'].dt.month_name().unique()
discotecas = df['discoteca'].unique()
# Selección de usuario
selected_cliente = st.selectbox('Selecciona un cliente:', clientes)
selected_mes = st.selectbox('Selecciona un mes:', meses)
selected_discoteca = st.selectbox('Selecciona una discoteca:', discotecas)
# Filtrar los datos según las selecciones del usuario
filtered_data0 = df[(df['cliente'] == selected_cliente) & 
                   (df['fecha'].dt.month_name() == selected_mes) & 
                   (df['discoteca'] == selected_discoteca)]

# Contar el número de filas para cada valor único de numMesa
bar_data = filtered_data0['numMesa'].value_counts().sort_index()
# Crear el gráfico de barras
fig, ax = plt.subplots()
ax.bar(bar_data.index, bar_data.values)  # Usamos bar_data en lugar de daily_counts
ax.set_xlabel('Número de Mesa')  # Cambiamos el texto del eje x
ax.set_ylabel('Número de reservas')  # Cambiamos el texto del eje y
ax.set_title(f'Número de reservas para el cliente {selected_cliente}, mes {selected_mes} en {selected_discoteca}')  # Ajustamos el título
ax.set_ylim(bottom=0, top=bar_data.max() + 1)  # Establecemos los límites del eje y como enteros
# Muestra el gráfico de barras
st.pyplot(fig)




#violin
selected_month9 = st.selectbox('Selecciona un mes:', list(months.keys()), key='month_select_9')
# Filtra los registros que coinciden con el mes seleccionado
month_num9 = months[selected_month9]
filtered_data9 = df[df['fecha'].dt.month == month_num9]
# Crear un gráfico de violín del número de reservas por discoteca
fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(data=filtered_data9, x='discoteca', y='idMesa', ax=ax)
ax.set_title(f'Distribución de reservas por discoteca en {selected_month9}')
ax.set_xlabel('Discoteca')
ax.set_ylabel('Número de reservas (idMesa)')
# Mostrar el gráfico de violín en Streamlit
st.pyplot(fig)
















#boxplot
selected_month5 = st.selectbox('Selecciona un mes:', list(months.keys()), key='month_select_6')
# Filtra los registros que coinciden con el mes seleccionado
month_num5 = months[selected_month5]
filtered_data5 = df[df['fecha'].dt.month == month_num5]
# Crear un boxplot de las reservas diarias por discoteca para el mes seleccionado
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_data5, x='discoteca', y='idMesa', ax=ax)
ax.set_title(f'Boxplot de reservas por día y discoteca en {selected_month5}')
ax.set_xlabel('Discoteca')
ax.set_ylabel('Número de reservas')
# Mostrar el boxplot en Streamlit
st.pyplot(fig)



# -------------------------------
# Tercero gráfico de barras
# -------------------------------
st.text('REPORTE DE RESERVAS CANCELADAS')
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
ax.set_ylabel('Número de reservas canceladas')
ax.set_title(f'Número de reservas canceladas por día en {selected_month1} para {selected_name1}')
# Muestra el gráfico de barras
st.pyplot(fig)
# Muestra el DataFrame filtrado (opcional)
if st.checkbox('Mostrar dataframe de reservas canceladas'):
    st.write(filtered_data_cancelled)



# -------------------------------
# Cuarto gráfico de histogramas
# -------------------------------
st.text('REPORTE DE FECHAS RESERVADAS')
# Campo de selección para elegir un mes
selected_month2 = st.selectbox('Selecciona un mes para fechas reservadas:', list(months.keys()), key='month_select_3')
# Campo de selección para elegir una discoteca
selected_name2 = st.selectbox('Selecciona la discoteca:', names, key='name_select_3')
# Filtra los registros que coinciden con el mes y nombre seleccionados
month_num2 = months[selected_month2]
filtered_data_reserved = df[(df['fecha'].dt.month == month_num2) & 
                             (df['discoteca'] == selected_name2)]
# Extrae los días del mes de las fechas filtradas
days_reserved = filtered_data_reserved['fecha'].dt.day
# Crea un histograma usando Matplotlib
fig, ax = plt.subplots()
ax.hist(days_reserved, bins=range(1, 32), edgecolor='black')
ax.set_xlabel('Día del mes')
ax.set_ylabel('Número de reservas para el día')
ax.set_title(f'Número de fechas reservadas por día en {selected_month2} para {selected_name2}')
# Muestra el histograma
st.pyplot(fig)
# Muestra el DataFrame filtrado (opcional)
if st.checkbox('Mostrar dataframe de reporte de fechas reservadas'):
    st.write(filtered_data_reserved)




# -------------------------------
# Quinto gráfico de Headmap
# -------------------------------
selected_month3 = st.selectbox('Selecciona un mes:', list(months.keys()), key='month_select_4')
# Filtra los registros que coinciden con el mes seleccionado
month_num3 = months[selected_month3]
filtered_data3 = df[df['fechaHora'].dt.month == month_num3]
# Crear una tabla de conteo de reservas por día y discoteca
heatmap_data = filtered_data3.pivot_table(index=filtered_data3['fecha'].dt.day, columns='discoteca', aggfunc='size', fill_value=0)
# Crear el heatmap usando Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap='YlGnBu', ax=ax)
ax.set_title(f'Reservas diarias por discoteca en {selected_month3}')
ax.set_xlabel('Discoteca')
ax.set_ylabel('Día del mes')
# Mostrar el heatmap en Streamlit
st.pyplot(fig)