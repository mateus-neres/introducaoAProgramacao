'''
6. Escreva um programa que crie uma lista com as quantidades de alunos de 4 turmas, e exiba a
quantidade total de alunos.
'''

soma_Aluno = 0
lista_Aluno_Turma = []
for i in range(4):
    qtd_Alunos = int(input("Digite a quantidade de alunos na turma: "))
    lista_Aluno_Turma.append(qtd_Alunos)
    soma_Aluno += qtd_Alunos
print(lista_Aluno_Turma)
print(f"Quantidade total de alunos é de: {soma_Aluno}")