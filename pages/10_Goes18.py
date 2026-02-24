import streamlit as st
from pathlib import Path
import re
import time
import pandas as pd

# Carregando estilos CSS 
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

st.markdown("<h1 class='titulo'>Imagens de satélite - GOES - Canal 18</h1>",
    unsafe_allow_html=True)

Goes18_dir = Path("/home/henrique/Documentos/CIEX/Streamlit_COAWST/plots/Goes18")

def hora_previsao(p):
    nums = re.findall(r"(\d+)h", p.name)
    if nums:
        return int(nums[-1])
    return -1  # coloca no início da ordenação

pngs = sorted(
    Goes18_dir.glob("*.png"),
    key=hora_previsao
)

col_esq, col_centro, col_dir = st.columns([1, 2, 1])

with col_centro:

    st.divider()
    
    if "idx" not in st.session_state:
        st.session_state.idx = 0

    if "playing" not in st.session_state:
        st.session_state.playing = False

    # -------------------------------
    # Botões
    # -------------------------------
    col1, col2, col3 = st.columns([1,4,1])

    with col1:
        
        label = "⏸ Pause" if st.session_state.playing else "▶️ Play"

        if st.button(label):
            st.session_state.playing = not st.session_state.playing

            

    with col2:
        st.session_state.idx = st.slider(
            "Passo de tempo:",
            0,
            len(pngs) - 1,
            st.session_state.idx
        )


    st.image(pngs[st.session_state.idx])


    if st.session_state.playing:
        time.sleep(0.8)  

        st.session_state.idx += 1
        if st.session_state.idx >= len(pngs):
            st.session_state.idx = 0  # volta para o início

        st.rerun()