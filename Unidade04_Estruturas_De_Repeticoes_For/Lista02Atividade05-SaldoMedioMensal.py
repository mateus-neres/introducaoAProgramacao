'''
5. Vitória está fazendo um balanço de suas finanças nesse ano para saber se conseguiu
economizar o suficiente ou não. Escreva um programa que receba como entrada o valor do
salário dela e o valor total de suas despesas em cada mês, e exiba o valor médio economizado
ao longo do ano. (Dica: o salário dela não teve reajuste ao longo dos meses, foi sempre o
mesmo)
'''

# VAriaveis 
gastosAcumulados = 0 # Contadgem de gastos mensais acumulados
contMes = 0 # Contagem de meses
# Entrada de dados pelo usuário
salario = float(input("Digite o salário: "))

# Estrutura de repetição
for cont in range(1,4):
    # Contagem de mês
    contMes += 1
    print(f"Mês {contMes}")
    # Entrada de dados pelo usuário
    despesa = float(input("Digite as despesas do mês: "))
    gastosAcumulados += despesa # Contadgem de gastos mensais acumulados

# Tratamento de dados
salarioAcumulado = salario * contMes # Calculando o total de salario do total de meses
saldo = (salarioAcumulado - gastosAcumulados) / contMes # Calculando o saldo medio
# Saida de dados
print(saldo)