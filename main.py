# streamlit_app.py
import streamlit as st

# Título da página
st.title("Meu primeiro app com Streamlit")

# Entrada de texto
nome = st.text_input("Digite seu nome:")

# Slider numérico
idade = st.slider("Selecione sua idade:", 0, 100, 25)

# Botão de ação
if st.button("Enviar"):
    # Exibe mensagem personalizada
    st.write(f"Olá, {nome}! Você tem {idade} anos.")
