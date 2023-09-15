'''
1. Escreva um programa que receba como entrada vários números, até que o usuário não deseje mais
informar, e exiba a soma dos que são múltiplos de 3. (Obs: as entradas da tabela indicam o número e a
resposta do usuário a cada repetição)
'''

# Variaveis

soma = 0

# Estrutura de repetição

repeticao = 'SIM' # Variavel de controle da estrutura de repetição

while repeticao == 'SIM': # Estrutura de repetição

    numero = int(input('Digite um número: ')) # Entrada de dados

    # Estrutura condicional

    if numero % 3 == 0: 
        soma += numero # Tratamento dos dados recebidos

    repeticao = str.upper(input('Deseja continuar, sim ou não? ')) # Variavel de controle da estrutura de repetição

# Saída de dados

print(f'A soma dos numés multiplos de 3 é {soma}.') 
