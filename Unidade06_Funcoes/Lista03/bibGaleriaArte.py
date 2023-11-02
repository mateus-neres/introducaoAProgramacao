'''bibGaleriaArte
 Função consultaPreco  recebe como entrada o título de uma obra e retorna
seu valor em Reais
 Função consultaArtista  recebe como entrada o nome de uma obra e retorna
o nome do artista responsável por ela
 Função consultaQuantObras  recebe como entrada o nome de um artista e
retorna a quantidade de obras dele que existem na galeria
 Função consultaTipo  recebe como entrada o nome de uma obra e retorna
seu tipo: Quadro ou Escultura'''

import random

def consultaPreco (obra):
    return random.randint(2,8) * random.choice([132.40, 275.81, 98.66])

def consultaArtista (obra):
    nome = random.choice(["Manoel Gomes", "Dênis Novaes", "Adélia Machado", "Patrícia Lisboa", "Leonardo Resende"])    
    return nome

def consultaQuantObras (artista):
    return random.randint(0,5)

def consultaTipo (obra):
    return random.choice(["Quadro", "Escultura"])