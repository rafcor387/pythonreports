import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/rafcor387/pythonreports/main/covid_africa.csv')
    return df
df = load_data()
st.write(df)
