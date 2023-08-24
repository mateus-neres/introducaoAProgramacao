'''
1. Escreva um programa que receba como entrada um número e exiba uma mensagem
informando se ele é positivo, negativo ou neutro.
Lembrete: Os números maiores que zero são chamados de positivos, enquanto os
números menores que zero são os negativos. Zero é um número neutro.
'''

# Entrada de Dados:

numero = int(input('Digite um número: '))

# Tratamento de dados:

if numero > 0:
    print(f'O número {numero} é positivo!')
elif numero < 0:
    print(f'O número {numero} é negativo!')
else:
    print(f'O número {numero} é neutro!')
