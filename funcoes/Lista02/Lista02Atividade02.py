'''
2. A figura a seguir representa a distribuição das estações do ano ao longo dos meses. Crie uma
biblioteca chamada Ano, e escreva nela uma função defineEstacao que receba como entrada o
nome de um mês e retorne a estação do ano que ocorre naquele mês.
'''
import Ano

teste1 = ["janeiro","fervereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

for i in range(len(teste1)):
    mes = str.upper(teste1[i])
    print(mes)
    estacao = Ano.defineEstacao(mes)
    print(estacao)