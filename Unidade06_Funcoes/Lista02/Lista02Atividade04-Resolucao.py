'''4. Escreva um programa que receba como entrada os dados de visitação de um museu em seis
meses quaisquer (mês + quantidade de visitantes), e utilize a biblioteca Ano para calcular e
exibir a estação do ano em que foi registrado o maior número de visitantes em um único mês.'''


import Ano

estacao = ""
mes_mais_visitado = 0
for i in range(6):
    mes = str.upper(input(f"Digite o {i+1}° mês:\n"))
    qtd_visita = int(input("Digiete a quantidade de visitante deste mês:\n"))

    if mes_mais_visitado < qtd_visita: 
        mes_mais_visitado = qtd_visita
        estacao = Ano.defineEstacao(mes)

print(estacao)