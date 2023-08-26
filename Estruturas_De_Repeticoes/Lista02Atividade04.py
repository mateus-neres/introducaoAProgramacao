'''
4. Devido aos altos índices de poluição, uma cidade resolveu multar as casas que possuem mais de 2 veículos em R$
10 por mês por cada veículo extra. Escreva um programa que receba como entrada a quantidade de veículos de
várias residências, até que seja informado o valor 555, e exiba a multa de cada casa e o total mensal arrecadado
com as multas.
'''
casa = 0
multa = 10
total_arrecadado = 0
multa_mensal = 0
Lite_qtd_veiculo = 2

qtd_veiculo = int(input('Quantos veículos tem em sua residência: '))

while qtd_veiculo != 555:
    total_arrecadado = total_arrecadado + multa_mensal
    if qtd_veiculo > 2:
       multa_mensal = (qtd_veiculo - Lite_qtd_veiculo) * multa
       
       print(f'O valor da multa da casa {casa} é de R${multa_mensal:.2f}.')
       casa += 1
    qtd_veiculo = int(input('Quantos veículos tem em sua residência: '))
print(f'O valor arrecadado total é de: R${multa_acumulada:.2f}.')