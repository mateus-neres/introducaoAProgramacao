'''
4. Luana é voluntária em um asilo que atende 80 velhinhos e está pedindo doações a todos os seus
amigos e conhecidos para comprar material de higiene e alimentos.

Escreva um programa que receba como entrada os valores doados pelos 20 amigos de Luana, e
calcule e exiba o valor arrecadado para cada velhinho.
'''

# Variaveis
velhinhos = 80 # Quantidade de membros do asilo
saldo = 0 # Contagem do valor arrecadado

# Estrutura de repecição "for"
for cont in range(1,6):
    #  Entrada de dados pelo usuário
    doacao = float(input("Digite o valor doado: "))
    # Contagem de valor arrecadado
    saldo += doacao
# Tratamento dos dados
valor_percapito = saldo / velhinhos
# Saida de dados
print(valor_percapito)