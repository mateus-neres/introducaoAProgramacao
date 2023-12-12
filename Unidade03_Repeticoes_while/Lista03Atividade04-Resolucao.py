# 4. A Secretaria de Planejamento do Estado deseja promover um momento de lazer para as famílias de
# seus funcionários. Escreva um programa que receba como entrada a quantidade de familiares que
# cada funcionário deseja levar, até que o usuário não deseje mais informar dados, e exiba o custo total
# da festa, sabendo que o valor por pessoa é R$ 14. Exiba também a quantidade total de pessoas que
# participarão da festa.

# variaveis 

tota_pago = 0 # valor total do evento 
soma_pessoas = 0 # Qantidade total de familiares no evento
valor_por_pessoa = 14 # Custo por pessoa no evento
variavel_de_controle = 'SIM' # Variavel de controle 1° passo da Estrutura de repetição

# Estrutura de repetição

while variavel_de_controle == 'SIM': # Condição de repetição 2° passo da estrutura de repetição

    # Entrada de dados

    qtd_pessoas = int(input('Digite a quantidade de pessoas: '))

    # Tratamento dos dados 

    soma_pessoas += qtd_pessoas + 1 # Calculo da Quantidade de vamiliares mais funcionarios
    total_pago = soma_pessoas * valor_por_pessoa # Calculo do valor total do evento

    variavel_de_controle = str.upper(input('Deseja continuar, sim ou não? ')) # Variavel de controle 3° passo da estrutura de repetição
    
    # 2° Estrutura de repetição (Induz o usuario ao comando adequado)
    while variavel_de_controle != 'SIM' and variavel_de_controle != 'NÃO':
        print('Por gentileza, digite apenas "sim" para continuar ou "não" para sair')
        variavel_de_controle = str.upper(input('Deseja continuar, sim ou não? '))
        
# Saída de dados 

print(f'Valor total: R${total_pago:.2f}')
print(f'Quantidade de paticipante: {soma_pessoas}')
