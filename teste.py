from datetime import datetime

hoje = datetime.now()
mes_atual = hoje.month
ano_atual = hoje.year

def mes_ano_balanco(mes, ano):

    mes_balanco = mes - 2
    ano_balanco = ano

    if mes_balanco == 0:
        mes_balanco = 12
        ano_balanco -= 1

    if mes_balanco == -1:
        mes_balanco = 11
        ano_balanco -= 1

    return mes_balanco, ano_balanco

mes_balanco_fechado = mes_ano_balanco(mes_atual, ano_atual)[0]
ano_balanco_fechado = mes_ano_balanco(mes_atual, ano_atual)[1]

print(f'Mês para o balanço fechado: {mes_ano_balanco(mes_atual, ano_atual)[0]}\nAno para o balanço fechado: {mes_ano_balanco(mes_atual, ano_atual)[1]}')
