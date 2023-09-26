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
for i in range(10):
    numero = random.randint(1,100)
    if numero % 2 == 1:
        contaImpar += 1
    lista.append(numero)

somanumeros = sum(lista[0:5])

print(lista)
print(f"Primeiro elemento é {lista[0]}, o ultimo elemento é {lista[-1]}")
print(f"A soma dos 5 primeiros elemenstos é {somanumeros}")
lista.sort()
print(f"O menor elemento é {lista[0]}")
print(f"Há {contaImpar}, elementos impares.")

