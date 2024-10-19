from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
from Heap_Sort import media_heap_sort
from SelectionSort import media_selection_sort  # Certifique-se de que isso também esteja ajustado
from Insertion_Sort import Media_Insertion_Sort

# Definindo tamanhos de dados
quantidades = np.arange(1000, 6000, 1000)

# Dicionário para armazenar os tempos de execução
tempos_heap_sort = []
tempos_selection_sort = []
tempos_insertion_sort = []

for tamanho in quantidades:
    tempos_heap_sort.append(media_heap_sort(tamanho))
    tempos_selection_sort.append(media_selection_sort(tamanho))
    tempos_insertion_sort.append(Media_Insertion_Sort(tamanho))

# Criando um DataFrame
df = pd.DataFrame({
    'quantidade_dados': quantidades,
    'tempo_heap_sort': tempos_heap_sort,
    'tempo_selection_sort': tempos_selection_sort,
    'tempo_insertion_sort': tempos_insertion_sort
})

# Transformando o DataFrame para um formato longo para plotagem
df_melted = df.melt(id_vars='quantidade_dados', 
                    value_vars=['tempo_heap_sort', 'tempo_selection_sort', 'tempo_insertion_sort'], 
                    var_name='algoritmo', 
                    value_name='tempo_algoritmo')

# Criando o aplicativo Dash
app = Dash()

app.layout = [
    html.H1(children='Comparação de Tempo de Execução dos Algoritmos', style={'textAlign': 'center'}),
    dcc.Graph(id='graph-content', figure=px.line(df_melted, 
                                                   x='quantidade_dados', 
                                                   y='tempo_algoritmo', 
                                                   color='algoritmo',
                                                   title='Comparação de Tempo de Execução dos Algoritmos'))
]

if __name__ == '__main__':
    app.run(debug=True)
