'''
7. Luíz Carlos é um carteiro muito comprometido com seu trabalho. Ele participou de uma reunião
recente em que foi informado de que deveria entregar pelo menos 100 correspondências por
dia para dar conta do grande fluxo de envios na época de Natal.

Escreva um programa que receba como entrada a quantidade de correspondências entregues
por ele em cada um dos sete dias da semana, e exiba em quantos dias ele cumpriu a meta, e a
média de entregas diárias que ele fez no período.
'''
entregas_acumuladas = 0
cont_meta = 0
cont_dias = 0
for dias in range(1,8):
    entregas = int(input(f"Quantas correspondências foiram entregues no {dias}°: "))
    entregas_acumuladas += entregas
    cont_dias += 1
    if entregas >= 100:
        cont_meta += 1
media = entregas_acumuladas // cont_dias
print(f"Cumpriu a meta em {cont_meta} dias")
print(f"Média de entregas: {media}")