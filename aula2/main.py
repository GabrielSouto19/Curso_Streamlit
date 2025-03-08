import streamlit as st 
import pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(empresas):
    acoes = " ".join(empresas)
    print(acoes)
    dados_acao = yf.Tickers(empresas)
    cotacoes_acao = dados_acao.history(period="1d",start="2010-01-01",end="2025-03-06")
    cotacoes_acao = cotacoes_acao["Close"]


    return cotacoes_acao



acoes = ["ITUB4.SA","PETR4.SA","MGLU3.SA","VALE3.SA","ABEV3.SA","GGBR4.SA"]
dados = carregar_dados(acoes)
# todas as ações que terminam com SA , são da bolsa brasileira



st.write("# Meu sistema de correlação de ações")
lista_acoes = st.multiselect("Selecione as ações que deseja aplicar o filtro",dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1 :
        acao_unica = lista_acoes[0]
        dados  = dados.rename(columns={acao_unica:"Close"})
# preparação para visualização de do gráfico com filtros 


st.line_chart(dados)
st.write("# Fim do meu programa")