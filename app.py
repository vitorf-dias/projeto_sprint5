import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados

st.header('Visualizador de dados')

# Slider para escolher quantas linhas mostrar
qtd_linhas = st.slider(
    'Quantas linhas você quer visualizar?',
    min_value=5,
    max_value=len(car_data),
    value=10
)

# Exibindo o DataFrame com a quantidade escolhida de linhas
st.dataframe(car_data.head(qtd_linhas))

st.header('Relação Preco x Modelo')

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="model", y="price", nbins=50,
                       title="Distribuição de Preços dos Carros")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

st.header('Compare o preço de diferentes carros')
# título do aplicativo

coluna_x = st.selectbox('Escolha o eixo X', car_data.columns.tolist())
# escolhendo os dados da coluna para o eixo X
coluna_y = st.selectbox('Escolha o eixo Y', car_data.columns.tolist())
# escolhendo os dados da coluna para o eixo Y
fig = px.scatter(car_data, x=coluna_x, y=coluna_y)
# exibir um gráfico interativo
st.plotly_chart(fig, use_container_width=True)
# criando um gráfico de dispersão interativo

st.header('Comparação de preços por modelo')

# Agrupar por modelo e calcular o preço médio
preco_medio_modelo = car_data.groupby('model')['price'].mean().reset_index()

# Ordenar do maior para o menor preço
preco_medio_modelo = preco_medio_modelo.sort_values('price', ascending=False)

# Deixar o usuário escolher quantos modelos quer ver
qtd_modelos = st.slider('Quantos modelos mostrar?',
                        min_value=5, max_value=50, value=15)

# Pegar só os N primeiros
top_modelos = preco_medio_modelo.head(qtd_modelos)

# Criar o gráfico de barras
fig = px.bar(
    top_modelos,
    x='model',
    y='price',
    title=f'Preço médio dos {qtd_modelos} modelos mais caros',
    labels={'model': 'Modelo', 'price': 'Preço médio (US$)'}
)

st.plotly_chart(fig, use_container_width=True)
