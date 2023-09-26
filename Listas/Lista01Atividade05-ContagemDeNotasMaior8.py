'''
5. Escreva um programa que crie uma lista com 5 notas informadas pelo usuário, e exiba quantas
notas foram acima de 8.
'''

listaNota = []
contNota = 0
for i in range(5):
    nota = float(input("Digite a nota: "))
    listaNota.append(nota)
    if nota > 8:
        contNota += 1
print(f"Quantidade de notas maiores que 8: {contNota}")