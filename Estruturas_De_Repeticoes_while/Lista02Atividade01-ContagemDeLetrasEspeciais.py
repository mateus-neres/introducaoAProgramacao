'''
1. Escreva um programa que receba como entrada várias letras, até que seja informada a letra X (ou x) e exiba
quantas vezes foram lidas as letras especiais K, Y e W.
Dica: as letras podem ser informadas em maiúsculas ou minúsculas.
'''

# entrada de dados: 

contagem = 0
letra = str.upper(input('Digite uma letra: '))

# tratamento de dados: 

while letra != 'X':
    if letra == 'K' or letra == 'Y' or letra == 'W':
        contagem += 1
        print(f'Já foram {contagem} letras especiais')
    letra = str.upper(input('Digite uma letra: '))
print('Acabou')