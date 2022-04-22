import yfinance as yf
import streamlit as st
import pandas as pd

# Função que mostra texto markdown no site
st.write(""" 
         # App simples de preço de ações
         
         Mostrando o **preço** de fechamento e **volume** de ações do Google!
         """)

# Obtendo os dados
simbolo = "GOOGL"
dados = yf.Ticker(simbolo)
dataframe = dados.history(period = "1d", start = "2010-5-31", end = "2020-5-31")

# Data frame está no formato 
# Open | High | Low | Close | Volume | Dividends | Stock Splits

st.write("## Preço fechamento")
st.line_chart(dataframe.Close)
st.write("## Volume")
st.line_chart(dataframe.Volume)

# streamlit run 01_stock_price.py