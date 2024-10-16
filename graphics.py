from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
from Heap_Sort import media_heap_sort
from SelectionSort import media_selection_sort

# Exemplo de DataFrame com dados de diferentes algoritmos
quantidade_dados = 5000

# Simulando tempos de execução para diferentes algoritmos
algoritmos = {
    'Selection Sort': np.linspace(0, media_selection_sort(), quantidade_dados),
    'Heap Sort': np.linspace(0, media_heap_sort(), quantidade_dados),
    'Quick Sort': np.linspace(0, 0.2, quantidade_dados)
}

# Criando um DataFrame
df_list = []
for alg, tempos in algoritmos.items():
    df_list.append(pd.DataFrame({
        'quantidade_dados': np.arange(1, quantidade_dados + 1),
        'tempo_algoritmo': tempos,
        'algoritmo': alg
    }))

df = pd.concat(df_list)

app = Dash()

app.layout = [
    html.H1(children='Comparação de Tempo de Execução dos Algoritmos', style={'textAlign': 'center'}),
    dcc.Graph(id='graph-content')
]

# Criar o gráfico
fig = px.line(df, x='quantidade_dados', y='tempo_algoritmo', color='algoritmo',
               title='Comparação de Tempo de Execução dos Algoritmos')

# Ajuste do gráfico
fig.update_traces(mode='lines')

app.layout[1] = dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run(debug=True)
