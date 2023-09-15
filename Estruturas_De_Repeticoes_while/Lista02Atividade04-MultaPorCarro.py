'''
4. Devido aos altos índices de poluição, uma cidade resolveu multar as casas que possuem mais de 2 veículos em R$
10 por mês por cada veículo extra. Escreva um programa que receba como entrada a quantidade de veículos de
várias residências, até que seja informado o valor 555, e exiba a multa de cada casa e o total mensal arrecadado
com as multas.
'''
# Variaveis
casa = 0
multa = 10
total_arrecadado = 0
multa_mensal = 0
Limite_qtd_veiculo = 2

# Entra de dados
qtd_veiculo = int(input('Quantos veículos tem em sua residência: '))

# Comando de repetição
while qtd_veiculo != 555:
    
    if qtd_veiculo > 2: 

       multa_mensal = (qtd_veiculo - Limite_qtd_veiculo) * multa 
       total_arrecadado += multa_mensal
       casa += 1
       print(f'O valor da multa da casa {casa} é de R${multa_mensal:.2f}.')
       qtd_veiculo = int(input('Quantos veículos tem em sua residência: '))
    else:   
        qtd_veiculo = int(input('Quantos veículos tem em sua residência: '))
        casa += 1   

print(f'O valor arrecadado total é de: R${total_arrecadado:.2f}.')