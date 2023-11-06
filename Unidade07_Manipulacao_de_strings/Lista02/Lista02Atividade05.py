# 5. Escreva uma função contaTotalH que receba como parâmetro uma lista de palavras e retorne a
# quantidade total de letras "h", sejam maiúsculas ou minúsculas, presentes em todas elas.

def contaTotalH(Lista_palavras):
    contH = 0
    for i in range(len(Lista_palavras)):
        palavra = Lista_palavras[i]
        for a in range(len(palavra)):
            if palavra[a].upper() == "H":
                contH += 1
    return contH

lista = ["hiato", "pato", "rinoceronte", "elefante", "hgainha", "hiena"]

print(contaTotalH(lista))
