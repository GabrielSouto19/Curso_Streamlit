import streamlit as st 
import pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d",start="2010-01-01",end="2025-03-06")
    cotacoes_acao = cotacoes_acao[["Close"]]


    return cotacoes_acao

# todas as ações que terminam com SA , são da bolsa brasileira
dados = carregar_dados("ITUB4.SA")
print(dados)
st.write("# Meu sistema de correlação de ações")
st.line_chart(dados)
st.write("# Fim do meu programa")