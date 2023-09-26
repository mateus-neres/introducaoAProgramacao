'''
4. Escreva um programa que crie uma lista com 5 números inteiros informados pelo usuário,
depois some cada elemento com seu próximo, e exiba a lista original e a nova lista resultante.
(Dica: Atenção para o índice limite da lista)
'''

lista = []
listaSoma = []
for i in range(5):
    numero = int(input("Digite um numero inteiro: "))
    lista.append(numero)
    if i >= 1:
        listaSoma.append(lista[i] + lista[i-1])
listaSoma.append(lista[-1])
print(lista)
print(listaSoma)
