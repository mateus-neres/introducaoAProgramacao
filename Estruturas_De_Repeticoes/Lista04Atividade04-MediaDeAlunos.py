'''
4. A professora Júlia ensina Geografia e precisa de sua ajuda para escrever um programa que receba
como entrada as 4 notas de cada um dos 50 alunos (teste apenas para 4) de sua turma e exiba:
a. a média de cada aluno e uma mensagem informando se ele foi aprovado ou reprovado
b. a quantidade total de alunos aprovados (média igual ou superior a 8.0)
c. a média geral da turma
d. a maior média obtida
'''

cont=0
totalAlunos = 0
maiorMedia = 0
mediaGeral = 0
alunosAprovados = 0
while(cont!=4):
    nota1=float(input("nota 1: "))
    nota2=float(input("nota 2: "))
    nota3=float(input("nota 3: "))
    nota4=float(input("nota 4: "))
    media=(nota1+nota2+nota3+nota4)/4
    mediaGeral+=media
    if(media>=8):
        print(f"Aluno Aprovado com media {media:.2f}")
        alunosAprovados +=1
        if(maiorMedia<media):
            maiorMedia = media

    else:
        print(f"Aluno reprovado com media {media:.2f}")
    cont+=1
resultadoMediaGeral = mediaGeral / cont

print(f"AlunosAprovados: {alunosAprovados}")
print(f"Media da turma: {resultadoMediaGeral:.2f}")
print(f"Maior Media Obtida: {maiorMedia:.2f}")