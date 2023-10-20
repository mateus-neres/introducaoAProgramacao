'''
4. Escreva um programa que receba como entrada os dados de visitação de um museu em seis
meses quaisquer (mês + quantidade de visitantes), e utilize a biblioteca Ano para calcular e
exibir a estação do ano em que foi registrado o maior número de visitantes em um único mês.
'''

import random
import Ano
# BLOCO DE TESTES
teste1 = ["janeiro","fervereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
visita_teste = [88, 86, 93, 87, 83, 99, 90, 99, 94, 82, 81, 100]


# PROGRAMA
estacao = ""
mes_mais_visitado = visita_teste[0]
for i in range(6):
    aleatorio = random.randint(1,11) # número aleatorio para seleção do mês

    mes = str.upper(teste1[aleatorio])
    qtd_visita = int(visita_teste[aleatorio])

    if mes_mais_visitado < qtd_visita:
        mes_mais_visitado = qtd_visita
        estacao = Ano.defineEstacao(mes)

print(estacao)