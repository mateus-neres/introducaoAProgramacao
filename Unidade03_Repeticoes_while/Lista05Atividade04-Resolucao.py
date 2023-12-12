'''
4. A diretora de um famoso hospital precisa controlar melhor suas despesas. Ela precisa de um programa
que receba como entrada o tipo (crédito ou débito) e o valor de várias movimentações feitas ao longo
do mês, até que seja informado o tipo Sair, e exiba as seguintes informações:

a. a quantidade de créditos realizados
b. o saldo financeiro do hospital (total de créditos menos total de débitos)
c. uma mensagem informando se o saldo foi positivo (maior ou igual a zero)
'''
soma_debito = 0
soma_Credito = 0
contador_credito = 0
contador_debito = 0
saldo = 0
variavel_controle = "NÃO"
while variavel_controle == "NÃO" or  variavel_controle == "NAO":
    tipo = str.upper(input("Crédito ou Débito:  "))
    valor = float(input("valor da movimentação: "))
    if tipo == "CRÉDITO" or tipo == "CREDITO":
        contador_credito += 1
        soma_Credito += valor
    if tipo == "DÉBITO" or tipo == "DEBITO":
        contador_debito += 1
        soma_debito += valor
    saldo = soma_Credito - soma_debito
    variavel_controle = str.upper(input("Deseja sair ? "))

    while variavel_controle != "NÃO" or variavel_controle != "NAO" or variavel_controle != "SAIR":
        print("Digite 'não' para continuar ou 'sair' para encerrar o programa.")
        variavel_controle = str.upper(input("Deseja sair ? "))

print(f"Quantidade de créditos:{contador_credito}") 
print(f"Saldo financeiro: R$ {saldo:.2f}.")
if saldo > 0:
    print("Saldo Positivo")
elif saldo == 0:
    print("Saldo zerado")
else:
    print("Saldo Negativo") 	