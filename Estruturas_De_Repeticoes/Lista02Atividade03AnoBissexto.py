'''
3. Escreva um programa que receba como entrada vários anos, até que seja informado um ano negativo, e exiba
quantos anos lidos eram bissextos.
Obs: Há duas possibilidades para um ano ser bissexto:
- se ele for múltiplo de 400
- se ele for múltiplo de 4 mas não for múltiplo de 100
'''
ano = int(input('Digite um ano, para sair digite um número negativo: '))

while ano >= 0:
    if ano % 4 == 0 and ano % 100 != 0:
        print(f'O ano {ano} é um ano bissexto')
        ano = int(input('Digite um ano, para sair digite um número negativo: '))

    elif ano % 400 == 0:
        print(f'O ano {ano} é um ano bissexto')
        ano = int(input('Digite um ano, para sair digite um número negativo: '))
        
    else:
        print(f'O ano {ano} não é um ano bissexto')
        ano = int(input('Digite um ano, para sair digite um número negativo: '))
print('Sair')
    