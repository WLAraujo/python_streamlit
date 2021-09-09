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
