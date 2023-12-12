'''3) Escreva um programa que utilize as funções da biblioteca criada na questão 2 para receber como
entrada cinco números e exibir quantos deles são múltiplos de 4.'''
import bibNumeros

cont = 0
for i in range(5):
    a = int(input(f"Digite o {i+1}° número: \n"))
    if bibNumeros.testaMultiplo4(a) == True:
        cont += 1
print(cont)