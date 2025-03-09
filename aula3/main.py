import streamlit as st 
import pandas as pd
import yfinance as yf
from datetime import timedelta


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

st.sidebar.header("Filtros")

# Filtro de ações
lista_acoes = st.multiselect("Selecione as ações que deseja aplicar o filtro",dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1 :
        acao_unica = lista_acoes[0]
        dados  = dados.rename(columns={acao_unica:"Close"})
# preparação para visualização de do gráfico com filtros 

# filtro de datat
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
print(data_inicial)
print(data_final)

intervalo_datas = st.sidebar.slider("Selecione o período",min_value=data_inicial,max_value=data_final,value=(data_inicial,data_final),step=timedelta(days=15))


dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]


print(dados)
st.line_chart(dados)
st.write("# Fim do meu programa")
