import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv("tus_datos.csv")

# Widget para seleccionar pa
selected_country = st.selectbox("Selecciona un país", data["Country/Other"].unique())

# Widget para seleccionar tipo de reporte
selected_report = st.selectbox("Selecciona el tipo de reporte", ["Gráfico de barras", "Gráfico de pastel", "Correlación"])

# Filtrar los datos por el país seleccionado
country_data = data[data["Country/Other"] == selected_country]

# Generar el reporte seleccionado
if selected_report == "Gráfico de barras":
    st.bar_chart(country_data[["Total Cases", "Total Deaths", "Total Recovered"]])
elif selected_report == "Gráfico de pastel":
    st.pyplot(plt.pie(country_data["Total Cases"], labels=country_data["Country/Other"]))
elif selected_report == "Correlación":
    st.write(country_data.corr())
