'''3. Escreva um programa que receba como entrada os dados de visitação de um museu em seis
meses quaisquer (mês + quantidade de visitantes), e utilize a biblioteca Ano para calcular e
exibir o total de visitantes registrados na primavera.'''

import Ano

qtd_visita_primavera = 0  
for i in range(6):
    mes = str.lower(input(f"Digite o {i+1}° mês:\n"))
    qtd_visita = int(input("Digite a quantidade visitantes nesse mês:\n"))
    if (Ano.defineEstacao(mes)) == "Primavera":
        qtd_visita_primavera += qtd_visita
print(qtd_visita_primavera)
