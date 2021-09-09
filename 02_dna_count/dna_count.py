import pandas as pd
import streamlit as st
import altair as alt # Biblioteca de visualização estatística baseada em VEGA (Visualization Grammar)
from PIL import Image # Biblioteca que permite manipulação e grvação de muitos formatos de imagem

# Sobre Altair e Vega:
# https://altair-viz.github.io/
# https://vega.github.io/vega/

# Sobre PIL:
# https://pt.wikipedia.org/wiki/Python_Imaging_Library

# Abrindo a imagem e colocando ela em nosso relatório
imagem = Image.open('dna-logo.jpg')
st.image(imagem, use_column_width=True)

# Colocando o texto introdutório
st.write("""
# Aplicativo para contar nucleotídeos

O aplicativo conta a quantidade de nucleotídeos da sequência de DNA passada.

***
""")

# Texto da caixa de entrada
st.header("Entre com a sequência de DNA")

# Diagramando a caixa de entrada
sequencia = st.text_area("Sequência de Entrada", height = 250)
sequencia = ''.join(sequencia).upper()

# Imprimindo a entrada atual
st.header("Entrada")
st.write(sequencia)

# Realizando a contagem de cada tipo de base de DNA
A = sequencia.count('A')
T = sequencia.count('T')
G = sequencia.count('G')
C = sequencia.count('C')

# Vamos imprimir a informação de algumas maneiras diferentes

# 1. Dicionário
st.subheader("1. Dicionário")
dic = {
    'A' : A,
    'T' : T,
    'G' : G,
    'C' : C
}
dic

# 2. Texto
st.subheader("2. Texto")
st.write(f'Temos {A} adeninas')
st.write(f'Temos {T} timinas')
st.write(f'Temos {G} guaninas')
st.write(f'Temos {C} citosinas')

# 3. Dataframe
st.subheader("3. Dataframe")
df = pd.DataFrame.from_dict(dic, orient = 'index')
df = df.rename({0:'Contagem'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index': 'Nucleotídeos'})
st.write(df)

# 4. Gráfico de barras
st.subheader("4. Gráfico de barras")
p = alt.Chart(df).mark_bar().encode(
    x = 'Nucleotídeos',
    y = 'Contagem'
)
p = p.properties(
    width = alt.Step(80)
)
st.write(p)


