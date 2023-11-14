# 2. Escreva uma função contaPalavras que receba como parâmetro uma frase
# e retorne a quantidade de palavras dela.

def contaPalavras(str):
    if str != "":
        cont = 1
    else:
        cont = 0
    for i in range(len(str)):
        if str[i] == " ":
            cont += 1
    return cont
a = str(input("Digite uma frase: \n"))

print(contaPalavras(a))