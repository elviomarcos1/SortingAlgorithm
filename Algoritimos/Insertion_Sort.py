from Data.Create_Data import create_data;
import time

def insertion_sort( lista ):
  for i in range( 1, len( lista ) ):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave


def Media_Insertion_Sort(tamanho):
   lista_datas = create_data(tamanho)
   tempo_inicial = time.time()
   insertion_sort(lista_datas)
   tempo_fim = time.time()
   tempo_final = (tempo_fim - tempo_inicial)
   return tempo_final


   
