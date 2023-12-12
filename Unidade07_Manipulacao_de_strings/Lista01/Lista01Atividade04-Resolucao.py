'''4. Escreva uma função RemoveA que receba um String, remova todas as letras A, e retorne o
String resultante.'''

from bibiLetras import RemoveA

str = input("Digite um texto: \n").upper()
print(RemoveA(str).capitalize())
