'''
3) Janete vai comemorar seu aniversário numa pizzaria muito badalada. Conversando com o dono, ela
conseguiu uma promoção: a cada 10 rodízios, um será gratuito. Escreva um programa que receba
como entrada a quantidade de pessoas convidadas e o preço do rodízio, e exiba o total a ser pago
com duas casas decimais. (Dica: pense em divisão!)
'''

# Entrada de dados:

rodizioGratuito = 10
pessoas = int(input('Quantas pessoas participarão do aniversario de janete? '))
valorRodizio = float(input('Qual o valor do rodizio? '))

# Processamento de dados:

ganhoRodizio = pessoas // rodizioGratuito
total = (pessoas - ganhoRodizio) * valorRodizio

#saida de dados:

print('Janete pagará R${:.2f}.'.format(total))