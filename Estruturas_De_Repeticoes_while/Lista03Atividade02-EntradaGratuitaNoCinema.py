'''
2. Hoje à noite, o cinema da cidade será inaugurado com uma promoção: crianças até 10 anos e idosos
com mais de 60 anos não pagarão ingresso. Escreva um programa que receba como entrada a idade de
cada pessoa que foi ao cinema até que o usuário não deseje mais informar dados, e exiba a quantidade
de pessoas que tiveram entrada gratuita. (Obs: as entradas da tabela indicam a idade e a resposta do
usuário a cada repetição)
'''

cont = 0
controle = 'SIM'

while controle == 'SIM':
    idade = int(input('Digite a idade: '))
    if idade <= 10 or idade > 60:
        cont += 1
    controle = str.upper(input('Deseja continuar, sim ou não? '))
print(f'Tiveram {cont} pessoas com entrada gratuita')