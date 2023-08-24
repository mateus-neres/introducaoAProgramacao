'''
4. A Escola Legal paga seus professores considerando as aulas que eles dão e os projetos que
orientam. Sabendo que são pagos R$ 35 por cada hora de aula, e R$ 80 por cada projeto, escreva
um programa que receba como entrada a quantidade de horas em que um professor esteve em
sala de aula no mês, e a quantidade de projetos orientados por ele, e exiba o salário desse
professor.
'''

# Entrada de dados:

hora_aula = input('Quantas Horas Aulas o professor deu em sala: ')
projetos = input('Quantos projetos o professor o professor orienta: ')

# Tratamento de dados: 

hora_aula_int = int(hora_aula)
projetos_int = int(projetos)

salario = (hora_aula_int * 35) + (projetos_int * 80)

# Saída de dados: 

print(f'O salario do professor será R${salario:.2f}')