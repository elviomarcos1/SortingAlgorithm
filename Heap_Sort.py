from Create_Data import create_data
import time

lista_datas = create_data(5001)

def heapsort(arr):
    n = len(arr)

    def heapfy(arr, n, i):
        largest = i
        left = 2 * i + 1
        rigth = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if rigth < n and arr[rigth] > arr[largest]:
            largest = rigth

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapfy(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapfy(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapfy(arr, i, 0)


def media_heap_sort():

    lista_tempo = []

    for i in range(10):
        tempo_inicio = time.time()
        heapsort(lista_datas)
        tempo_fim = time.time()

        lista_tempo.append(tempo_fim - tempo_inicio)

    return round(sum(lista_tempo) / len(lista_tempo), 2)

