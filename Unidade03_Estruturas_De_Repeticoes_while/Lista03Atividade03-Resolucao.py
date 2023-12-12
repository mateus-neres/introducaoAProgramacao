'''
3. O Ministério da Saúde deseja vacinar contra o sarampo todas as crianças de 3 a 6 anos. Escreva um
programa para ser usado em uma escola que receba como entrada a idade de várias crianças até que o
usuário não deseje mais informar dados, e calcule e exiba a quantidade total de vacinas aplicadas.
'''

# Variaveis

cont = 0 # Variavel de contador

variavel_de_controle = 'SIM' # Variavel de controle 1° passo da estrutura de repetição

# Estrutura de repetição

while variavel_de_controle == 'SIM': # Condição de repetição 2° passo da estrutura de repetição

    # Entrada de dados

    idade = int(input('Digite a idade da criaça: '))

    # Comando condicional

    if idade >= 3 and idade <= 6:
        cont += 1 # Variavel de contador

    variavel_de_controle = str.upper(input('Deseja continuar, sim ou não? ')) # Variavel de controle 3° passo da estrutura de repetição

    # 2° Estrutura de repetição (Induz o usuario a digitar os comandos adequados)

    while variavel_de_controle != 'SIM' and variavel_de_controle != 'NÃO':
        print('Por gentileza, digite apenas, "sim" ou "não"  ou encerrar.')
        variavel_de_controle = str.upper(input('Deseja continuar, sim ou não? '))

        # Saída de dados
        
print(f'O total de vacinas aplicadas foi de {cont}')