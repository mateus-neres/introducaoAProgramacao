# bibGaleriaArte

#  Função consultaPreco  recebe como entrada o título de uma obra e retorna seu valor em Reais
def consultaPreco(obra, lista):
    valor_Obra = 0
    for i in range(len(lista)):
        if obra.upper() in lista[i][1]:
            valor_Obra = lista[i][2]
    return valor_Obra

#  Função consultaArtista  recebe como entrada o nome de uma obra e retorna o nome do artista responsável por ela
def consultaArtista(obra, lista):
    for i in range(len(lista)):
        if obra.upper() in lista[i][1]:
            return lista[i][0]
        
#  Função consultaQuantObras  recebe como entrada o nome de um artista e retorna a quantidade de obras dele que existem na galeria
def consultaQuantObras(nome, lista):
    cont_obra = 0
    for i in range(len(lista)):
        if nome in lista[i][0]:
            cont_obra += 1
    return cont_obra

#  Função consultaTipo  recebe como entrada o nome de uma obra e retorna seu tipo: Quadro ou Escultura
def consultaTipo(obra, lista):
    tipo_obra = ""
    for i in range(len(lista)):
        if obra in lista[i][1]:
            tipo_obra = lista[i][3]
    return tipo_obra