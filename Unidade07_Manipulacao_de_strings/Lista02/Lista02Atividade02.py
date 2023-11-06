# 2. Escreva uma função contaPalavras que receba como parâmetro uma frase
# e retorne a quantidade de palavras dela.

def contaPalavras(str):
    str = str.split(" ")
    return len(str)
