'''
3. Escreva um programa que receba como entrada os dados de visitação de um museu em seis
meses quaisquer (mês + quantidade de visitantes), e utilize a biblioteca Ano para calcular e
exibir o total de visitantes registrados na primavera.
'''
import random
import Ano
# BLOCO DE TESTES
teste1 = ["janeiro","fervereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
visita_teste = [88, 86, 93, 87, 83, 99, 90, 99, 94, 82, 81, 100]


# PROGRAMA
meses = []
qtd_visita_primavera = 0  
for i in range(6):
    aleatorio = random.randint(1,11) # número aleatorio para seleção do mês

    mes = str.upper(teste1[aleatorio])
    qtd_visita = int(visita_teste[aleatorio])

    if str.upper(Ano.defineEstacao(mes)) == "PRIMAVERA":
        qtd_visita_primavera += qtd_visita
        meses.append(mes)

print(meses)
print(qtd_visita_primavera)
