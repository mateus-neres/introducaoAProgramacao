'''6) Escreva um programa que receba como entrada 6 letras e, usando a função da biblioteca criada na
questão 5, exiba quantas dessas letras são vogais.'''
import bibLetras

contVogal = 0
vogais = []

for i in range(6):

    vogal = str.lower(input(f"Digite a {i+1}° letra para testar se é vogal: \n"))
    
    if bibLetras.testaVogal(vogal) == True:
        vogais.append(vogal)
        contVogal += 1

print(vogais)
print(contVogal)