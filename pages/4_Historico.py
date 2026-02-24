import streamlit as st
from datetime import datetime, timedelta #Data automatizada


# Carregando estilos CSS 
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

st.markdown("<h1 class='titulo'>Histórico de previsões</h1>",
    unsafe_allow_html=True)

st.divider()

st.write(
    "<p class='subtitulo_nota'>Selecione a data para visualizar o histórico</p>",
    unsafe_allow_html=True)
st.write("")
st.write("")

# Button Datas 

col1, col2, col3 = st.columns([1,4,1])
with col2:

    data_atual = datetime.now().date()
    cols = st.columns(3)

    # for sobre os 9 dias anteriores à data_atual
    datas = []
    for i in range(9, 0, -1):
        datas.append(data_atual - timedelta(days=i))
        
        for idx, data in enumerate(datas):
            label = data.strftime("%d/%m/%Y")
        
        with cols[idx % 3]:
            if st.button(label, key=f"data_{idx}"):
                st.session_state["data_selecionada"] = data.strftime("%Y%m%d")

    st.write("")
    st.write("")
    st.write(
        "<p class='subtitulo_nota'>Selecione a variável</p>",
        unsafe_allow_html=True)
    st.write("")
    st.write("")


    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌬️ Vento"):
            st.switch_page("pages/1_Vento.py")

    with col2:
        if st.button("🌧️ Chuva"):
            st.switch_page("pages/historico_chuva.py")

    with col3:
        if st.button("🌊 Ondas"):
            st.switch_page("pages/historico_ondas.py")