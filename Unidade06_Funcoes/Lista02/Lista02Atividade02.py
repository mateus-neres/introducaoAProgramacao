'''2. A figura a seguir representa a distribuição das estações do ano ao longo dos meses. Crie uma
biblioteca chamada Ano, e escreva nela uma função defineEstacao que receba como entrada o
nome de um mês e retorne a estação do ano que ocorre naquele mês.'''

import Ano

mes = str.lower(input("Digite o mês que deseja verificar a estação: \n"))
print(Ano.defineEstacao(mes))