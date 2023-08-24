'''
2. Escreva um programa que receba como entrada vários números, até que seja informado o valor 100, e exiba a
média dos números pares.
Dica: a média dos números pares é calculada dividindo-se a soma dos pares pela quantidade de números pares.
Porém, antes de dividir, é preciso testar se a quantidade é maior que zero, pois pode ser que não tenham sido
lidos números pares.
'''

# Entrada de Dados:

contagem = 0
somar_par = 0
numero = int(input('Digite um número: '))

# Tratamento de dados:

while numero > 0 and numero <= 100:
    if numero % 2 == 0:
        contagem = contagem + 1
        somar_par = (somar_par + numero) / contagem
        print(f'Contagem {contagem}')
        print(f'A media entre os pares é {somar_par:.0f}')
    numero = int(input('Digite um número: '))
print('Sair')    