'''
6) Escreva um programa que receba como entrada 6 letras e, usando a função da biblioteca criada na
questão 5, exiba quantas dessas letras são vogais.
'''
import bibLetras

teste1 = ["P", "x", "á", "e", "S", "T", "q", "V", "õ", "i", "L", "U", "c", "m", "r", "Y", "K", "W"]

contVogal = 0
vogais = []

for i in range(len(teste1)):

    vogal = str.lower(teste1[i])
    
    if bibLetras.testaVogal(vogal) == True:
        vogais.append(vogal)
        contVogal += 1

print(vogais)
print(contVogal)