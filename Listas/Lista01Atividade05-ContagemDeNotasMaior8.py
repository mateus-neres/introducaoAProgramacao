'''
5. Escreva um programa que crie uma lista com 5 notas informadas pelo usuário, e exiba quantas
notas foram acima de 8.
'''

listaNota = []
notaMaior8 = []

for i in range(5):
    nota = float(input("Digite a nota: "))
    listaNota.append(nota)

for nota in listaNota:
    if nota > 8:
        notaMaior8.append(nota)
    
print(f"Quantidade de notas maiores que 8: {len(notaMaior8)}")