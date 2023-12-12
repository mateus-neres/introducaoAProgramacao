'''
3. Escreva um programa que receba como entrada três números e exiba uma mensagem
informando qual é o maior deles. (Dica: desconsidere a entrada de números iguais)
'''

# Entrada de dados:

numero = int(input('Digite um número: '))
numero2 = int(input('Digite mais um número: '))
numero3 = int(input('Digite mais um número: '))

# tratamento de dados:

if numero > numero2 and numero > numero3 :
    print(f'{numero} é maior que {numero2} e {numero3}')
elif numero2 > numero and numero2 > numero3:
    print(f'{numero2} é maior que {numero} e {numero3}')
else:
    print(f'{numero3} é maior que {numero} e {numero2}')