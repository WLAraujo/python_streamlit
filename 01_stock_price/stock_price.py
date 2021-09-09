import yfinance as yf # Dados sobre o mercado financeiro com fonte no yahoo
import streamlit as st
import pandas as pd

# Abaixo usamos a função write para escrever um texto na nossa página do streamlit
# O texto escrito na função write é em markdown
st.write("""
# App Simples Para Ver Infos de Ações

Aqui mostramos preço de fechamento de ações e volume de ações do Google!
""")

# Definindo o identificador que queremos, no caso queremos o da google
id_emp = 'GOOGL'
# Requisitando os dados baseando-se no identificador, criamos um objeto com os dados da empresa
obj_dados = yf.Ticker(id_emp)
# Construindo um dataframe histórico com base no objeto construido
df_dados = obj_dados.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

# Estrutura do df
# Open High     Low Close       Volume      Dividends       Stock Splits

# Adicionamos à página um gráfico de linha que acompanha o valor de fechamento ao longo do tempo e 
# outro que acompanha o volume de ações ao longo do tempo
st.write("## Valor de fechamento")
st.line_chart(df_dados.Close)
st.write("## Volume")
st.line_chart(df_dados.Volume)

# Para rodar um app usando streamlit use streamlit run programa.py