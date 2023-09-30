'''
5. Os professores de Introdução à Programação resolveram fazer uma gincana entre as
turmas de LCC e SI. Os alunos deverão disputar cinco provas, valendo 100 pontos cada
uma. Escreva um programa que receba como entrada e armazene em duas listas
diferentes a quantidade de pontos de cada turma por prova. Após a entrada, o programa
deve calcular e exibir:
a. A quantidade de vitórias de cada equipe
b. A quantidade de empates registrados
c. O curso da equipe vencedora da gincana
'''
disciplina_lcc_teste = ["lcc", "lcc", "lcc", "lcc", "lcc"]
lcc_nota_teste = [90, 80, 70, 95,95]
disciplina_bsi_teste = ["bsi", "bsi", "bsi", "bsi", "bsi"]
bsi_nota_teste = [95, 85, 65, 95, 90]

resultados_bsi = []
resultados_lcc = []

for i in range(5):
    disciplina = str.upper(disciplina_bsi_teste[i])
    nota_prova = float(bsi_nota_teste[i])
    agrupamento = [disciplina, nota_prova]
    resultados_bsi.append(agrupamento)

for i in range(5):
    disciplina = str.upper(disciplina_lcc_teste[i])
    nota_prova = float(lcc_nota_teste[i])
    agrupamento = [disciplina, nota_prova]
    resultados_lcc.append(agrupamento)

cont_vitoria__bsi = 0
cont_vitoria_lcc = 0
cont_impate = 0
for i in range(5):
    if resultados_bsi[i][1] > resultados_lcc[i][1]:
        cont_vitoria__bsi += 1
    elif resultados_lcc[i][1] > resultados_bsi[i][1]:
        cont_vitoria_lcc += 1
    else:
        cont_impate +=1



print(resultados_bsi)
print(resultados_lcc)
print(f"O curso de BSI foi vitorioso {cont_vitoria__bsi} vezes, e LCC {cont_vitoria_lcc} vezes.")
print(f"Houveram  {cont_impate} empates.")
if cont_vitoria__bsi > cont_vitoria_lcc:
    print(f"O curso vitoriosos foi Bacharelado em Sistemas de Informação.")
elif cont_vitoria__bsi == cont_vitoria_lcc:
    print("Houve um empate entre os cursos.")
else:
    print("O curso de Licenciatura em Ciêcia da Computação foi vencedor.")