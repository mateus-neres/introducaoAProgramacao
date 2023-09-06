'''
5. Escreva um programa que receba como entrada a quantidade de filhos dos vários funcionários de uma
empresa, até que seja informada uma quantidade negativa, e exiba a quantidade média de filhos do
grupo. (Dica: a média pode ser obtida dividindo-se a soma dos números pela quantidade deles)
'''
contador = 0
soma_filhos = 0
qtd_filhos = 0
while qtd_filhos >= 0:
    qtd_filhos = int(input("Quantos filhos você tem ? "))
    soma_filhos += qtd_filhos
    contador += 1
media_filhos = soma_filhos / contador
print(f"Media total de filhos {contador}")