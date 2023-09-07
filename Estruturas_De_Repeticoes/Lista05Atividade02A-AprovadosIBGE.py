'''
2. O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma
prova de português com 50 questões, outra de matemática com 35 questões, e uma prova de redação.

Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática,
e ter nota igual ou superior a 7 na redação.

Escreva um programa que receba como entrada, para cada candidato, a quantidade de questões certas em
português e em matemática, e também a nota na redação, e depois exiba quantos candidatos foram aprovados. A
entrada de dados deve ser encerrada quando for informada uma quantidade de questões de português negativa.
'''

aprovadoPT = 40
aprovadoMat = 21
aprovadoRed = 7
contAprovado = 0

portugues = int(input("Digite a quantidade de acertos em português: "))
while portugues >= 0:    
    matematica = int(input("Digite a quantidade de acertos em matemática: "))
    redacao = float(input("Digite a nota em redação: "))
    portugues = int(input("Digite a quantidade de acertos em português: "))
    if portugues >= aprovadoPT:
        if matematica >= aprovadoMat:
            if redacao >= aprovadoRed:
                contAprovado += 1
print(contAprovado)


