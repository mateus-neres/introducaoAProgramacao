'''
2. Escreva um programa que crie uma lista com 5 números inteiros informados pelo usuário e
exiba o menor deles:
'''


lista = []

for indice in range(5):
    print(f"{indice}º repetição")
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)
    
menorNumero = lista[0]
print(menorNumero)

for numero in lista:
    if numero < menorNumero:
        menorNumero = numero

print(lista)
print(f"O menor número informado é {menorNumero}")