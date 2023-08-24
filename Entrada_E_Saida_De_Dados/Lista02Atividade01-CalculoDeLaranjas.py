'''
1) Uma dúzia de laranjas custa R$ 9,75 no supermercado mais próximo. Escreva um programa que
receba como entrada a quantidade desejada de laranjas e exiba o valor total necessário para
comprá-las. (Dica: uma dúzia corresponde a 12 laranjas. Descubra o preço unitário)
'''

duzia = 12
valor_duzia = 9.75

valor_por_lalanja = valor_duzia / duzia

# Entrada de dados:

qtd_laranjas = int(input('Quantas laranjas deseja: '))

# Tratamento de dados:

valor_necessario = qtd_laranjas * valor_por_lalanja

# Saída de dados: 

print(f'O valor para a compra das laranjas é R${valor_necessario:.2f}')
