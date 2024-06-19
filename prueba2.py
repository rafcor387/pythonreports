import streamlit as st
from PIL import Image

st.set_page_config(page_title="Prueboita",layout="wide")

#introsefs

with st.container():
    st.header("Hola, soy la prueba")
    st.title("este es el titulo de la prueba")
    st.write("esto es con write")
    st.write("esto es con write tambien")
    st.write("[saber mas >](https://www.youtube.com/watch?v=mAhJ_mQEoO4)")
