'''
3. No próximo mês será realizada uma grande competição de sinuca entre jogadores de todo o Brasil. O
comitê organizador quer que você faça um programa que receba como entrada o nome e a pontuação
de cada um dos 120 competidores (teste apenas para 4), e exiba o nome do vencedor da competição.
'''

# Variaveis

ponto = 0
novaPontuacao = 0
cont = 0

# Estrutuda de repetição

while cont <= 3:

    # Entrada de dados
    
    nome = input("Digite nome: ")
    ponto = int(input("Digite a pontuação: "))

    # Estrutura condicional
                
    if ponto > novaPontuacao:

        # Tratamento de dados
                
        nomeVencedor = nome
        novaPontuacao = ponto
                
    cont += 1

print(f'{nomeVencedor} venceu a competição com {novaPontuacao} pontos.')