'''
3) Regiane vai comemorar o aniversário de seu filho e precisa encomendar docinhos. Cada brigadeiro
custa R$ 1,90 e cada beijinho custa R$ 1,70. Escreva um programa que receba como entrada a
quantidade de brigadeiros e de beijinhos pedidos, e também a quantidade de crianças convidadas,
e exiba o valor total gasto, e a quantidade total de docinhos que cada criança vai comer.
'''
# Entrada de dados:

brigadeiro = int(input('Quantos brigadeiros: '))
beijinho = int(input('Quantidade de beijeinhos: '))
crianca = int(input('Quantas criaçãos participarão: '))

# Tratamento de dados:

consumo: float = (brigadeiro + beijinho) // crianca
custo: float = (brigadeiro * 1.9) + (beijinho * 1.70)

# Saída de dados:

print('O valor total gasto é de R${:.2f}, e cada criança comerá {} docinhos.'.format(custo, consumo))
