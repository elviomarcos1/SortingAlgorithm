from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from Heap_Sort import media_heap_sort
from SelectionSort import media_selection_sort
from Insertion_Sort import Media_Insertion_Sort

# Definindo tamanhos de dados de 200 em 200
quantidades = np.arange(200, 5000 + 1, 200)

# Dicionário para armazenar os tempos de execução em milissegundos
tempos_heap_sort = []
tempos_selection_sort = []
tempos_insertion_sort = []

for tamanho in quantidades:
    tempos_heap_sort.append(media_heap_sort(tamanho) * 1000)  # Converte para milissegundos
    tempos_selection_sort.append(media_selection_sort(tamanho) * 1000)  # Converte para milissegundos
    tempos_insertion_sort.append(Media_Insertion_Sort(tamanho) * 1000)  # Converte para milissegundos

# Criando um DataFrame
df = pd.DataFrame({
    'quantidade_dados': quantidades,
    'Heap Sort (O(n log n))': tempos_heap_sort,
    'Selection Sort (O(n^2))': tempos_selection_sort,
    'Insertion Sort (O(n^2))': tempos_insertion_sort
})

# Criando o gráfico com plotly.graph_objects para maior controle
fig = go.Figure()

# Adicionando as linhas para cada algoritmo
fig.add_trace(go.Scatter(x=df['quantidade_dados'], y=df['Heap Sort (O(n log n))'],
                         mode='lines', name='Heap Sort (O(n log n))',
                         line=dict(color='orange', width=2)))
fig.add_trace(go.Scatter(x=df['quantidade_dados'], y=df['Selection Sort (O(n^2))'],
                         mode='lines', name='Selection Sort (O(n^2))',
                         line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=df['quantidade_dados'], y=df['Insertion Sort (O(n^2))'],
                         mode='lines', name='Insertion Sort (O(n^2))',
                         line=dict(color='green', width=2)))

# Configurações do layout do gráfico
fig.update_layout(
    title='Comparação de Algoritmos de Ordenação (Escala Semilogarítmica)',
    xaxis_title='Número de Dados Aleatórios',
    yaxis_title='Tempo de Execução (Milissegundos)',
    yaxis_type="log",  # Escala logarítmica no eixo Y
    font=dict(family="Arial", size=12),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    plot_bgcolor="white",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='gray', dtick=200),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='gray'),
    margin=dict(l=40, r=40, t=40, b=40),
    height=600  # Aumentando a altura do gráfico
)

# Configurando as linhas de grade
fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)

# Criando o aplicativo Dash
app = Dash()

app.layout = html.Div(
    children=[
        html.H1(children='Comparação de Algoritmos de Ordenação (Escala Semilogarítmica)', style={'textAlign': 'center'}),
        html.Div(
            dcc.Graph(id='graph-content', figure=fig, style={'width': '100%'}),  # Ocupa 100% da largura da tela
            style={'display': 'flex', 'justify-content': 'center', 'width': '100%'}  # Centraliza e ajusta à tela
        )
    ],
    style={'textAlign': 'center'}  # Centraliza todo o conteúdo da página
)

if __name__ == '__main__':
    app.run(debug=True)
