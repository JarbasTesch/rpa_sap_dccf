from datetime import datetime

hoje = datetime.now()

#mes_atual = hoje.month
ano_atual = hoje.year

mesatual = int(input('Qual mês?'))

mes_balanco = mesatual - 2

print(f'Mês: {mes_balanco}\nAno: {ano_atual}\n\n')

if mes_balanco == 0:
    mes_balanco = 12
    ano_atual -= 1

if mes_balanco == -1:
    mes_balanco = 11
    ano_atual -= 1

print(f'@@@@@@@@@@@@@@@@@\nMês: {mes_balanco}\nAno: {ano_atual}\n\n')