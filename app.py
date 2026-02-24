import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

# Carregando estilos CSS 
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

st.set_page_config(
    page_title="COAWST CIEX",
    page_icon="assets/logo_icon.png",
    layout="wide"
)


col1, col2 = st.columns([0.8, 5])

with col1:
    
    st.image("assets/logo_ciex_v2.png", width=120)
    st.image("assets/logo_procosta.png", width=120)
   
with col2:


    st.markdown("""
    <div style="text-align: center; padding-left: 5%; padding-right: 15%;">

    <h1> Dashboard de Monitoramento COAWST </h1>

    <br>

    <p>
    Este painel apresenta visualizações e análises geradas a partir das simulações do modelo 
    <b>COAWST (Coupled Ocean–Atmosphere–Wave–Sediment Transport)</b>, 
    uma plataforma numérica acoplada utilizada para estudar a interação entre oceano e atmosfera.
    </p>

    <br>

    <p>
     O sistema integra diferentes componentes físicos, permitindo uma representação mais realista dos processos costeiros e oceânicos.
    </p>

    <br>

    <p>
     As previsões disponibilizadas neste dashboard possuem horizonte de <b>72 horas (3 dias)</b>, 
    contadas a partir da data atual de execução do modelo e atualizadas diariamente.
    </p>

    <br>

    <p>
    Além da previsão recorrente, o sistema mantém um <b>histórico das simulações geradas nos 9 dias anteriores</b>.
    </p>

    <br>

    <p>
    O dashboard também integra imagens do satélite <b>GOES (Geostationary Operational Environmental Satellite)</b>, 
    em uma janela temporal de <b>1 hora</b> e atualizações a cada <b>10 minutos</b>.
    </p>

    </div>
    """, unsafe_allow_html=True)
st.divider()

st.markdown(
"<h1 class='titulo'>Previsão Operacional</h1>",
unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🌬 Velocidade e direção (Kt)",
        value="Vento",
        delta="Atualização diária"
    )
    if st.button("Toque para visualizar", key="vento"):
        st.switch_page("pages/1_Vento.py")

with col2:
    st.metric(
        label="🌧 Valor acumulado (mm)",
        value="Precipitação",
        delta="Atualização diária"
    )
    if st.button("Toque para visualizar", key="prec"):
        st.switch_page("pages/2_Precipitacao.py")

with col3:
    st.metric(
        label="🌊 Altura (m) e direção",
        value="Ondas",
        delta="Atualização diária"
    )
    if st.button("Toque para visualizar", key="ondas"):
        st.switch_page("pages/3_Ondas.py")

with col4:
    st.metric(
        label="🗂 Histórico",
        value="Previsões Anteriores",
        delta="-9 Dias",
        delta_color="off"

    )
    if st.button("Toque para visualizar", key="hist"):
        st.switch_page("pages/4_Historico.py")

st.divider()

st.markdown(
"<h1 class='titulo'>Imagens de satélite - GOES  </h1>",
unsafe_allow_html=True)

st.write("")
st.write("")


col1, col2, col3 = st.columns(3)

# 🔵 CANAL 02
with col1:
    st.metric(
        label="🛰 Canal 02",
        value="0.64 µm",
        delta="Visível",
        delta_color="yellow"
    )
    if st.button("Toque para visualizar", key="goes02"):
        st.switch_page("pages/8_Goes02.py")

# 🟣 CANAL 08
with col2:
    st.metric(
        label="🛰 Canal 08",
        value="6.2 µm",
        delta="Vapor d’água",
        delta_color="blue"
    )
    if st.button("Toque para visualizar", key="goes08"):
        st.switch_page("pages/9_Goes08.py")

# 🔴 CANAL 13 (corrigindo 18µm → 10.3 µm se for IR padrão)
with col3:
    st.metric(
        label="🛰 Canal 13",
        value="10.3 µm",
        delta="Infravermelho",
        delta_color="red"
    )
    if st.button("Toque para visualizar", key="goes13"):
        st.switch_page("pages/10_Goes18.py")

st.write("")
st.write("")
st.write("")
st.write("")

st.divider()

st.write(
    "<p class='subtitulo_nota'>Informações do sistema de modelagem COAWST (ROMS, WRF e SWAM) – Parcerias: projeto PROCOSTA – \
        Grupo META1 – Pesquisadores: Dr. William Duarte Jacondino; Dr. Luis Felipe Ferreira de Mendonça </p>",
    unsafe_allow_html=True)
st.caption("<p class='subtitulo_nota'>CIEX • Procosta • © 2026</p>", unsafe_allow_html=True)
