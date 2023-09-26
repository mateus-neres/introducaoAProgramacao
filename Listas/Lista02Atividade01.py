'''
1. Escreva um programa que receba como entrada quinze letras, armazene-as em uma lista,
e depois exiba quantas vezes uma letra qualquer informada pelo usuário aparece na lista.
'''


lista = []
for i in range(15):
    listaLetra = ["a","b","g","g","j","y","y","y","y","k","l","t","e","e","e",]
    letra = listaLetra[i]
    lista += [letra]
    contador = lista.count("y")
    

print(letra)
print(contador)
print(lista)
