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
    raw = raw.fillna(0)
    estatisticas = raw.drop(['Rk'], axis = 1)
    return estatisticas
estatisticas_jogadores = carregar_dados(ano)

# Seleção de times através da barra de parâmetros
times_ordenados = sorted(estatisticas_jogadores['Tm'].unique())
times_selecionados = st.sidebar.multiselect('Times', times_ordenados, times_ordenados)

# Seleção de posições através de barra de parâmetros
posicoes = sorted(estatisticas_jogadores['Pos'].unique())
pos_sel = st.sidebar.multiselect('Posições', posicoes, posicoes)

# Filtragem dos dados
df_times_pos = estatisticas_jogadores[(estatisticas_jogadores['Tm'].isin(times_selecionados)) & (estatisticas_jogadores['Pos'].isin(pos_sel))]

# Mudando os tipos de dados numéricos
lista_colunas = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
for coluna in lista_colunas:
    df_times_pos[coluna] = pd.to_numeric(df_times_pos[coluna])

# Display das informações
linhas = df_times_pos.shape
st.header('Informações de Jogadores dos Times e Posições Selecionadas')
st.write(f"""
A tabela tem {df_times_pos.shape[0]} **linhas** e {df_times_pos.shape[1]} **colunas**.
""")
st.dataframe(df_times_pos)

# Download dos dados
def download_dados(df):
    csv = df.to_csv(index = False)
    cod_b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href = "data:file/csv;base64,{cod_b64}" download = "estatisticas.csv"> Download CSV </a>'
    return href

st.markdown(download_dados(df_times_pos), unsafe_allow_html = True)
    
# Mostrando heatmap de correlação
if st.button("Heatmap de Intercorrelação"):
    st.header("Heatmap de Intercorrelação")
    df = pd.DataFrame
    df = df_times_pos.copy(deep = True)
    corr = df.corr()
    fig, ax = plt.subplots(figsize = (7,5))
    ax = sns.heatmap(corr, vmax = 1, vmin= -1)
    st.pyplot(fig)
    