'''
6. Talita está preocupada com o desempenho de seu filho na escola. No semestre passado, o
boletim estava cheio de notas baixas e ele corre o risco de repetir de ano.

Para motivá-lo, ela propôs um desafio: se ele conseguir melhorar de desempenho
a cada avaliação mensal, durante seis meses, ganhará um brinquedo novo! Ou seja, para
mostrar que ele está se esforçando, cada nota terá que ser superior à anterior.

Escreva um programa que receba como entrada as 6 notas do filho de Talita e exiba uma
mensagem informando se ele ganhará brinquedo ou não.
'''
menor_nota = 0
maior_nota = 0
for contMes in range(1,7):
    nota = float(input(f"Digite a nota do {contMes}° mês: "))
    if nota > maior_nota:
        maior_nota = nota
        maior_nota += 1
    elif maior_nota <= nota:
        menor_nota += 1
if menor_nota >= 1:
    print("Não ganha brinquedo")
else:
    print("Ganha brinquedo")