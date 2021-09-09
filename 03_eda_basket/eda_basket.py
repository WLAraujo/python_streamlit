import streamlit as st
import pandas as pd
import base64 # Biblioteca responsável por codificação https://docs.python.org/3/library/base64.html
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Título
st.title("Explorer de estatísticas de jogadores da NBA")

# Escreve texto reconhecendo o markdown
st.markdown("""
Esse app mostra informações estatísticas sobre o desempenho de jogadores da NBA.

* **Bibliotecas usadas:** streamlit, pandas, base64,   matplotlib, seaborn, numpy       
* **Fonte dos dados:** https://www.basketball-reference.com/

""")

# Criação da barra de seleção de parâmetros
st.sidebar.header("Filtros")

# Criação de uma caixa de seleção para o ano
ano = st.sidebar.selectbox("Ano", list(reversed(range(1950, 2020))))

# Realização de web scraping com base na página que estamos usando para coletar os dados
def carregar_dados(ano):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(ano) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
