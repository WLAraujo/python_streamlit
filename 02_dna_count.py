import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Adição de imagem
image = Image.open("02_dna_image.PNG")
st.image(image, use_column_width = True)

# Adição do título
st.write("""
         # Contador de Nucleotídeos de DNA
         
         Esse app conta os nucleotídeos que compõem uma sequência de DNA.
         
         ***
         """)

# Entrada
st.header("Entre com a sequência de DNA")
sequencia_padrao = "GAAAAAAGTCCCCCCCGAATTCGTGCCGTTGAAGGTAAA"
sequencia = st.text_area("Sequência de Entrada", sequencia_padrao, height=250)
sequencia = ''.join(sequencia).upper()

# Quebrando a string
split_sequencia = []
for index in range(0, len(sequencia), 90):
    split_sequencia.append(sequencia[index : index + 90])

# Mostrando sequência digitada
st.write("""
         ***
         """)
st.header("Entrada (Sequência de DNA)")
for linha in split_sequencia:
    linha
st.write("""
         ***
         """)


# Contagem de nucleotídeos
A = sequencia.count('A')
T = sequencia.count('T')
G = sequencia.count('G')
C = sequencia.count('C')

# Mostrar como dicionário
st.subheader("1. Dicionário")
dic = {
    'A' : A,
    'T' : T,
    'G' : G,
    'C' : C
}
dic

# Mostrar como texto
st.subheader("2. Texto")
st.write(f'Temos {A} adeninas')
st.write(f'Temos {T} timinas')
st.write(f'Temos {G} guaninas')
st.write(f'Temos {C} citosinas')

# Mostrar como dataframe
st.subheader("3. Dataframe")
df = pd.DataFrame.from_dict(dic, orient = 'index')
df = df.rename({0:'Contagem'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index': 'Nucleotídeos'})
st.write(df)

# Mostrar como gráfico de barras
st.subheader("4. Gráfico de barras")
p = alt.Chart(df).mark_bar().encode(
    x = 'Nucleotídeos',
    y = 'Contagem'
)
p = p.properties(
    width = alt.Step(80)
)
st.write(p)