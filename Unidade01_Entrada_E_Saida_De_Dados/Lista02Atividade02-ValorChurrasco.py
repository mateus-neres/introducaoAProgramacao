'''
2) Otávio resolveu organizar um churrasco para comemorar seu aniversário. A estimativa é que cada
pessoa consuma 400 gramas de carne e 6 latas de cerveja. Pelas pesquisas que ele fez no
supermercado de seu bairro, o quilo de carne custará R$ 41 e cada cerveja sairá por R$ 5,20.
Escreva um programa que receba como entrada a quantidade de pessoas que irão para o churrasco
e exiba o valor total que ele gastará com carne e cerveja com duas casas decimais cada um.
'''
consumo_cerveja_por_pessoa = 6
consumo_de_carne_por_pessoa = 400 
quilo = 1000
valor_quilo_carne = 41
valor_cerveja = 5.20

# Entrada de dados:

Quantidade_de_pessoas = int(input('Quantas pessoas participaram do churrasco: '))

# tratamento dos dados:

Valor_gasto_carne = ((valor_quilo_carne / quilo) * consumo_de_carne_por_pessoa) * Quantidade_de_pessoas
valor_gasto_cerveja = (valor_cerveja * consumo_cerveja_por_pessoa) * Quantidade_de_pessoas

# Saída de dados:

print(f'O valor a ser pago pelo churrasco com carne será de R${Valor_gasto_carne:.2f} e cerveja é de {valor_gasto_cerveja:.2f}.')
