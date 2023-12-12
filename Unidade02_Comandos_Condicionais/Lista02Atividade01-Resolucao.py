'''
1. Escreva um programa que receba como entrada um número e exiba uma mensagem
informando se ele é positivo, negativo ou neutro.
Lembrete: Os números maiores que zero são chamados de positivos, enquanto os
números menores que zero são os negativos. Zero é um número neutro.
'''

# Entrada de dados

num = int(input('Digite um númeor: '))

# Tratamento de dados

if num > 0:  # Comando Condição
    print('positivo') # Saida de dados

elif num < 0:  # Comando Condição
    print('negativo') # Saida de dados

else:  # comando Condição
    print('neutro') # Saida de dados