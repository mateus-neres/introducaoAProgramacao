# 3. Escreva uma função contaInicioVogal que receba como parâmetro uma lista de palavras
# e retorne a quantidade de palavras iniciadas por vogais.

def contaInicioVogal(lista):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    contador = 0
    for i in range(len(lista)):
        if lista[i][0].lower() in vogal:
            contador += 1
    return contador


nomes = ['Wilson', 'Anderson', 'Luis', 'Mateus ', 'Marco', 'Sabrina']

print(contaInicioVogal(nomes))