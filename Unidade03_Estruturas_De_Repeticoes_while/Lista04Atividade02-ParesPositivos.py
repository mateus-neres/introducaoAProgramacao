'''
2. Escreva um programa que receba como entrada 25 números (teste apenas para 5) e exiba a
quantidade de números que são pares e positivos.
'''
contadorDeNumeros = 0
contador = 0
while contador <= 4:
    numero = int(input("Digite um número "))
    if numero % 2 == 0 and numero >= 0:
        contadorDeNumeros += 1
    contador += 1
print(f'Quantidade {contadorDeNumeros}')
    