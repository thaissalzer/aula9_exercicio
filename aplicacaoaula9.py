import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
st.write(df)
