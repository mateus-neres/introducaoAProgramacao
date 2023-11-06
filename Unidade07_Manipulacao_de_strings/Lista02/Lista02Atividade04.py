# 4. Escreva uma função contaMaisDe3 que receba como parâmetro uma lista de palavras
# e retorne a quantidade de palavras com mais de 3 vogais. (Obs: desconsidere a existência de acentos)

def contaMaisDe3(lista_palavra):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    contpalavra = 0
    for i in range(len(lista_palavra)):
        palavra = lista_palavra[i]
        contVogal = 0
        for a in range(len(palavra)):
            if palavra[a] in vogal:
                contVogal += 1
        if contVogal > 3:
            contpalavra += 1
    return contpalavra

lista_palavra = ['Planaltoa', 'Agua Fria', 'Cenaatro', 'Manaira', 'Bnacaeurs', 'mtsranmaei']

print(contaMaisDe3(lista_palavra))