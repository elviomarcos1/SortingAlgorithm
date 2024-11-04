import random
from datetime import datetime, timedelta

def gerar_datas(qtd):
    datas = []
    for _ in range(qtd):
        # Define um intervalo de tempo
        data_inicial = datetime(2000, 1, 1)
        delta = random.randint(0, 365 * 20)  # até 20 anos de intervalo
        data_aleatoria = data_inicial + timedelta(days=delta)
        # Adiciona hora, minuto e segundo aleatórios
        data_aleatoria += timedelta(hours=random.randint(0, 23),
                                    minutes=random.randint(0, 59),
                                    seconds=random.randint(0, 59))
        datas.append(data_aleatoria.strftime('%d/%m/%Y %H:%M:%S'))
    return datas

if __name__ == "__main__":
    qtd = int(input("Informe a quantidade de datas a serem geradas: "))
    datas_geradas = gerar_datas(qtd)
    for data in datas_geradas:
        print(data)
