# 2. Ainda considerando as listas da questão anterior, escreva os comandos necessários para:

LA = [["Carol", 4], ["Pedro", 2], ["Laura", 3], ["Alice", 5], ["Luís", 4], ["Ludmila", 6]]
LB = [[7, 2, 5, 1], [9, 4, 3], [6, 8, 0, 2, 1], [4, 5, 10]]

# a) Alterar o número do segundo elemento da lista LA para 3.
LA[1][1] = 3
print(LA)

# b) Acrescentar em LA uma lista com os elementos "Bruno" e 1.
LA.append(["Bruno", 1])
print(LA)

# c) Acrescentar o número 7 ao terceiro elemento de LB.
LB[2].append(7)
print(LB)

# d) Exibir, da lista LA, apenas os nomes associados a números menores que 4.
nomes = []
for i in range(len(LA)):
    if LA[i][1] < 4:
        nomes.append(LA[i][0])
print(nomes)

# e) Exibir o primeiro valor de cada sublista de LB.
primeiroValor = []
for i in range(len(LB)):
    primeiroValor.append(LB[i][0])
print(primeiroValor)