def MediaInteiraLista (lista):
    soma = 0
    for i in range (len(lista)):
        soma += lista [i]
    MediaInteiraLista = soma // len(lista)
    return MediaInteiraLista

def MultiplicaLista (lista, valor):
    NovaLista = []
    for i in range (len(lista)):
        mult = lista [i] * valor
        NovaLista.append(mult)
    return NovaLista

def Busca(lista, valor):
    if valor in lista:
        return True
    else:
        return False
    
def ContaOcorrencias(lista, valor):
    cont = 0
    for i in range (len(lista)):
        if valor is lista[i]:
            cont += 1
    return cont

def RemoveValor(lista, valor):
    novaLista = []
    for i in range (len(lista)):
        if valor is not lista[i]:
            novaLista.append(lista[i])
    return novaLista

def SemRepetição(lista):
    novaLista = []
    for i in range(len(lista)):
        if lista[i] not in novaLista:
            novaLista.append(lista[i])
    return novaLista

def TestaOrdenacao(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
    '''cont = 0
    for i in range(len(lista)):
        if lista[i - 1] <= lista[i]:
            cont += 1
    if len(lista) != 1 and len(lista) != 0:
        if (cont + 1) == len(lista):
            return True
    else:
        return False'''





    

    





            
    

        








