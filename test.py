import streamlit as st

# Título e descrição em inglês
st.title("Welcome to the App")
st.write("The App can be used as a test")

# Input e seletores em inglês
nome_de_usuario = st.text_input("Username:")

# Traduzimos as opções de tema (Dark/Light/Colorful) e o texto do slider
tema = st.selectbox("Choose a theme for your test:", ["Dark", "Light", "Colorful"])
outro = st.select_slider("Choose your difficulty level: 5 - Great / 4 - Good / 3 - So-so / 1 - Bad", [1, 2, 3, 4, 5])    

# Mensagem de sucesso final toda em inglês
if nome_de_usuario:
    st.success(f"Welcome {nome_de_usuario}! You chose the {tema} theme. And your difficulty level is {outro}.")
