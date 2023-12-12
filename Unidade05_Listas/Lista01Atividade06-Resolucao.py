'''
6. Escreva um programa que crie uma lista com as quantidades de alunos de 4 turmas, e exiba a
quantidade total de alunos.
'''


lista_aluno_turma = []
soma_aluno = 0
for i in range(4):
    qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
    lista_aluno_turma.append(qtd_alunos)
    soma_aluno += qtd_alunos

print(lista_aluno_turma)
print(f"Quantidade total de alunos é de: {soma_aluno}")