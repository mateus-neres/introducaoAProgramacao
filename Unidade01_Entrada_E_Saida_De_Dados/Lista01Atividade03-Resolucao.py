'''
3. Sabendo que a Copiadora de Rio Tinto cobra R$ 0,15 por cada cópia feita, escreva um programa
que receba como entrada a quantidade de folhas de um livro e exiba o valor total a ser pago para
copiá-lo com duas casas decimais. (Lembrete: cada folha corresponde a duas páginas - frente e
verso)
'''

# Entrada de dados:

livro = input('Quantas paginas tem seu livro: ')

# Tratamento de dados:

livro_float = float(livro)

valor_a_ser_pago = 0.15 * 2 * livro_float

# Saída de dados:

print(f'O valor a ser pago pelas copias será R${valor_a_ser_pago:.2f}')