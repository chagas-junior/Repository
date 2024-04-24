import streamlit as st
import pandas as pd

st.header("Hello world")

st.write()

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

st.dataframe(df)

lista_escolhas = df["Linguagem"].unique()

escolha = st.selectbox('Escolha uma alternativa',lista_escolhas)

botao = st.button("Clique para enviar")

if(botao):
    st.dataframe(df.loc[df["Linguagem"] == escolha])

