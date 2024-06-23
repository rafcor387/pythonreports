import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from reporte1 import create_pdf
import os

st.header('Gráficas utilizando Pandas y Streamlit', divider='rainbow')
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
pdf_buffer = create_pdf(figs)
st.download_button(
    label="Generar y Descargar PDF",
    data=pdf_buffer,
    file_name="report.pdf",
    mime="application/pdf"
)
