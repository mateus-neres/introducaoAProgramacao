'''
2. Marcílio e Aurélio estão disputando a eleição para presidente do Centro Acadêmico. Para ser
considerado vencedor, o candidato deve ter mais votos que seu opositor, e também uma
quantidade de votos superior ao total de votos brancos.

Escreva um programa que receba como entrada os votos de 100 alunos e exiba uma mensagem
informando o nome do eleito. Caso não haja nenhum vencedor, deverá ser exibida uma
mensagem informando que será necessária uma nova votação.
'''

# Variaveis para contagem dos pontos de votação
branco = 0
marcilio = 0
aurelio = 0

# Estrutura de repetição FOR
for contador in range(1,100):
    # Entrada de dados do usuário
    voto = str.upper(input("Digite seu voto: \nMarcílio\nAurélio\nBranco\nVoto: "))
    # Tratamentos de dados do usuario para evitar erros de digitação
    while voto != "MARCÍLIO" and voto != "AURÉLIO" and voto != "BRANCO":
        print("Você digitou algo errado, por gentileza, digite apenas")
        voto = str.upper(input("Marcílio\nAurélio\nBranco\nDigite: "))
    # Comandos condicionais para contagem de votos
    if voto == "MARCÍLIO":
        marcilio += 1
    elif voto == "AURÉLIO":
        aurelio += 1
    elif voto == "BRANCO":
        branco += 1
# Saida de dados de acordo com o desafio 
if aurelio <= branco and marcilio <= branco:
    print("Nova votação")
   
elif aurelio  == marcilio:
    print("Nova votação")
    
elif aurelio > marcilio and aurelio > branco:
    print("Aurélio")
   
elif marcilio > aurelio and marcilio > branco:
    print("Marcílio")
    