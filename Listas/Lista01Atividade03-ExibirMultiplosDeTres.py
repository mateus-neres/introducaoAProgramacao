'''
3. Escreva um programa que crie uma lista com 8 números inteiros informados pelo usuário e
exiba apenas aqueles que são múltiplos de 3.
'''

lista_teste = [3,15,10,20,45,8,9,12]

lista = []
lista_Multiplos = []

for i in range (8):

    numero = int(input("Digite um número intenrio: "))  # lista_teste[i]
    lista.append(numero)

    if numero % 3 == 0:
        lista_Multiplos.append(numero)

print(lista)
print(f"Dentre os números digitados, os seguintes são multiplos de 3, {lista_Multiplos}.")
