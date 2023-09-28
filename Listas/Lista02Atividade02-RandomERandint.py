'''
2. Escreva um programa que crie uma lista de dez valores aleatórios (Dica: use
random.randint()), e exiba dessa lista:
- O primeiro e o último elemento
- A soma dos cinco primeiros elementos
- O menor elemento
- A quantidade de elementos ímpares
'''

import random
random.seed(1)
lista = []
contaImpar = 0
menor_numero = 0
soma_numeros = 0
for i in range(10):
    numero = random.randint(1,100)
    if numero % 2 == 1:
        contaImpar += 1
    lista.append(numero)
    
menor_numero = lista[0]
for numero in lista:
    if numero < menor_numero:
        menor_numero = numero

for numero in lista[0:5]:
    soma_numeros += numero

print(lista)
print(f"Primeiro elemento é {lista[0]}, o ultimo elemento é {lista[-1]}")
print(f"A soma dos 5 primeiros elemenstos é {soma_numeros}")
print(f"O menor elemento é {menor_numero}")
print(f"Há {contaImpar}, elementos impares.")

