'''
2. Vladimir trabalha em uma papelaria da cidade que oferece serviços de xérox e encadernação. Os
preços cobrados são os seguintes:

Serviço Preço
Xérox em preto e branco R$ 0,06 (cada)
Xérox colorida R$ 0,29 (cada)
Encadernação (até 100 folhas) R$ 2,00
Encadernação (mais de 100 folhas) R$ 4,00

Escreva um programa que receba como entrada o tipo de serviço (xérox ou encadernação) preferido
por um cliente, e a quantidade de páginas para copiar ou de folhas para encadernar. O programa
deverá também calcular e exibir o valor total a ser pago. Observe que, caso o usuário opte por xérox,
será necessário receber como entrada também o tipo de xérox (PB ou colorida).
'''

# Variaveis

xerox_preto_branco = 0.06
xerox_colorida = 0.29
encadernacao_ate_100_folhas = 2.00
encadernacao_mais_de_100_folhas = 4.00

servico = str.upper(input("Digite o tipo de serviço, xérox ou encadernação: "))
folhas = int(input("Digite a quantidade de folhas: "))

if servico == "XÉROX" or servico == "XEROX":
    preto_branco = str.upper(input("Deseja a xérox PB ou colorida: "))
    if preto_branco == "PB":
        valor_pago = folhas * xerox_preto_branco
    else:
        valor_pago = folhas * xerox_colorida
elif servico == "ENCADERNAÇÃO" or servico == "ENCADERNAÇAO":
    if folhas <= 100:
        valor_pago = encadernacao_ate_100_folhas
    else:
        valor_pago = encadernacao_mais_de_100_folhas

print(f"{valor_pago:.2f}")



