'''
4. A Secretaria de Planejamento do Estado deseja promover um momento de lazer para as famílias de
seus funcionários. Escreva um programa que receba como entrada a quantidade de familiares que
cada funcionário deseja levar, até que o usuário não deseje mais informar dados, e exiba o custo total
da festa, sabendo que o valor por pessoa é R$ 14. Exiba também a quantidade total de pessoas que
participarão da festa.
'''


valor_por_pessoa = 14
pessoas_na_festa = 0
contador_funcionario = 0
variavel_de_controle = "SIM"


while variavel_de_controle == "SIM":

    
    familiares = int(input("Digite a quanditadade de familiares: "))
    contador_funcionario += 1 
    pessoas_na_festa = pessoas_na_festa + familiares

    variavel_de_controle = str.upper(input("Deseja continuar ? Sim ou não ?"))

qtd_total_pessoas = contador_funcionario + pessoas_na_festa
custo_da_festa = qtd_total_pessoas * valor_por_pessoa


print(f"{custo_da_festa:.2f}")

print(qtd_total_pessoas)