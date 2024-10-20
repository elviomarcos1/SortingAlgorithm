import random
from datetime import datetime
import calendar

def create_data(valordata):
    ano_inicial = 1990
    ano_final = 2024
    lista_de_datas = []

    for i in range(valordata):
        ano_random = random.randint(ano_inicial, ano_final)
        mes_random = random.randint(1, 12)
        dia_mes = calendar.monthrange(ano_random, mes_random)[1]
        dia_random = random.randint(1, dia_mes)
        data = datetime(ano_random, mes_random, dia_random)
        
        hora_random = random.randint(0, 23)
        minuto_random = random.randint(0, 59)
        segundos_random = random.randint(0, 59)

        data_final = data.replace(hour = hora_random, minute = minuto_random, second = segundos_random)
        data_formatada = data_final.strftime('%Y-%m-%d %H-%M-%S')
        lista_de_datas.append(data_formatada)
    
    return lista_de_datas