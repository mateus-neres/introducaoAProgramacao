'''
3) Escreva um programa que utilize as funções da biblioteca criada na questão 2 para receber como
entrada cinco números e exibir quantos deles são múltiplos de 4.
'''
import bibNumeros

teste1 = [3, 9, 2, 12, 5, 0, 7, 4, 6, 8, 81, 17, 43, 11, 1 ]

cont = 0
for i in range(len(teste1)):
    if bibNumeros.testaMultiplo4(teste1[i]) == True:
        cont += 1
print(cont)