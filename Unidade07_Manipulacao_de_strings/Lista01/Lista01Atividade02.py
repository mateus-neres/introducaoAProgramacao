'''2. Escreva uma função ContaVogais que receba um String e retorne a quantidade de vogais
presentes nele. Desconsidere o uso de acentos nas palavras.'''

from bibiLetras import conta_vogal

string = str(input()).lower()

print(conta_vogal(string))