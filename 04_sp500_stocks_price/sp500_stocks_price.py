import streamlit as st
import pandas as pd
import base64 # Biblioteca responsável por codificação https://docs.python.org/3/library/base64.html
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

st.title("Aplicativo de Acompanhamento do S&P 500")

st.markdown("""
Esse aplicativo tem por objetivo mostrar os valores de fechamento do [S&P 500](https://pt.wikipedia.org/wiki/S%26P_500) ao longo do tempo.

As informações estão sendo retiradas do Yahoo Finance.         

** Bibliotecas Usadas**: streamli, pandas, base64, matplotlib, seaborn, numpy, yfinance.
""")

st.sidebar.header("Parâmetros das Empresas")