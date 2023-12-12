'''
4. A professora Júlia ensina Geografia e precisa de sua ajuda para escrever um programa que receba
como entrada as 4 notas de cada um dos 50 alunos (teste apenas para 4) de sua turma e exiba:
a. a média de cada aluno e uma mensagem informando se ele foi aprovado ou reprovado
b. a quantidade total de alunos aprovados (média igual ou superior a 8.0)
c. a média geral da turma
d. a maior média obtida
'''

notaTotalTurma = 0
maiorMedia = 0
mediaTurma = 0
mediaAluno = 0
alunosAprovados = 0
contadorNotas = 0
contadorAluno = 0
notaTotal = 0

while contadorAluno < 4:
    while contadorNotas < 4:
        nota = float(input("Digite a nota: "))
        notaTotal += nota
        contadorNotas += 1
    mediaAluno = notaTotal / 4
    if mediaAluno >= 8:
        print(f'O aluno teve media {mediaAluno:.2f} e foi aprovado.')
        alunosAprovados += 1
    else:
        print(f"O aluno teve media {mediaAluno:.2f} e foi reprovado.")
    if mediaAluno > maiorMedia:
        maiorMedia = mediaAluno
    notaTotalTurma += mediaAluno
    notaTotal = 0
    contadorNotas = 0    
    contadorAluno += 1
mediaTurma = notaTotalTurma / 4

print(f"Alunos aprovados:{alunosAprovados}")
print(f"Média da turma: {mediaTurma:.2f}")
print(f"Maior média obtida: {maiorMedia:.2f}")