'''
4) Todos os anos, os motoristas devem pagar ao Detran o IPVA (Imposto sobre a Propriedade de
Veículos Automotores) e uma taxa de trânsito. Caso paguem o IPVA com antecedência, recebem um
desconto de 5% apenas no valor desse imposto. Escreva um programa que receba como entrada o
valor do IPVA e o valor da taxa de trânsito, e exiba o total a ser pago por um motorista que deseja
quitar sua dívida cinco dias antes do prazo.
'''

# Entrada de dados:

ipva = float(input('Digite o valor do IPVA: '))
taxa = float(input('Digite o valor da taxa: '))

# tratamento de dados: 

desconto: float = (ipva + taxa) - (ipva * 0.05)

# Saída de dados:

print('Se o ipva for R${:.2f} e a taxa R${:.2f}, pagos com antecedência, o valor do imposto será R${:.2f}'.format(ipva, taxa, desconto))