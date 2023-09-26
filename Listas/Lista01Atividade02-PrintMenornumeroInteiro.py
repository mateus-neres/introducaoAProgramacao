'''
2. Escreva um programa que crie uma lista com 5 números inteiros informados pelo usuário e
exiba o menor deles:
'''


lista = []
for indice in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista += [numero]
lista.sort()
print(lista)
print(f"O menor número informado é {lista[0]}")