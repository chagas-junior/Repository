import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

grafico = px.bar(df, x='Linguagem', y='Desenvolvedores', color='Linguagem')

st.plotly_chart(grafico)
