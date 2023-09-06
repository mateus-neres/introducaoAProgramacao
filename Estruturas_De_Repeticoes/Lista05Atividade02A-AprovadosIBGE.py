'''
2. O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma
prova de português com 50 questões, outra de matemática com 35 questões, e uma prova de redação.

Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática,
e ter nota igual ou superior a 7 na redação.

Escreva um programa que receba como entrada, para cada candidato, a quantidade de questões certas em
português e em matemática, e também a nota na redação, e depois exiba quantos candidatos foram aprovados. A
entrada de dados deve ser encerrada quando for informada uma quantidade de questões de português negativa.
'''

aprovadoPt = 40 # 80% de 50 == 40
aprovadoMat = 21 # 60% de 35 == 21
contador = 0
portugues = int(input("Digite a quantidade de questões acertadas em portugês: "))
while portugues >= 0:
    matematica = int(input("Digite a quantidade de questões acertadas em matematica: "))
    notaredacao = float(input("Digite a nota em redação: "))
    
    if portugues >= aprovadoPt and matematica >= aprovadoMat and notaredacao >= 7:
        contador += 1
    portugues = int(input("Digite a quantidade de questões acertadas em portugês: "))
print(f"Foram aprovados {contador}")


