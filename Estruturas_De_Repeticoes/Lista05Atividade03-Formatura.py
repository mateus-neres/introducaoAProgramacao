'''
3. No mês que vem os alunos de Informática vão se formar e pretendem realizar uma grande festa. Eles
fizeram os cálculos e chegaram à conclusão de que teriam que estabelecer limites para suas listas de
convidados, pois o local escolhido para o evento é pequeno.

Ficou acertado que cada formando vai pagar R$ 3000 e terá direito a 15 senhas para seus convidados.
Aqueles que tiverem interesse poderão adquirir até 10 senhas extras cada um, ao preço de R$ 42 cada.

Escreva um programa que receba como entrada a quantidade de convidados de vários formandos, até
que não haja mais formandos, e exiba o valor total que será pago por senhas extras, e a quantidade
total de pessoas que estarão presentes na festa.

Dica: não esqueça que os formandos também estarão na festa, mas não precisam de senhas.

Obs: caso o formando tenha um número total de convidados superior ao permitido, deverá ser
considerada a quantidade máxima.
'''
limite_Convidado = 25
convidados_inclusos = 15
convidados_eliminados = 0
contador_pessoas= 0
senhas_Extra = 0
valor_Senha = 42
variavel_Controle = "SIM"

while variavel_Controle == "SIM":
    convidados = int(input("Digite a quantidade de convidados: "))
    if convidados > limite_Convidado:
        convidados_eliminados = convidados - limite_Convidado

    if convidados > convidados_inclusos:
        senhas_Extra = (convidados - convidados_inclusos - convidados_eliminados) * 42
    if convidados > limite_Convidado:
        contador_pessoas += convidados - convidados_eliminados + 1
    else: 
        contador_pessoas += convidados + 1
    variavel_Controle = str.upper(input("Deseja continuar, sim ou não? "))
    
    while variavel_Controle != "SIM" and variavel_Controle != "NÃO":
        print("Digite apenas 'sim' para continuar ou 'não' para encerrar.")
        variavel_Controle = str.upper(input("Deseja continuar, sim ou não? "))
        
print(f"Total a ser pago por senhas extras R${senhas_Extra:.2f}")
print(f"Total de participante {contador_pessoas}")