'''
4) Sheldon tem uma grande coleção de revistas em quadrinhos raras e resolveu doá-las a seus amigos
(Bazinga!!!). Escreva um programa que receba como entrada a quantidade total de revistas e a
quantidade de amigos que serão beneficiados, e exiba quantas revistas cada um vai receber e
quantas sobrarão para Sheldon.
'''

# Entrada de dados:

revistas = int(input('Quantas revistas Sheldon está doando: '))
amigos = int(input('Quantos amigos Sheldon tem: '))

# Tratamento de dados:

revistaPorAmigo = revistas // amigos
quociente = revistas % amigos

# Saida de dados:

print('A quantidade de revista que cada um dos amigos receberá é de {:.0f}, e a quantidade de revista que Sheldon manterá é de {}.'.format(revistaPorAmigo, quociente))