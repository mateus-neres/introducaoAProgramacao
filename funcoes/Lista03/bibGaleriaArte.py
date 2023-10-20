'''
Emília trabalha em uma galeria de arte e está usando um novo aplicativo para gerenciar os
quadros e esculturas disponíveis. O aplicativo utiliza a seguinte biblioteca de funções:

bibGaleriaArte
'''

# Função consultaPreco  recebe como entrada o título de uma obra e retorna seu valor em Reais
def consultaPreco(A,B):
    valor = 0
    for i in range(len(B)):
        if A in B[i][0]:
            valor = B[i][3]
    return valor

# Função consultaArtista  recebe como entrada o nome de uma obra e retorna o nome do artista responsável por ela
def consultaArtista(A, B):
    nome = ""
    for i in range(len(B)):
        if A in B[i][1]:
            nome = B[i][1]
    return nome

# Função consultaQuantObras  recebe como entrada o nome de um artista e retorna a quantidade de obras dele que existem na galeria
def consultaQuantObras(A,B):
    contObra = 0
    for i in range(len(B)):
        if A in B[i][1]:
            contObra += 1
    return contObra

# Função consultaTipo  recebe como entrada o nome de uma obra e retorna seu tipo: Quadro ou Escultura
def consultaTipo(A,B):
    tipo = ""
    for i in range(len(B)):
        if A in B[i][0]:
            tipo = B[i][2]
    return tipo