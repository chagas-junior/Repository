import streamlit as st
import pandas as pd

st.header("Hello world")

st.write()

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

st.dataframe(df)