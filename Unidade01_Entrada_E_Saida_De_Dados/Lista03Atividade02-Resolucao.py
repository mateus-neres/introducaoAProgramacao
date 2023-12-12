'''
2) Betina trabalha em um escritório de advocacia e todos os dias analisa vários processos. Sabendo
que ela cumpre um expediente diário de 8h, escreva um programa que receba como entrada
quantos minutos ela leva para analisar cada processo, e exiba o total de processos revisados em um
dia de trabalho. (Dica: Uma hora tem 60 minutos, e considere que um processo não pode ser
analisado parcialmente, apenas totalmente)
'''

# Entrada de dados:

diariaEmHoras = 8
horaEmMinutos = 60
diasEmMinutos = diariaEmHoras * horaEmMinutos
analiseEmMinutos = int(input('Digite, quantos minutos Betina leva para analizar um processo? '))

# Tratamento de dados:

qtdProcessos = diasEmMinutos // analiseEmMinutos

#Saida de dados:

print('A quantidade de processos que Betina consegue analisar em um dia de trabalho é {}.'.format(qtdProcessos))