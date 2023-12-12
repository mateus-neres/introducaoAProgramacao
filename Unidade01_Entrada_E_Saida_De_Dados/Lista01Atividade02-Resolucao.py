'''
2. A biblioteca de Rio Tinto empresta gratuitamente seus livros a alunos, professores e funcionários
de todo o campus. Entretanto, sempre que um usuário atrasa a entrega de um livro, ele tem que
pagar uma multa de R$ 2,50 por cada dia de atraso.
Escreva um programa que receba como entrada a quantidade de dias de atraso do empréstimo de
um livro, e exiba o valor da multa a ser paga pelo usuário com duas casas decimais.

'''

# Entrada de dados:

dias = input('Quantos dias de atrazo: ')

# Tratamento de dados:

dias_float = float(dias)

multa = dias_float * 2.5

# Saida de dados:

print(f'O valor da multa por atraso será de R${multa:.2f}')