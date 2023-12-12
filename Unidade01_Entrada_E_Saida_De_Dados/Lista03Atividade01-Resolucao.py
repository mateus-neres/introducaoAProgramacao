'''
1) O doutor Jonas Gutierrez é cardiologista e atende diversos pacientes. Ele recebe R$ 170 por cada
consulta realizada por convênio, e R$ 310 por consulta particular. Escreva um programa que receba
como entrada quantas consultas de convênio e quantas consultas particulares ele realizou em uma
semana, e exiba o valor total recebido por ele.
'''

# Entrada de dados:

convenio = 170
particular = 310
qtdConvenio = int(input('Quantas consultas pelo convenio o Dr. Gutierrez realizou esse mês? '))
qtdParticular = int(input('Quantas consultas particular o Dr. Gutierrez realizou esse mês? '))

# Tratamento de dados:
valorConvenio = (convenio * qtdConvenio)
valorParticular = (particular * qtdParticular)
total = valorParticular + valorConvenio

# Saida de dados:
print('O Dr. Gutierrez, recebeu esse mês o montante de R${:.2f}.'.format(total))