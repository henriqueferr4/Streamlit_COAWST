import streamlit as st
from datetime import datetime, timedelta #Data automatizada


# Carregando estilos CSS 
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# Identificar a data selecionada em 4_Historico.py
# PLotar o frames do diretório hist/data_selecionada(AAAAMMDD)