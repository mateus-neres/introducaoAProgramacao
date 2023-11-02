def removevalor(lista, numero):
    novaLista = []
    for i in range(len(lista)):
        if numero is not lista[i]:
            novaLista.append(lista[i])
    return novaLista

lista = [2,14,2,39]

print(removevalor(lista,2))