'''
1. Escreva um programa que receba como entrada quinze letras, armazene-as em uma lista,
e depois exiba quantas vezes uma letra qualquer informada pelo usuário aparece na lista.
'''


# Lista 
letra = []

# Recebe quinze letras do usuário
for i in range(15):
    letrasUsuario = input(f"Digite a {i+1}ª letra: ")
    letra.append(letrasUsuario)

# Pede ao usuário para informar uma letra
letra_procurada = input("Digite uma letra para procurar na lista: ")

# Usa o método count() para contar quantas vezes a letra aparece na lista
ocorrencias = letra.count(letra_procurada)

# Exibe o resultado
print(f"A letra '{letra_procurada}' aparece {ocorrencias} vezes na lista.")
