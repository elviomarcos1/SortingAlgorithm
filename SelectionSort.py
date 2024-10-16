from Create_Data import create_data
import time

lista_de_datas = create_data(5001)

def selection_sort(lista):
  """ Ordena uma lista. Custo O(n²) """
  
  n = len(lista)

  if n == 1: 
    return lista[0] 

  # Loop externo para iterar sobre os índices da lista
  for i in range(n-1):
    
    menor = i  # primeiro índice inicia como o menor

    # Loop interno para encontrar o índice do menor elemento
    for j in range(i + 1, n):
      if lista[j] < lista[menor]:
        menor = j

    # Se o elemento atual não é o menor, troca
    if lista[i] != lista[menor]:
      aux = lista[i]
      lista[i] = lista[menor]
      lista[menor] = aux

  return lista 

def media_selection_sort():

    lista_tempo = []

    for i in range(10):
        tempo_inicio = time.time()
        selection_sort(lista_de_datas)
        tempo_fim = time.time()

        lista_tempo.append(tempo_fim - tempo_inicio)

    return round(sum(lista_tempo) / len(lista_tempo), 2)
