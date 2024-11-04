import time
import random
import plotly.express as px
import pandas as pd
from Data.Create_Data import gerar_datas
from Algoritimos.Heap_Sort import heap_sort
from Algoritimos.SelectionSort import selection_sort
from Algoritimos.Insertion_Sort import insertion_sort
from datetime import datetime
import numpy as np

def medir_tempo(algoritmo, dados):
    start_time = time.time()
    algoritmo(dados)
    return time.time() - start_time

def main():
    tamanhos = list(range(200, 5200, 200))
    tempos_heap = []
    tempos_selection = []
    tempos_insertion = []

    for tamanho in tamanhos:
        datas = gerar_datas(tamanho)
        dados = [datetime.strptime(data, '%d/%m/%Y %H:%M:%S') for data in datas]
        
        tempos_heap.append(medir_tempo(heap_sort, dados.copy()))
        tempos_selection.append(medir_tempo(selection_sort, dados.copy()))
        tempos_insertion.append(medir_tempo(insertion_sort, dados.copy()))

    resultados = pd.DataFrame({
        'Tamanho': tamanhos,
        'Heap Sort': tempos_heap,
        'Selection Sort': tempos_selection,
        'Insertion Sort': tempos_insertion
    })

    # Criar o gráfico
    fig = px.scatter(resultados, x='Tamanho', y=resultados.columns[1:], 
                     title='Tempo de Execução dos Algoritmos de Ordenação',
                     labels={'value': 'Tempo (s)', 'Tamanho': 'Quantidade de Datas'},
                     log_y=True)

    # Ajustar a linha de fit de grau 2
    for coluna in resultados.columns[1:]:
        x = resultados['Tamanho']
        y = resultados[coluna]
        
        # Calcular os coeficientes do polinômio de ajuste (grau 2 para quadrático)
        coeficientes = np.polyfit(x, y, 2)
        polynomial = np.poly1d(coeficientes)
        
        # Gerar valores de y para a linha de ajuste
        y_fit = polynomial(x)
        
        # Adicionar a linha de ajuste ao gráfico
        fig.add_scatter(x=x, y=y_fit, mode='lines', name=f'Fit {coluna}', line=dict(dash='dash'))

    # Configurar o eixo x para exibir de 200 em 200
    fig.update_xaxes(dtick=200)

    fig.show()

if __name__ == "__main__":
    main()
