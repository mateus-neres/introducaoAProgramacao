'''2. Escreva uma função ContaVogais que receba um String e retorne a quantidade de vogais
presentes nele. Desconsidere o uso de acentos nas palavras.'''

from bibiLetras import contaVogal

string = str(input("Digite uma palavra:\n")).lower()

print(contaVogal(string))