'''
3. Escreva um programa que crie uma lista com 8 números inteiros informados pelo usuário e
exiba apenas aqueles que são múltiplos de 3.
'''

lista = []
lista_Multiplos = []
for i in range (8):
    numero = int(input("Digite um número intenrio: "))
    lista.append(numero)
    if numero % 3 == 0:
        lista_Multiplos.append(numero)
print(lista)
print(f"Dentre os números digitados, os seguintes são multiplos de 3, {lista_Multiplos}.")
